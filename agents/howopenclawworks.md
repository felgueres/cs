
# Quick description 

openclaw.mjs ← CLI binary
└→ src/entry.ts ← Process setup, env normalization            
    └→ src/cli/run-main.ts ← CLI framework, command dispatch             
        └→ src/cli/program/build-program.ts ← Commander.js program                
            └→ src/cli/program/command-registry.ts ← Lazy command registration       
                └→ src/cli/program/register.agent.ts ← "openclaw agent" command        
                    └→ src/commands/agent-via-gateway.ts ← Gateway vs local branching  
                        └→ src/commands/agent.ts ← Agent orchestrator          
                            └→ src/agents/pi-embedded-runner/run.ts ← Outer runner
                                └→ src/agents/pi-embedded-runner/run/attempt.ts ← CORE LOOP

1) Instantiate the command line 
2) Build core commands out of the registry
3) Build commands out of the add on plugins
4) Register agent commands 
5) Dispatch to the .action() handler which will direct to either "embedded" meaning locally or to the "gateway" (default)
6) agentViaGatewayCommand() makes an RPC to the Gateway via callGateway({ method: "agent"})

The typical loop runs because you pass "agent" as a command in cli. 

eg. 

$ openclaw agent <subcommands>

1. openclaw agent --message "hi" --to +1...
2. Commander.js parses it, calls the .action() in register.agent.ts
3. That calls agentCliCommand() in src/commands/agent-via-gateway.ts, which conditions on opts.local === true. If true, runs local, otherwise viaGateway. This file validates inputs, build RPC params and calls gateway, and formats response for terminal.
4. ./agent.js -> this runs the agent locally if needed

The core agent loop is identical. Both paths call runEmbeddedPiAgent()

Local:
- Executes in cli process
- Session is read and written to local disk
- Response is blocking, waits for completion 
- Concurrency is single sequential execution

Gateway:
- Agent loop runs on remote gateway server
- Session is managed server-side in gateway's session store
- Response is Queued as a background task, client polls via WebSocket for the final result
- Multiple concurrent runs with deduplication by idempotency key
- Server manages delivery to channels like slack, sms, etc

# Gateway  

Openclaw architecture is hub and spoke style orchestration.
The gateway is a standalone WebSocket + HTTP Server. Hub and Spoke style orchestration.
It's a node.js process and acts as the control plane for all things like agents, channels, scheduling, approvals, sessions, etc.
It gets started with:

```shell
openclaw gateway run 
```

It binds to loopback (self), LAN (local network), or Tailscale (tailscale vpn), use gaeway.bind to config

Websocket is RPC + HTTP for control UI and includes openai compatible api endpoints (/v1/chat/completions, /v1/responses) 

When the Gateway boots it registers many methods as RPC handlers on its websocket server. This happens in `src/gateway/server-methods.ts`, ie. method-name to handler mapping like this { method: "agent", params: {...}}, then the gateway looks up "agent" and calls the corresponding handler.

Some methods are:
[agents] agent, agent.wait, agents.list, agents.create, agents.delete
[chat] chat.send, chat.history, chat.abort
[config] config.get, config.set, config.patch
[cron] cron.list, cron.add, cron.run
[sessions] sessions.list, sessions.preview, sessions.reset
[nodes] node.list, node.invoke, node.pair
[approvals] exec.approval.request, exec.approval.resolve
[channels] channels.status, channels.logout

Each handler lives in its own file under src/gateway/server-methods/ , eg. `agent.ts`,`chat.ts`, `cron.ts`

eg. 

$ openclaw agent --message "hello"

The cli opens a websocket to the Gateway, sends an RPC, and the gateway runs the agent loop server-side. It is essentially a method router over WebSocket. The CLI is just a client sending RPC requests to it.

Why websocket?
- Keeps the connection alive via heartbeat. Server sends signal every 30s. Client tracks last time it received one. If server goes by 1min+, client assumes its dead and closes.
- Allows bidirectional comms.

RPC call is: `callGateway`
Resolve connection details -> open WebSocket -> handshake -> Send one RPC request -> return result -> close
It's a single request wrapped in a Promise
It settles the promise either:
a) Success which makes onHelloOk fire. client.request() returns and promise resolves to result
b) Connection Failure which makes onClose fire before request completes 
c) Timesout

It's not a persistent client, it's fire and forget on each CLI invocation.

callGateway<GatewayAgentResponse>({
method: "agent",           // which RPC handler to invoke on the server           
params: {                                                                                message: body,           // the user's message text
  agentId,                 // which agent to use (e.g., "my-assistant")
  to: opts.to,             // recipient phone number (E.164), used to derive session
  replyTo: opts.replyTo,   // delivery target override
  sessionId: opts.sessionId, // explicit session ID
  sessionKey,              // resolved session key 
  thinking: opts.thinking, // LLM thinking level (off/minimal/low/medium/high)
  deliver: Boolean(opts.deliver), // should the server send the reply to a channel?
  channel,                 // which channel (chat, slack, sms, etc.)
  replyChannel: opts.replyChannel, // channel override for the reply
  replyAccountId: opts.replyAccount, // which account to send from
  timeout: timeoutSeconds, // how long the agent can run
  lane: opts.lane,         // execution lane (for concurrency/priority)
  extraSystemPrompt: opts.extraSystemPrompt, // additional system prompt to inject
  idempotencyKey,          // dedup key — prevents running the same request twice
},
expectFinal: true,         // wait for completion, not just "accepted"
timeoutMs: gatewayTimeoutMs, // client-side WebSocket timeout
clientName: GATEWAY_CLIENT_NAMES.CLI,
mode: GATEWAY_CLIENT_MODES.CLI,
})

Client dispatches RPC via src/gateway/call.ts, callGateway() which creates a GatewayClient and sends a json frame over websocket with method: "agent"

Then the server handles the message:

src/gateway/server/ws-connection/message-handler.ts which receives the websocket frame and calls handleGatewayRequest

Then src/gateway/server-methods.ts handleGatewayRequest() looks up the "agent" method in the coreGatewayHandlers registry, which includes the agentHandlers

Then the rpc handler, src/gateway/server-methods/agent.ts, agentHandlers.agent validates the params, does auth/session setup, and fires the agentCommand() with void (async, no await) and returns "accepted" response to the client.

Then src/commands/agent.ts - agentCommand() resolves the session/workspace/model config, and calls runWithModelFallback(), which runAgentAttempt()

In src/commands/agent.ts, runAgentAttempt branches into runCliAgent() or runEmbeddedPiAgent()

The loop happens at src/agens/pi-embedded-runner/run.ts, with runEmbeddedPiAgent which initializes the session, calls runEmbeddedAttempt, which creates a SessionManager and calls subscribeEmbeddedPiSession in src/agents/pi-embedded-subscribe.ts, this is an event subscriber/bridge that reacts to events emitted by the loop.

# LOOP

The loop has three layers:

Layer 1: Resilience loop — runEmbeddedPiAgent() in src/agents/pi-embedded-runner/run.ts

while (true) retry loop. Not the reasoning loop — this handles recovery:
- Auth profile rotation: cycles through API key profiles on auth/rate-limit failures
- Context overflow recovery: triggers auto-compaction or tool result truncation, then retries
- Thinking level fallback: if the model rejects a thinking level, downgrades and retries
- Model failover: throws FailoverError so the caller (runWithModelFallback) can try a different model

Each iteration calls runEmbeddedAttempt(). If the attempt returns a recoverable error, continue. Otherwise return or throw.

Layer 2: Single attempt — runEmbeddedAttempt() in src/agents/pi-embedded-runner/run/attempt.ts

Sets up everything for one agent run:
1. Resolve workspace, sandbox, skills, bootstrap files
2. Create tools (createOpenClawCodingTools)
3. Build system prompt (buildEmbeddedSystemPrompt)
4. Open SessionManager (session transcript on disk)
5. createAgentSession() from @mariozechner/pi-coding-agent — returns a session object with an agent that has prompt(), abort(), steer(), messages, isStreaming
6. Sanitize/limit history, inject images
7. Subscribe to session events via subscribeEmbeddedPiSession() (Layer 3)
8. activeSession.prompt(effectivePrompt) — this kicks off the pi-agent-core internal loop
9. Wait for completion + compaction retry
10. Capture messages snapshot, run hooks, return result

The prompt() call is the boundary. Everything before it is setup. prompt() blocks until the LLM finishes (including all tool call rounds). Everything after is teardown.

Layer 3: Event bridge — subscribeEmbeddedPiSession() in src/agents/pi-embedded-subscribe.ts

Passive observer. Does NOT drive the loop — listens to it. session.subscribe() registers a callback that receives events from pi-agent-core as the loop runs.

Events emitted by pi-agent-core:

Event: agent_start
When: Loop begins
Handler: Emit lifecycle event
────────────────────────────────────────
Event: message_start
When: New assistant message begins
Handler: Reset streaming state
────────────────────────────────────────
Event: message_update
When: Text delta arrives (streaming)
Handler: Buffer deltas, emit partial replies, stream reasoning, feed block chunker
────────────────────────────────────────
Event: message_end
When: Assistant message complete
Handler: Finalize text, emit block replies, record usage, dedupe messaging tool sends
────────────────────────────────────────
Event: tool_execution_start
When: Tool call begins
Handler: Flush block buffer, emit tool summary, track pending messaging sends
────────────────────────────────────────
Event: tool_execution_update
When: Tool streams partial output
Handler: Emit tool progress events
────────────────────────────────────────
Event: tool_execution_end
When: Tool call completes
Handler: Commit/discard messaging texts, emit tool result, run after_tool_call hooks
────────────────────────────────────────
Event: auto_compaction_start
When: Context too large, compacting
Handler: Mark compaction in-flight
────────────────────────────────────────
Event: auto_compaction_end
When: Compaction finished
Handler: Resolve compaction wait, allow prompt to complete
────────────────────────────────────────
Event: agent_end
When: Loop finishes
Handler: Flush remaining buffers, emit lifecycle end, resolve compaction promises

The handler files:
- pi-embedded-subscribe.handlers.ts — event dispatcher (switch on evt.type)
- pi-embedded-subscribe.handlers.messages.ts — message_start/update/end
- pi-embedded-subscribe.handlers.tools.ts — tool_execution_start/update/end
- pi-embedded-subscribe.handlers.lifecycle.ts — agent_start/end, compaction_start/end
- pi-embedded-subscribe.handlers.compaction.ts — auto_compaction_start/end

The actual reasoning loop. session.prompt(text) calls Agent._runLoop() which calls agentLoop() which calls runLoop(). It's a double-nested while loop:

runLoop(context, messages, config, signal, stream)

Outer loop (follow-ups):
while (true):
  Inner loop (tool calls + steering):
    while (hasMoreToolCalls || pendingMessages.length > 0):
      1. Inject any pending steering/follow-up messages into context
      2. streamAssistantResponse() → call LLM, stream events
         - transformContext() → prune/modify AgentMessage[]
         - convertToLlm() → AgentMessage[] to Message[]
         - streamFn(model, context, opts) → SSE stream from provider
         - Emits: message_start, message_update (text_delta, text_end, etc.), message_end
      3. If error/aborted → emit agent_end, return
      4. Extract toolCall blocks from assistant response
      5. If tool calls exist:
         - executeToolCalls() — sequential, one at a time:
           a. emit tool_execution_start
           b. tool.execute(id, args, signal, onUpdate)
           c. emit tool_execution_end
           d. After EACH tool: poll getSteeringMessages()
            - If steering arrived → skip remaining tools ("Skipped due to queued msg.")
         - Append all tool results to context
      6. If no tool calls → hasMoreToolCalls = false
      7. Poll getSteeringMessages() again

  // Inner loop done (no more tool calls, no steering)
  Check getFollowUpMessages()
  If follow-ups exist → set as pendingMessages, continue outer loop
  Otherwise → break

emit agent_end

Cool concepts:
- transformContext is a pre-hook, used for context pruning/compaction 
- getSteeringMessages checks for queued messages by user, runs after every tool call 

The Agent class which wraps prompt(), _runLoop(), agentLoop(), runLoop(), also maintains state (messages, isStreaming, pendingToolCalls), manages the AbortController, and fans out events to subscribers via emit(). The subscribedEmbeddedPiSession is one of those subscribers.




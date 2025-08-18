# Interpreter

I've been wondering how to build a new language. 

1) Lexer: Converts single characters into tokens
2) Parser: Creates a tree following language-specific grammar rules. 
3) Static analysis: <Unclear what this does>

Compile:

```bash 
javac -d ./lox/out $(find ./lox/src -name "*.java")
```

Run:
```bash
java -cp ./lox/out com.craftinginterpreters.lox.Lox <file[optional]>
```

notes:
- Good practice to separate the code that generates an error and the code that reports it

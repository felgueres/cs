# Interpreter

I've been wondering how to build a new language. 

1) Lexer: Converts characters into tokens


2) Parser: Creates a tree following grammar rules. 
- Formal grammars have atomic pieces called alphabet (tokens)
- Then it defined a set of string or expressions that are "in the grammar", these are usually infinite
- Instead of writing the infinite strings which would be impossible, you define a finite set of rules
- Using the rules you can generate strings that are in the grammar! Rules are called productions because they produce strings.
- Each production has a head (name) and a body which describes what it generates
- John Backus came up with the notation - Backus-Naur form (BNF)
- Terminal: letter from the grammar's alphabet, eg. tokens from the scanner `if` or `1234`
- Nonterminal: referece to another rule in the grammar
- You basically expand every nonterminal in a string to a Terminal
- Because rules can refer to itself, it allows you do infinite number of strings with a finite grammar

Notation for Lox:

```
expression -> literal | unary | binary | grouping;
literal -> NUMBER | STRING | "true" | "false" | "nil";
grouping -> "(" expresssion ")";
unary -> ("-" | "!") expression;
binary -> expression operator expression;
operator -> "==" | "!=" | "<" | "<=" | ">=" | "+" | "-" | "*" | "/"; 
```

We capitalize terminals whose text represenation may vary, ie. NUMBER and STRING

NEXT: Implementing Syntax Trees (page. 58)

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

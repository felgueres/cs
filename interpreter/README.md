===========
Interpreter
===========

I was curious about how python works and quickly got into a language design rabbit hole. 
Working through the book Crafting Interpreters.

Goals
=====
* Build a scanner, parser, evaluator in Java, redo in C

Usage
=====

```shell 
// compile folder
$ javac -d ./lox/out $(find ./lox/src -name "*.java")

// Generate Expr.java
$ java -cp lox/out com.craftinginterpreters.tool.GenerateAst lox/src/com/craftinginterpreters/lox

// compile generated Expr 
$ javac -d ./lox/out $(find ./lox/src -name "*.java")

// Run interpreter
java -cp ./lox/out com.craftinginterpreters.lox.Lox <file[optional]>
```

Concepts 
========

1) Lexer or Scanner: Converts characters into tokens

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

Notation for the Lox language:

```ebnf
expression -> literal | unary | binary | grouping;
literal -> NUMBER | STRING | "true" | "false" | "nil";
grouping -> "(" expresssion ")";
unary -> ("-" | "!") expression;
binary -> expression operator expression;
operator -> "==" | "!=" | "<" | "<=" | ">=" | "+" | "-" | "*" | "/"; 
```
We capitalize terminals whose text represenation may vary, ie. NUMBER and STRING

- Grammar may allow more than one way of parsing an expression. The key here is to have precedence and associativity rules. Precedence in operators like (*) goes before (+). associativity determines if you have two same operators, which one is evaluated first. Substraction is left-associative, eg. 5 - 3 -1 is (5-3) - 1, and assignment is right-associative, eg. a = b = c is a = (b=c). Fix this by stratifying the grammar
- There are many parsing algorithms, recursive descent is a simple yet production ready (JavaScript VM in Chrome uses it)

Recursive descent. 
- Top-down parser. Starts from the outermost grammar rule, and down to subexpr towards the leaves
- Literal translation of grammar rules into imperative code, every rule becomes a function

Notes
=====
- Good practice to separate the code that generates an error and the code that reports it

OOP: classes with methods
functional: types and functions are distinct. to impl operation for different types you define a single function and use pattern matching for each type all in one place. conversely adding a new type means updating every function 
visitor pattern lets you do approx functional style in oop 

overloading: when two funcs have same name but differ in the parameter list. the runtime decides which one to call based on the args used


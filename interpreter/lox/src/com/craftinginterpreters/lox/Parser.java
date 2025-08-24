package com.craftinginterpreters.lox;
import java.util.List;
import static com.craftinginterpreters.lox.TokenType.*;

// Resume from page 82

class Parser {
    private final List<Token> tokens;
    private int current = 0; // points to the next token to be parsed
    Parser(List<Token> tokens){
        this.tokens = tokens;
    }

    private Expr expression(){
        return equality();
    }

    private Expr equality(){
        // equality → comparison ( ( "!=" | "==" ) comparison )* ;
        // ( ... )* means a loop
        Expr expr = comparison();
        while (match(BANG_EQUAL, EQUAL_EQUAL)){
            Token operator = previous();
            Expr right = comparison();
            expr = new Expr.Binary(expr, operator, right);
        }
        return expr;
    }
   private boolean match(TokenType... types){
       for (TokenType type: types){
           if (check(type)){
               advance();
               return true;
           }
       }
       return false;
   } 
   private boolean check(TokenType type){
       if (isAtEnd()) return false;
       return peek().type == type;
   }
   private Token advance(){
       // returns a consumed Token
       if (!isAtEnd()) current++; // advances the index pointing to the next token to be parsed
       return previous();
   }

   private boolean isAtEnd(){
       return peek().type == EOF;
   }

   private Token peek(){
       return tokens.get(current);
   }

   private Token previous(){
       return tokens.get(current - 1);
   }

}

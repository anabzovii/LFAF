# Parser & Building an Abstract Syntax Tree
## Course: Formal Languages & Finite Automata
## Author: Bzovii Ana FAF-213

## Theory
A parser is a part of a compiler that breaks down data into smaller pieces after doing lexical analysis. It creates a parse tree after processing a string of tokens. The abstract syntax of source code is shown in a tree-like representation known as an Abstract Syntax Tree. A source code concept is represented by each tree node. Abstract Syntax Trees are essential to compilers because they act as data structures to represent the structure of programs. Usually, a compiler's syntax analysis phase produces an Abstract Syntax Tree. It frequently serves as an interim program representation during various compiler stages, having a substantial impact on the compiler's output.
## Objectives:
- Get familiar with parsing, what it is and how it can be programmed.

- Get familiar with the concept of AST.

- In addition to what has been done in the 3rd lab work do the following:
    - In case you didn't have a type that denotes the possible types of tokens you need to:
      - Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
      - Please use regular expressions to identify the type of the token.
    - Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    - Implement a simple parser program that could extract the syntactic information from the input text.

## Implementation description
### parse
The outcome of this procedure, which evaluates an arithmetic expression, is returned as a float. To calculate the outcome, it first calls the expression() method. It then determines whether the following token is an assignment operator ('='). If so, it advances to the subsequent token and determines if the input has ended. It returns the outcome if it is. It raises an exception that indicates an incomplete expression if these requirements are not met.
```java
    def parse_function(self):
        result = self.expr_function()
        if self.pos < len(self.tokens):
            raise Exception(f"Invalid syntax: {self.tokens[self.pos][0]}")
        return result
```

### expression
Using addition and subtraction operations, this approach evaluates an arithmetic statement. To obtain the initial value, the term() method is first used. It then enters a loop where each token in the expression is checked. If the token is a plus sign, the position is increased, the value is increased, and the loop is continued. If the token is a minus sign, the position is increased, the value is reduced by the subsequent term, and the loop is then continued. It returns the current value if the token is neither a plus nor a negative sign, or if there are no more tokens.
```java
    def expr_function(self):
        result = self.term_function()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in ("Addition", "Subtraction"):
            if self.tokens[self.pos][1] == "Addition":
                self.pos += 1
                result += self.term_function()
            else:
                self.pos += 1
                result -= self.term_function()
        return result
```
### term
With this approach, a portion of the mathematical phrase that calls for multiplication and division operations is evaluated. To obtain the initial value, the factor() method is first called. It then enters a loop where each token in the expression is checked. If the token is a multiplication symbol, the position is increased, the current value is multiplied by the subsequent factor, and the loop is then continued. If the token is a division symbol, the position is increased, the current value is divided by the subsequent factor, and the loop is then continued. It yields the current value if the token is neither a multiplication nor a division sign, or if there are no more tokens.
```java
    def term_function(self):
        result = self.factor_function()
        while self.pos < len(self.tokens) and self.tokens[self.pos][1] in ("Multiply", "Divide"):
            if self.tokens[self.pos][1] == "Multiply":
                self.pos += 1
                result *= self.factor_function()
            else:
                self.pos += 1
                result /= self.factor_function()
        return result
```
### factor
The expression is processed using this method's individual numbers. It throws an error if there are no more tokens. The current token is converted to a float and returned if it is a number. It throws an error if the token is not a number.
```java
    def factor_function(self):
        if self.tokens[self.pos][1] == "Digit":
            result = float(self.tokens[self.pos][0])
            self.pos += 1
            return result
        elif self.tokens[self.pos][1] == "LeftP":
            self.pos += 1
            result = self.expr_function()
            if self.tokens[self.pos][1] != "RightP":
                raise Exception(f"Missing closing parenthesis")
            self.pos += 1
            return result
        else:
            raise Exception(f"Invalid syntax: {self.tokens[self.pos][0]}")
```

## Results

---------------------------------

`THe parser is  40.0
THe token is :  [('5', 'Digit'), ('*', 'Multiply'), ('2', 'Digit'), ('*', 'Multiply'), ('(', 'LeftP'), ('10', 'Digit'), ('-', 'Subtraction'), ('2', 'Digit'), (')', 'RightP'), ('/', 'Divide'), ('2', 'Digit')]`

---------------------------------

## Conclusions
To sum up, working at the lab has been a rewarding experience. I've got the chance to delve into the complexities of building a parser in Java, which is an essential step in the compilation and interpretation of code. I've learned how to simplify complicated equations into smaller, more manageable units and how to evaluate these units in accordance with arithmetic laws. Additionally, I now have a better understanding of how to deal with various data kinds, such integers and floating-point numbers, as well as how to handle unexpected input. My appreciation for the intricacy and elegance of compiler design has definitely grown as a result of this work. I'm excited to use these ideas in my future projects.

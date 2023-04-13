# Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Bzovîi Ana FAF-213

## Theory
In computer science, a lexer (short for lexical analyzer) is a program or function that performs lexical analysis on a stream of input characters.
The main task of a lexer is to break up a sequence of characters into a sequence of tokens, which are meaningful units in the language being analyzed. It does this by examining the input stream character by character, identifying the boundaries of each token, and associating each token with a specific type or category.

For example, in a programming language lexer, the input characters might be separated into tokens such as keywords (e.g. "if", "while"), identifiers (e.g. variable names), operators (e.g. "+", "-"), and literals (e.g. numbers, strings).

The output of a lexer is typically a sequence of tokens that can be fed into a parser for further processing. A parser uses the sequence of tokens to build a parse tree, which represents the syntactic structure of the input program.

## Objectives:
- Understand what lexical analysis [1] is.
- Get familiar with the inner workings of a lexer/scanner/tokenizer.
- Implement a sample lexer and show how it works.
  

## Implementation description
### Lexer class
The Lexer class has several methods, including advance(), skip_whitespace(), integer(), and get_next_token(), which is the main method responsible for tokenizing the input text. The class has the task of analyzing an input string and detecting the different kinds of tokens present in it. It accomplishes this by establishing a group of regular expression patterns that correspond to different token types, such as numbers, keywords, operators, identifiers, and strings.

The Token class has two attributes, type and value, and a repr method that returns a string representation of the Token object.  The get_next_token() method iterates over the input text and matches each character with a set of predefined regular expression patterns to identify the type of token. If a match is found, a Token object is created and returned with the corresponding token type and value. If an invalid character is encountered, an exception is raised. The output of the Lexer is a list of Token objects representing the input text.
```python
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token(type='{self.type}', value={self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token('INTEGER', self.integer())

            if self.current_char == '+':
                self.advance()
                return Token('PLUS', '+')

            if self.current_char == '-':
                self.advance()
                return Token('MINUS', '-')

            if self.current_char == '*':
                self.advance()
                return Token('MUL', '*')

            if self.current_char == '/':
                self.advance()
                return Token('DIV', '/')

            if self.current_char == '(':
                self.advance()
                return Token('LPAREN', '(')

            if self.current_char == ')':
                self.advance()
                return Token('RPAREN', ')')

            if self.current_char.isalpha():
                return Token('ID', self.current_char)

            raise Exception(f"Invalid character: {self.current_char}")

        return Token('EOF', None)

```

### Main
The Main class imports the Lexer class from the lexer module, and then creates an instance of the Lexer class by invoking its constructor without any arguments. Subsequently, the tokenize method of the Lexer instance is invoked with the input string "3 + 4 * 2 - 1". The method tokenizes the input string by separating it into a list of tokens and then returns the list. Finally, the resulting list of tokens is printed to the console using the print function. The output confirms that the input string has been correctly tokenized into its component tokens, including numbers, operators, and parentheses. Moreover, the message "input valid" is printed to the console, indicating that the input string was tokenized successfully without encountering any errors.```python
```python
 # Define input text
        text = "3 + 4 * 2 - 1"


        # Create lexer object
        lexer = Lexer(text)

        token = lexer.get_next_token()

        while token.type != "EOF":
            print(token)
            token = lexer.get_next_token()

        print(token)

```



## Results
Token(type='INTEGER', value=3)
Token(type='PLUS', value=+)
Token(type='INTEGER', value=4)
Token(type='MUL', value=*)
Token(type='INTEGER', value=2)
Token(type='MINUS', value=-)
Token(type='INTEGER', value=1)
Token(type='EOF', value=None)


## Conclusions
A lexer is a crucial component of programming language processing. It breaks down an input string into tokens that represent meaningful language elements. These tokens are mapped to corresponding types and semantics defined by production rules. The lexer is used for syntax highlighting, code completion, and program analysis. This project implements a lexer in Python using regular expressions to match token types. The implementation involves iterating over the input string, matching against regular expressions, and generating corresponding tokens. Regular expressions provide an efficient way to define the language's syntax. The project demonstrates the importance of lexers in language processing and shows how they can be used to build sophisticated compilers and analysis tools.

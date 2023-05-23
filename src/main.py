import Lexer
import parser

lexer = Lexer.Lexer("5 * 2 * (10 - 2) / 2")
tokens = lexer.tokenize()

parser = parser.Parser(tokens)
parser_ans = parser.parse_function()

print("THe parser is ", parser_ans)
print("THe token is : ", tokens)
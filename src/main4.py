from grammar import Grammar
from ChomskyConv import Converter_CNF
from finite_automaton import FiniteAutomaton
from Lexer import Lexer, Token
import unittest
from UnitTester import UnitTester


def main():

    VN = {'S', 'A', 'B', 'C'}
    VI = {'a', 'b'}
    P = [
        ('S', ('a', 'B')),
        ('S', ('A', 'C')),
        ('A', ('a',)),
        ('A', ('A', 'S', 'C')),
        ('A', ('B', 'C', 'a')),
        ('B', ('C',)),
        ('B', ('b', 'S')),
        ('B', ('b',)),
        ('C', ('B', 'A')),
        ('C', ()),
    ]

    S = 'S'
    grammar = (VN, VI, P, S)

    # Convert the grammar to Chomsky normal form
    cnf_converter = Converter_CNF(grammar)
    cnf_grammar = cnf_converter.convert_to_cnf()

    # Print the resulting 
    print('Grammar:')
    print(grammar)
    print('Grammar in Chomsky Normal Form:')
    print(cnf_grammar)


if __name__ == '__main__':
    main()
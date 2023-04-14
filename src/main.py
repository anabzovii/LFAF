import random
from grammar import Grammar
from finite_automaton import FiniteAutomaton
class Main:
    def run(self):
        grammar = Grammar()
        print('Generating 5 valid strings from the language expressed by the grammar:')
        strings = grammar.generate_strings(5, 10)
        for string in strings:
            print(string)

        fa = FiniteAutomaton(
            states={'q0', 'q1', 'q2'},
            alphabet={'a', 'b', 'c', 'd', 'e'},
            transitions={
                ('q0', 'a'): 'q1',
                ('q1', 'd'): 'q2',
                ('q1', 'b'): 'q3',
                ('q3', 'c'): 'q0',
                ('q2', 'e'): 'q2',
                ('q2', 'a'): 'q2',
                ('q3', 'a'): 'q2'
            },
            start_state='q0',
            accept_states={'q2'}
        )
        print('Generated Finite Automaton:')
        print(fa)
        print('Checking if some example strings are accepted by the finite automaton:')
        input_strings = ['adee', 'ad', 'adea', 'acbd', 'adde']
        for input_string in input_strings:
            if fa.accepts(input_string):
                print(f'The input string "{input_string}" is accepted by the automaton.')
            else:
                print(f'The input string "{input_string}" is not accepted by the automaton.')


if __name__ == '__main__':
    main = Main()
    main.run()

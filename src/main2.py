from grammar import Grammar
from finite_automaton import FiniteAutomaton


class Main:
    def run(self):
        grammar = Grammar()
        grammar_type = grammar.classify()
        print("***************************")
        print(f"The grammar is of the type {grammar_type}.")

        # print('Generating 5 valid strings from the language expressed by the grammar:')
        # strings = grammar.generate_strings(5, 10)
        # for string in strings:
        #     print(string)

        fa = FiniteAutomaton(
            states={'q0', 'q1', 'q2', 'q3', 'q4'},
            alphabet={'a', 'b'},
            transitions={('q0', 'a'): 'q1',
                         ('q1', 'b'): 'q2',
                         ('q2', 'b'): 'q0',
                         ('q3', 'a'): 'q4',
                         ('q4', 'a'): 'q0',
                         ('q2', 'a'): 'q3',
                         ('q1', 'b'): 'q1'},
            start_state='q0',
            accept_states={'q3'}
        )

        regular_grammar = fa.to_regular_grammar()
        print("***************************")
        print("FA to regular grammar")
        print(regular_grammar)

        deterministic = fa.is_deterministic()
        if deterministic:
            print("***************************")
            print("The FA is deterministic")
        else:
            print("***************************")
            print("The FA is non-deterministic")

        # Convert the NDFA to a DFA
        dfa = fa.convert_to_dfa()
        print("***************************")
        print("______DFA______")
        print(dfa)
        print("***************************")
        fa.render()
        print('Generated Finite Automaton:')
        print(fa)


if __name__ == '__main__':
    main = Main()
    main.run()

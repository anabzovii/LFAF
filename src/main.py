import random

class Grammar:
    def __init__(self):
        self.VN = {'S', 'D', 'E', 'J'}
        self.VT = {'a', 'b', 'c', 'd', 'e'}
        self.P = {
            'S': ['aD'],
            'D': ['dE', 'bJ', 'aE'],
            'J': ['cS'],
            'E': ['e', 'aE']
        }


    def generate_string(self, start_symbol, max_length):
        if max_length == 0:
            return ''
        production = random.choice(self.P[start_symbol])
        string = ''
        for symbol in production:
            if symbol in self.VN:
                string += self.generate_string(symbol, max_length - 1)
            else:
                string += symbol
        return string

    def generate_strings(self, count, max_length):
        strings = []
        for i in range(count):
            strings.append(self.generate_string('S', max_length))
        return strings


class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            if (current_state, symbol) not in self.transitions:
                return False
            current_state = self.transitions[(current_state, symbol)]
        if current_state not in self.accept_states:
            return False
        return True

    def __str__(self):
        s = "Finite Automaton:\n"
        s += "States: " + str(self.states) + "\n"
        s += "Alphabet: " + str(self.alphabet) + "\n"
        s += "Transitions:\n"
        for transition in self.transitions:
            s += str(transition[0]) + " --" + str(transition[1]) + "--> " + str(self.transitions[transition]) + "\n"
        s += "Start state: " + str(self.start_state) + "\n"
        s += "Accept states: " + str(self.accept_states) + "\n"
        return s


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

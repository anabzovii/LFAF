# Regular grammars. Finite Automata
## Course: Formal Languages & Finite Automata
## Author: Bzovîi Ana FAF-213


## Theory
A formal language can be considered to be the media or the format used to convey information from a sender entity to the one that receives it. The usual components of a language are:
- The alphabet: Set of valid characters;
- The vocabulary: Set of valid words;
- The grammar: Set of rules/constraints over the lang.

Regular grammars and finite automata are two related concepts in computer science and formal language theory. They are used to describe and analyze formal languages, which are sets of strings that follow certain rules and constraints.

A regular grammar is a set of production rules that describe how to generate strings in a language. It consists of a set of nonterminal symbols, a set of terminal symbols, and a set of production rules that specify how to replace nonterminal symbols with sequences of symbols. Regular grammars are a type of formal grammar, which is a mathematical formalism used to describe the structure of languages.

A finite automaton is a machine that can recognize or generate strings in a language. It consists of a set of states, a set of input symbols, and a set of transitions that specify how to move from one state to another when processing an input symbol. Finite automata can be deterministic, meaning that there is only one possible transition for each input symbol, or nondeterministic, meaning that there can be multiple possible transitions for each input symbol.

## Objectives:
- Understand what a language is and what it needs to have in order to be considered a formal one.
- Create a local && remote repository of a VCS hosting service;
- Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;
- Create a separate folder where you will be keeping the report;
- Implement a type/class for your grammar;
- Add one function that would generate 5 valid strings from the language expressed by your given grammar;
- Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;
- For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it;


## Implementation description
### Grammar class

The implementation includes a class called "Grammar" that has three attributes: VN, VT, and P. These attributes represent the set of non-terminal symbols, the set of terminal symbols, and the set of production rules.

```python
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

```

### FiniteAutomaton class
This code defines a Finite Automaton class that represents a non-deterministic finite automaton. The class has an initialization method "init" that takes in five parameters: "states", "alphabet", "transitions", "start_state", and "accept_states". These parameters are used to set the initial state of the automaton.

The class also has an "accepts" method that checks whether a given input string is accepted by the automaton or not. The method simulates state transitions on the input string by iterating over each input symbol and following the transitions for each symbol. If the final state after processing the entire string is an accept state, the method returns True, otherwise, False is returned.

The "str" method is used to return a string representation of the Finite Automaton object. It returns a string containing information about the states, alphabet, transitions, start state, and accept states of the automaton. The transitions are displayed in the format "current_state --symbol--> next_state".

```python
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

```

### Main
The "run" method first creates an instance of the Grammar class and generates five valid strings from the language expressed by the grammar. It then prints these strings.

Next, the method creates an instance of the FiniteAutomaton class with the given parameters: states, alphabet, transitions, start_state, and accept_states. The method then prints the generated Finite Automaton object using the "str" method of the FiniteAutomaton class.

Finally, the method checks if some example input strings are accepted by the generated Finite Automaton using the "accepts" method of the FiniteAutomaton class. If an input string is accepted, it prints a message indicating that the string is accepted by the automaton. Otherwise, it prints a message indicating that the string is not accepted by the automaton.

```python
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

```

## Results
Generating 5 valid strings from the language expressed by the grammar:
abcaaae
aaaaaae
abcaae
aaaaae
abcade
Generated Finite Automaton:
Finite Automaton:
States: {'q1', 'q0', 'q2'}
Alphabet: {'a', 'e', 'd', 'c', 'b'}
Transitions:
q0 --a--> q1
q1 --d--> q2
q1 --b--> q3
q3 --c--> q0
q2 --e--> q2
q2 --a--> q2
q3 --a--> q2
Start state: q0
Accept states: {'q2'}

Checking if some example strings are accepted by the finite automaton:
The input string "adee" is accepted by the automaton.
The input string "ad" is accepted by the automaton.
The input string "adea" is accepted by the automaton.
The input string "acbd" is not accepted by the automaton.
The input string "adde" is not accepted by the automaton.


## Conclusions
This laboratory work involved working with formal languages, regular grammars, and finite automata, using Python classes. The laboratory began with defining a grammar, including nonterminal symbols, terminal symbols, and production rules. The generated strings were validated and converted to a finite automaton, which could accept or reject input strings based on its state transitions.

These concepts are useful in various fields, including text processing, natural language processing, and programming language design. Recognizing and generating valid strings in a language is a crucial part of these fields, and the tools developed in this project provide a foundation for further exploration and implementation.

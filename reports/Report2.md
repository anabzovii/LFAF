# Determinism in Finite Automata. Conversion from NDFA to DFA. Chomsky Hierarchy
## Course: Formal Languages & Finite Automata
## Author: Bzovîi Ana FAF-213

## Theory
A finite automaton is a mechanism used to represent processes of different kinds. It can be compared to a state machine as they both have similar structures and purpose as well. The word finite signifies the fact that an automaton comes with a starting and a set of final states. In other words, for process modeled by an automaton has a beginning and an ending.

Based on the structure of an automaton, there are cases in which with one transition multiple states can be reached which causes non determinism to appear. In general, when talking about systems theory the word determinism characterizes how predictable a system is. If there are random variables involved, the system becomes stochastic or non deterministic.

That being said, the automata can be classified as non-/deterministic, and there is in fact a possibility to reach determinism by following algorithms which modify the structure of the automaton.
    
The Chomsky Hierarchy is a system for classifying formal languages and grammars into four types - Type-0 to Type-3. Type-0 grammars are the most powerful, capable of generating all possible formal languages, while Type-3 grammars are the simplest and generate regular languages. The hierarchy is used to analyze the computational complexity and expressive power of different types of languages and grammars, and is commonly used in computer science and linguistics.

## Objectives:
- Understand what an automaton is and what it can be used for.

- Continuing the work in the same repository and the same project, the following need to be added: a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.

    b. For this you can use the variant from the previous lab.

- According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.

    b. Determine whether your FA is deterministic or non-deterministic.

    c. Implement some functionality that would convert an NDFA to a DFA.

    d. Represent the finite automaton graphically (Optional, and can be considered as a bonus point):

- You can use external libraries, tools or APIs to generate the figures/diagrams.

- Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.
  

## Implementation description
### Chomsky Hierarchy
This code defines a method named 'classify' that takes no input arguments and returns a string representing the type of Chomsky hierarchy that a grammar belongs to. The method uses a series of conditional statements to check whether the grammar is of Type-0 to Type-3 and returns the corresponding string.

The code first checks whether the grammar is Type-0 by comparing the length of the right-hand side of all productions to the length of the left-hand side. If the grammar is not Type-0, the code proceeds to check whether it is Type-1 by comparing the lengths of the right-hand side of all productions to the length of the left-hand side, while also checking that the length of the production is greater than zero.

The code then checks whether the grammar is Type-2 by ensuring that all productions are of the form A -> B, where A is a single non-terminal symbol and B is a string of terminals and non-terminals. Finally, the code checks whether the grammar is Type-3 by ensuring that all productions are of the form A -> aB or A -> e, where A and B are non-terminal symbols and a is a terminal symbol.

If none of the above conditions hold, the code returns "Not a valid Chomsky type".

```python

    def classify(self):
        # Check if the grammar is type-0
        if not all(len(production) <= len(symbol_string) for symbol_string in self.P.values() for production in
                   symbol_string):
            return "Type-0 (Unrestricted)"

        # Check if the grammar is type-1
        if not all(len(production) < len(symbol_string) for symbol_string in self.P.values() for production in
                   symbol_string if len(production) > 0):
            return "Type-1 (Context-Sensitive)"

        # Check if the grammar is type-2
        if all(len(production) == 1 and production.isupper() for symbol_string in self.P.values() for production in
               symbol_string):
            return "Type-2 (Context-Free)"

        # Check if the grammar is type-3
        if all((len(production) == 2 and production[0] in self.VN and production[1] in self.VT) or production == 'e' for
               symbol_string in self.P.values() for production in symbol_string):
            return "Type-3 (Regular)"

        # If none of the above conditions hold, then the grammar is not a valid Chomsky type
        return "Not a valid Chomsky type"
```

**Result:**
```
The grammar is of the type Type-0 (Unrestricted).
```
### FA to Regular grammar
This code provides a useful tool for converting a finite automaton to a regular grammar, which can be used for further analysis and manipulation of the language that the automaton recognizes.

The code first initializes an empty list called 'rules', which will contain the production rules of the grammar. It then iterates over each transition in the finite automaton, and for each transition, it checks whether the next state is an accept state.

If the next state is an accept state, the code creates a rule where the left-hand side is the current state, and the right-hand side is the symbol associated with the transition. Otherwise, the code creates a new non-terminal symbol and a rule that goes from the current state to this new non-terminal symbol and the symbol associated with the transition.

The method then creates a start symbol that corresponds to the start state of the finite automaton and adds it to the list of rules. Finally, the code joins the list of rules using newline characters and returns them as a string.

```python
    def to_regular_grammar(self):
        rules = []
        # Create a rule for each transition
        for (state, symbol), next_state in self.transitions.items():
            # If the transition goes to an accept state, add it to the RHS of the rule
            if next_state in self.accept_states:
                rhs = symbol
            # Otherwise, add a new nonterminal symbol and create a rule to that symbol and the symbol on the RHS
            else:
                rhs = f"<{next_state}> {symbol}"
                rules.append(f"<{next_state}> {'|'.join([symbol + f'<{s}>' for s in self.states if (next_state, s) in self.transitions.keys()])}")
            # Add the new rule to the list of rules
            rules.append(f"<{state}> {rhs}")
        # Create the start symbol and add it to the rules
        rules.append(f"S <{self.start_state}>")
        # Join the list of rules and return them as a string
        return "\n".join(rules)
```
**Result:**
```
FA to regular grammar
<q1> 
<q0> <q1> a
<q1> 
<q1> <q1> b
<q0> 
<q2> <q0> b
<q4> 
<q3> <q4> a
<q0> 
<q4> <q0> a
<q2> a
S <q0>
```

### Deterministic or non-deterministic
The 'is_deterministic' method checks if a finite automaton is deterministic. It uses a breadth-first search algorithm to visit each state and checks if there is only one possible transition for each input symbol. If a state is visited twice or there is more than one possible transition, the method returns False. Otherwise, it returns True.

```python
    def is_deterministic(self):
        # implementation of is_deterministic method
        visited_states = set()
        queue = [self.start_state]
        while queue:
            curr_state = queue.pop(0)
            if curr_state in visited_states:
                return False
            visited_states.add(curr_state)
            for symbol in self.alphabet:
                next_states = set()
                for state, trans_symbol in self.transitions.keys():
                    if state == curr_state and trans_symbol == symbol:
                        next_states.add(self.transitions[(state, trans_symbol)])
                if len(next_states) != 1:
                    return False
                queue.extend(next_states)
        return True
```
**Result:**
```
The FA is non-deterministic
```

### NDFA to DFA
The code defines a function convert_to_dfa that takes an NDFA and converts it into a Deterministic Finite Automaton (DFA). The function uses the powerset construction algorithm to compute the set of states and the transition function of the DFA.

The function initializes empty sets and queues to store the computed properties of the DFA. It then processes each state of the DFA by checking for its accept state status and computing the transitions for each symbol in the alphabet. Finally, it returns a new DFA object with the computed properties.

The powerset construction algorithm is a technique used to convert a non-deterministic finite automaton (NFA) to a deterministic finite automaton (DFA). The basic idea is to represent the states of the DFA as sets of states of the NFA, where each set represents a possible state of the DFA. The algorithm works by starting with the set containing the start state of the NFA, and computing the set of states that can be reached by consuming each symbol in the input alphabet. This process is repeated for each set of states until all possible states of the DFA have been computed. At the end, the resulting DFA has one state for each subset of states of the NFA, and transitions between those states are defined by the transitions of the NFA. The accept states of the DFA are those sets of states that contain at least one accept state of the NFA.

```python
    def convert_to_dfa(self):
        """
        Converts an NDFA to a DFA
        """
        # Set of states in the DFA
        dfa_states = set()
        # Dictionary representing the transition function of the DFA
        dfa_transitions = {}
        # Start state of the DFA
        dfa_start_state = frozenset([self.start_state])
        # Set of accept states in the DFA
        dfa_accept_states = set()
        # Queue for storing states to be processed
        queue = [dfa_start_state]

        # Loop through states in the queue
        while queue:
            # Get the next state from the queue
            state = queue.pop(0)
            # Add the state to the set of DFA states
            dfa_states.add(state)
            # Check if the state contains an accept state from the NDFA
            if any(s in self.accept_states for s in state):
                dfa_accept_states.add(state)
            # Loop through each symbol in the alphabet
            for symbol in self.alphabet:
                # Get the set of states reachable from the current state with the current symbol
                next_state = set()
                for s in state:
                    if (s, symbol) in self.transitions:
                        next_state.update(self.transitions[(s, symbol)])
                # If the set of states is not empty
                if next_state:
                    # Convert the set of states to a single state name
                    next_state_name = frozenset(next_state)
                    # Add the transition to the DFA transition function
                    dfa_transitions[(state, symbol)] = next_state_name
                    # If the next state has not been processed, add it to the queue
                    if next_state_name not in dfa_states:
                        queue.append(next_state_name)

        # Create a new DFA object with the computed properties
        dfa = FiniteAutomaton(states=dfa_states, alphabet=self.alphabet,
                              transitions=dfa_transitions, start_state=dfa_start_state,
                              accept_states=dfa_accept_states)
        return dfa
```
**Result:**
```
______DFA______
Finite Automaton:
States: {frozenset({'q0'}), frozenset({'q', '1'})}
Alphabet: {'a', 'b'}
Transitions:
frozenset({'q0'}) --a--> frozenset({'q', '1'})
Start state: frozenset({'q0'})
Accept states: set()

***************************
Generated Finite Automaton:
Finite Automaton:
States: {'q2', 'q0', 'q1', 'q3', 'q4'}
Alphabet: {'a', 'b'}
Transitions:
q0 --a--> q1
q1 --b--> q1
q2 --b--> q0
q3 --a--> q4
q4 --a--> q0
q2 --a--> q3
Start state: q0
Accept states: {'q3'}
```

## Conclusions
In this laboratory work I have included the basic concepts of finite automata, determinism, and the Chomsky Hierarchy, and have listed my objectives for the project, which include implementing a function to classify grammars based on the Chomsky Hierarchy and performing various operations on finite automata, such as conversion from NDFA to DFA and graphical representation.

An important part of the report is the implementation, which explains how I have implemented the classify function using conditional statements to check whether a given grammar belongs to Type-0 to Type-3 in the Chomsky Hierarchy. Additionally, I have provided code for converting a finite automaton to a regular grammar using a set of rules and have included code for checking whether the automaton is deterministic or non-deterministic and for converting an NDFA to a DFA. I have also mentioned that you have implemented functionality for graphical representation of the automaton, which uses external libraries, tools, or APIs.

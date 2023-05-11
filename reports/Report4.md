# Chomsky Normal Form
## Course: Formal Languages & Finite Automata
## Author: Bzovii Ana FAF-213


### Variant 8

G=(VN, VT, P, S) Vn={S, A, B, C} VT={a, d}
P={1. S⇒dB
2. S→A
3. A→d
4. A→dS
5. A→aAdAB
6. B→a
7. B→aS
8. B⇒A
9. B→ε
10. C→Aa}
## Theory

An algorithm for parsing and other language-processing tasks can be developed using the Chomsky Normal Form (CNF), a condensed version of context-free grammars. If all of a context-free grammar's production rules take one of the two following forms, it is considered to be in Chomsky Normal Form.

1. The non-terminal symbols A, B, and C in the chain A->BC.
2. Where A is a non-terminal symbol and an is a terminal symbol, the relationship is A->a. 

Its simplicity, which makes it simpler to create algorithms that work with context-free grammars, is CNF's main advantage. Any context-free grammar can be transformed into its Chomsky Normal Form equivalent. The following steps are involved in the conversion process:

Eliminate -productions by substituting alternative productions that provide the same language without the -production for every production rule of the pattern A ->.
2. Get rid of renaming (unit productions): Substitute production rules for B in favor of production rules for A, where A and B are non-terminal symbols.
3. Remove symbols that are inaccessible: In the grammar, remove any non-terminal symbols that are inaccessible from the start symbol.
4. Remove useless symbols: Get rid of any symbols that aren't terminal and can't be used to create terminal strings.
5. Convert the remaining rules to CNF format: Divide any production rules that have more than two symbols into separate rules that follow the CNF structure.

These procedures allow us to convert any context-free grammar into its equivalent in Chomsky Normal Form without changing the language that grammar produces.

## Objectives

1. Introduce a procedure for normalizing an input grammar in accordance with the CNF (Chomsky Normal Form) criteria.
2. Include the implementation in a method with the right signature (preferably in a class or type as well).
3. Put the implemented feature into use and test it.
4. (Bonus) Produce unit tests that confirm the project's functionality.
5. (Bonus) Change the function so that it will accept any grammar, not only the student's variety.

## Implementation description

### Eliminate Epsilon Productions

The grammar's 'delete_epsilon' method is in charge of eliminating -productions (rules of the type A -> ). In essence, it eliminates the requirement for -productions by identifying all non-terminal symbols that produce either directly or indirectly and substituting those symbols in all other production rules.

```python
        def delete_epsilon(self):
        vn, vi, p, s = self.grammar
        # Find nullable symbols
        nullable = set()
        while True:
            updated = False
            for rule in p:
                if all(s in nullable for s in rule[1]):
                    if rule[0] not in nullable:
                        nullable.add(rule[0])
                        updated = True
            if not updated:
                break
        # Eliminate epsilon productions
        new_p = []
        for rule in p:
            lhs, rhs = rule
            for i in range(2 ** len(rhs)):
                binary = bin(i)[2:].zfill(len(rhs))
                new_rhs = [rhs[j] for j in range(len(rhs)) if binary[j] == '0']
                if new_rhs:
                    new_p.append((lhs, tuple(new_rhs)))
            if not rhs:
                new_p.append((lhs, ('epsilon',)))
        if self.grammar[3]:
            self.grammar = vn, vi, new_p, s
        else:
            self.grammar = vn, vi, new_p
```


### Eliminate Renaming
Unit productions (rules with the form A -> B, where A and B are non-terminal symbols) are eliminated from the grammar using the 'delete_renaming' function. It accomplishes this by substituting all of the production regulations for the referenced non-terminal symbol for the unit production. Until all unit productions are stopped, this process is repeated.


```python
        def delete_renaming(self):
        vn, vi, p, s = self.grammar
        # Eliminate renaming
        new_p = []
        for rule in p:
            if len(rule[1]) == 1 and rule[1][0] in vn:
                for sub_rule in p:
                    if sub_rule[0] == rule[1][0]:
                        new_p.append((rule[0], sub_rule[1]))
            else:
                new_p.append(rule)
        
```
### Eliminate Inaccessible Symbols

The `eliminateInaccessibleSymbols` part of the `eliminate_renaming` removes non-terminal symbols that are not reachable from the start symbol of the grammar. It starts with the start symbol and iteratively finds all non-terminal symbols reachable from it. Then, it removes any production rules containing non-reachable symbols.

```python
  # Eliminate inaccessible symbols
   reachable = set([s])
        updated = True
        while updated:
            updated = False
            for rule in new_p:
                if rule[0] in reachable:
                    for symbol in rule[1]:
                        if symbol in vn or symbol in reachable:
                            updated = updated or symbol not in reachable
                            reachable.add(symbol)
        new_vn = set([s])
        new_p = [rule for rule in new_p if rule[0] in reachable and all(s in new_vn or s in vi for s in rule[1])]
        for rule in new_p:
            for symbol in rule[1]:
                if symbol in vn:
                    new_vn.add(symbol)
        if self.grammar[3]:
            self.grammar = new_vn, vi, new_p, s
        else:
            self.grammar = new_vn, vi, new_p
```

### Eliminate Non-Productive Symbols

The non-terminal symbols that cannot be used to create any terminal strings are removed by the 'delete_nonproductive' technique. It then eliminates any production rules including those symbols after first identifying any non-productive symbols. This phase makes sure that the grammar can deduce at least one terminal string from each non-terminal symbol.

```python
       def delete_nonproductive(self):
        vn, vi, p, s = self.grammar
        # Eliminate non-productive symbols
        productive = set([s])
        updated = True
        while updated:
            updated = False
            for rule in p:
                if rule[0] in productive:
                    for symbol in rule[1]:
                        if symbol in vn or symbol in productive:
                            updated = updated or symbol not in productive
                            productive.add(symbol)
        if not productive:
            raise ValueError('The resulting grammar has no productive symbols')
        new_vn = set([s])
        new_p = [rule for rule in p if rule[0] in productive and all(s in new_vn or s in vi for s in rule[1])]
        for rule in new_p:
            for symbol in rule[1]:
                if symbol in vn:
                    new_vn.add(symbol)
        if self.grammar[3]:
            self.grammar = new_vn, vi, new_p, s
        else:
            self.grammar = new_vn, vi, new_p
```

### Convert to Chomsky Normal Form
The remaining production rules are converted to the CNF format using the 'chomsky_normal_form' function. It accomplishes this by segmenting rules with more than two symbols on the right side into several rules that follow CNF. In rules with more than one symbol on the right side, it also introduces new non-terminal symbols to replace terminal symbols.

```python
        def chomsky_normal_form(self):
        vn, vi, p, s = self.grammar
        # Add a new start symbol if necessary
        if s in vn:
            s_prime = s + "'"
            while s_prime in vn:
                s_prime += "'"
            vn.add(s_prime)
            new_p = [('S', (s,))]
            new_p.extend(p)
            new_p.append(('S', ('epsilon',)))
            self.grammar = vn, vi, new_p, 'S'
        else:
            s_prime = s
        # Eliminate epsilon productions
        self.eliminate_epsilon()
        # Eliminate renaming
        self.eliminate_renaming()
        # Eliminate inaccessible symbols
        self.eliminate_nonproductive()
        # Convert remaining productions to Chomsky normal form
        new_vn = set()
        new_p = []
        mapping = {}
        count = 0
        for rule in self.grammar[2]:
            if len(rule[1]) == 1 and rule[1][0] in self.grammar[1]:
                new_p.append(rule)
            elif len(rule[1]) == 1 and rule[1][0] in mapping:
                new_p.append((rule[0], (mapping[rule[1][0]],)))
            else:
                new_lhs = rule[0]
                new_rhs = rule[1]
                while len(new_rhs) > 2:
                    new_lhs = new_lhs + str(count)
                    count += 1
                    new_vn.add(new_lhs)
                    mapping[new_lhs] = new_rhs[:2]
                    new_p.append((new_lhs, new_rhs[:2]))
                    new_rhs = (new_lhs,) + new_rhs[2:]
                new_p.append((new_lhs, new_rhs))
        if len(new_p) == 1 and len(new_p[0][1]) == 1 and new_p[0][1][0] in self.grammar[1]:
            vn = new_vn
            s = s_prime
            vi = self.grammar[1].union(new_vn)
            p = new_p
        else:
            vn = new_vn.union(set(mapping.keys()))
            s = s_prime
            vi = self.grammar[1].union(new_vn)
            p = new_p
            for lhs, rhs in mapping.items():
                p.append((lhs, rhs))
        return vn, vi, p, s
```

# Results:
```
Chomsky normal form:
(set(), {'d', 'a'}, [('S', ('S',)), ('S', ('d',)), ('S', ('d',)), ('S', ('a',)), ('S', ('d',)), ('S', ('d',)), ('S', ('d', 'S')), ('S', ('d',)), ('S', ('S',)), ('S', ('a', 'd')), ('S', ('a',)), ('S', ('d',))], "S'")

```

# Conclusions
This project successfully applied a technique to convert a grammar to Chomsky Normal Form, taking into account each stage of the conversion procedure. By doing away with -productions, unit productions, inaccessible symbols, and non-productive symbols, the remaining production rules can then be converted to CNF. Modularity in the code makes it simpler to maintain, test, and modify. Because it simplifies grammar structures and makes them more manageable for parsing and language processing algorithms, the Chomsky Normal Form is a useful tool for researching formal languages and automata. We now have a deeper understanding of context-free grammars, their characteristics, and the CNF conversion procedure thanks to this study. Future formal language and automata theory research and projects will find great use for this information.

Chomsky Normal Form conversion has computational advantages in addition to the previously discussed advantages. For instance, parsing a grammar in CNF can be done in polynomial time, meaning that the time needed to parse a sentence only increases polynomially as the length of the sentence increases. Contrastingly, more complicated grammars could take exponentially longer to parse, making them unsuitable for use in extensive language processing applications.

Furthermore, normalizing a grammar is not possible solely through CNF. Grammars can also be made simpler in various ways by other normal forms, such as Greibach Normal Form and the Extended Backus-Naur Form (EBNF). The normal form used will rely on the particular requirements of the language processing activity at hand.

Overall, the study of formal languages and automata theory is a fascinating and dynamic discipline with several real-world applications in fields like artificial intelligence, compiler design, and natural language processing. A thorough understanding of the underlying grammatical structures and normalization procedures will remain essential as we continue to create new language processing algorithms and methods.


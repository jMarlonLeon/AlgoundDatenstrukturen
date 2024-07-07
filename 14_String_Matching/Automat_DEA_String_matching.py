
# DFA = Deterministic Finite Automaton
# Deterministischer endlicher Automat
# DFA = (Q, Σ, δ, q0, F) (5 Tupel)
# (Q: Menge der Zustände, Σ: Eingabealphabet, 
# δ: Übergangsfunktion, q0: Startzustand, F: Menge der Endzustände)

# DEA für String-Matching

class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
        self.current_state = start_state

    def transition_to_state_with_input(self, input_value):
        if (self.current_state, input_value) in self.transition_function:
            self.current_state = self.transition_function[(self.current_state, input_value)]
        else:
            self.current_state = None

    def in_accept_state(self):
        return self.current_state in self.accept_states

    def go_to_initial_state(self):
        self.current_state = self.start_state

    def run_with_input_list(self, input_list):
        self.go_to_initial_state()
        for inp in input_list:
            self.transition_to_state_with_input(inp)
            if self.current_state is None:
                return False
        return self.in_accept_state()

# Beispiel-DFA anlegen (5 Tupel)
states = {'q0', 'q1', 'q2'}
alphabet = {'a', 'b'}
transition_function = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q0',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q1',
    ('q2', 'b'): 'q0'
}
# Mermaid


start_state = 'q0'
accept_states = {'q2'}

# DFA erstellen
dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# Eingabestrings testen
test_strings = ["aab", "abb", "abba", "bbaa"]

for test_string in test_strings:
    result = dfa.run_with_input_list(list(test_string))
    print(f"String: {test_string} - Accepted: {'Yes' if result else 'No'}")
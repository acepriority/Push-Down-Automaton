"""
    A PDA is a theoretical model of computation similar to a finite automaton but with an additional
    stack storage. It is used to recognize context-free languages.

    Mathematical Definition:
    A PDA is a 7-tuple (Q, Σ, Γ, $, δ, q0, F) where:
    - Q is a finite set of states.
    - Σ is a finite set of input symbols (alphabet).
    - Γ is a finite set of stack symbols.
    - δ: Q × (Σ ∪ {ε}) × Γ → Q × Γ* is the transition function.
    - $ ∈ Γ is the stack start symbol
    - q0 ∈ Q is the start state.
    - F ⊆ Q is the set of accepting (or final) states.
"""

states = {'A', 'B', 'C'}
alphabet = {'0', '1'}
stack_alphabet = {'$', '0'}
start_state = 'A'
accept_states = {'B'}
stack_start_symbol = '$'
transition_function = {
    ('A', '0', '$'): ('A', '0$'),
    ('A', '0', '0'): ('A', '00'),
    ('A', '1', '0'): ('B', ''),
    ('B', '1', '0'): ('B', ''),
    ('B', '1', '$'): ('C', '$'),
}

input_string = '000111'


class PDA:
    """
    A class to represent a pushdown automaton (PDA).

    Attributes:
    -----------
    states : set
        A set of states in the PDA.
    alphabet : set
        The alphabet (set of input symbols) the PDA operates on.
    stack_alphabet : set
        The stack alphabet (set of stack symbols) the PDA operates on.
    start_state : str
        The start state of the PDA.
    accept_states : set
        The set of accepting states of the PDA.
    stack_start_symbol : str
        The initial symbol on the stack.
    transition_function : dict
        A dictionary representing the transition function.
    current_state : str
        The current state of the PDA during processing.
    stack : list
        The stack used by the PDA for processing input.
    """

    def __init__(self):
        """
        Initialize the PDA with states, alphabet, stack alphabet, start state, accept states,
        stack start symbol, and transition function.
        """
        self.states = states
        self.alphabet = alphabet
        self.stack_alphabet = stack_alphabet
        self.start_state = start_state
        self.accept_states = accept_states
        self.stack_start_symbol = stack_start_symbol
        self.transition_function = transition_function
        self.current_state = self.start_state
        self.stack = [self.stack_start_symbol]

    def process(self, input_string):
        """
        Process an input string to determine if it is accepted by the PDA.

        Parameters:
        -----------
        input_string : str
            The string to be processed by the PDA.

        Returns:
        --------
        bool
            True if the string is accepted by the PDA, False otherwise.
        """
        for symbol in input_string:
            if symbol not in self.alphabet:
                print(f"The symbol {symbol} doesn't belong to the alphabet [0, 1]")
                return False
            top_of_stack = self.stack.pop() if self.stack else None
            transition = self.transition_function.get((self.current_state, symbol, top_of_stack))
            if not transition:
                return False
            self.current_state, stack_push = transition
            if stack_push:
                self.stack.extend(reversed(stack_push))

        top_of_stack = self.stack.pop() if self.stack else None
        transition = self.transition_function.get((self.current_state, '', top_of_stack))
        if transition:
            self.current_state, _ = transition
        return self.current_state in self.accept_states


class Test(PDA):
    """
    A class to test the PDA with a given input string.
    """

    def __init__(self):
        """
        Initialize the Test class by inheriting from the PDA class.
        """
        super().__init__()

    def test(self, input_string):
        """
        Test the PDA with a given input string and print the result.

        Parameters:
        -----------
        input_string : str
            The input string to be tested.
        """
        if self.process(input_string):
            print(f'The string "{input_string}" is accepted by the PDA.')
        else:
            print(f'The string "{input_string}" is rejected by the PDA.')


Test().test(input_string)

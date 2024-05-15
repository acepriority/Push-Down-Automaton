# Push-Down-Automaton

This repository contains an implementation of a Pushdown Automaton (PDA) in Python. A PDA is a theoretical model of computation similar to a finite automaton but with an additional stack storage. It is used to recognize context-free languages.

## Table of Contents
- [Introduction](#introduction)
- [Mathematical Definition](#mathematical-definition)
- [Usage](#usage)
- [Example](#example)
- [Classes](#classes)
  - [PDA Class](#pda-class)
  - [Test Class](#test-class)

## Introduction

A PDA consists of a finite number of states, a finite set of input symbols (alphabet), a finite set of stack symbols, a transition function, a start state, a set of accepting states, and an initial stack symbol. The PDA processes input strings and determines whether the string belongs to the language it recognizes by using transitions that can modify the stack.

## Mathematical Definition

A PDA is formally defined as a 7-tuple `(Q, Σ, Γ, $, δ, q0, F)` where:
- `Q`: A finite set of states.
- `Σ`: A finite set of input symbols (alphabet).
- `Γ`: A finite set of stack symbols.
- `δ`: `Q × (Σ ∪ {ε}) × Γ → Q × Γ*`, the transition function.
- `q0`: The start state, `q0 ∈ Q`.
- `$`: The stack start symbol, `$ ∈ Γ`.
- `F`: A set of accepting states, `F ⊆ Q`.

## Usage

To use the PDA implementation, create an instance of the `Test` class and call the `test` method with the input string you want to process.

```python
# Example usage
Test().test(input_string)
```

## Example
Consider the following example with predefined states, alphabet, stack alphabet, start state, accept states, stack start symbol, and transition function 
for a language ```L(n) = { 0^n1^n | n>=1 }```:

```python
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
```

## Classes

### PDA Class
Attributes:
- ```states```: A set of states in the PDA.
- ```alphabet```: The alphabet (set of input symbols) the PDA operates on.
- ```stack_alphabet```: The stack alphabet (set of stack symbols) the PDA operates on.
- ```start_state```: The start state of the PDA.
- ```accept_states```: The set of accepting states of the PDA.
- ```stack_start_symbol```: The initial symbol on the stack.
- ```transition_function```: A dictionary representing the transition function.
- ```current_state```: The current state of the PDA during processing.
- ```stack```: The stack used by the PDA for processing input.

Methods:
- ```__init__()```: Initializes the PDA with the given parameters.
- ```process(input_string)```: Processes an input string to determine if it is accepted by the PDA.

### Test Class
The Test class is used to test the PDA with a given input string.

Methods:
- ```__init__()```: Initializes the Test class by inheriting from the PDA class.
- ```test(input_string)```: Tests the PDA with a given input string and prints the result.

from typing import List

from alphabet import Alphabet, AbcdAlphabet
from state import State


class Automaton:
    def __init__(self, alphabet: Alphabet):
        self._ALPHABET = alphabet
        self._INITIAL_STATE = State(0, False)
        self._STATES = [self._INITIAL_STATE]
        self._TABLE = [[]]

    @property
    def alphabet(self) -> Alphabet:
        return self._ALPHABET

    @property
    def states(self) -> List[State]:
        return self._STATES

    @property
    def initial_state(self) -> State:
        return self._INITIAL_STATE

    def next_state(self, state: State, symbol: chr) -> State:
        return self._TABLE[state.index][self._ALPHABET.index_of(symbol)]


class AbcdAutomaton(Automaton):
    def __init__(self):
        Automaton.__init__(self, AbcdAlphabet())

        for index in range(1, self._ALPHABET.size()):
            self._STATES.append(State(index, True if index == 3 else False))

        # A(B|C)*D
        self._TABLE = [[None for _ in range(self._ALPHABET.size())] for _ in range(len(self._STATES))]
        self._TABLE[0][0] = self._STATES[1]
        self._TABLE[1][1] = self._STATES[1]
        self._TABLE[1][2] = self._STATES[2]
        self._TABLE[1][3] = self._STATES[3]
        self._TABLE[2][1] = self._STATES[1]
        self._TABLE[2][2] = self._STATES[2]
        self._TABLE[2][3] = self._STATES[3]

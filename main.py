from automaton import AbcdAutomaton
from itertools import product
from pprint import pprint as pp
from time import sleep


def get_words(symbols: iter, word_len: int):
    return [''.join(x) for x in product(symbols, repeat=word_len)]


def run(word: str):
    state = auto.initial_state
    for symbol in word:
        if state is None:
            pass
        else:
            state = auto.next_state(state, symbol)
            try:
                print(f'State {state.index}')
            except AttributeError as e:
                pass
    if state is None:
        print(f'{word} does not match')
        wrong.append(word)
    elif state.is_final:
        print('You had a match')
        match.append(word)
    else:
        print('Partial match')
        partial.append(word)


if __name__ == '__main__':
    wrong = []
    partial = []
    match = []
    auto = AbcdAutomaton()
    words = []
    for i in range(10):
        words.extend(get_words(auto.alphabet.alphabet, i + 1))

    for word in words:
        print(word)
        run(word)
        # sleep(0.5)

    pp(match)

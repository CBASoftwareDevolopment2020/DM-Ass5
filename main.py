from automaton import AbcdAutomaton
from log_entry import LogEntry
from itertools import product
from pprint import pprint as pp
from time import sleep


def get_words(symbols: iter, word_len: int):
    return [''.join(x) for x in product(symbols, repeat=word_len)]


def run(symbols: str):
    print(symbols)
    state = auto.initial_state
    for symbol in symbols:
        if state is None:
            pass
        else:
            print(f'State {state.index}', '=>', symbol, end=' => ')
            state = auto.next_state(state, symbol)
            print(f'State {state.index}' if state else 'Fail')
    if state is None:
        print(f'{symbols} is not a match')
        wrong.append(symbols)
    elif state.is_final:
        print(f'{symbols} is a match')
        match.append(symbols)
    else:
        print(f'{symbols} is a partial match')
        partial.append(symbols)


if __name__ == '__main__':
    auto = AbcdAutomaton()
    words, wrong, partial, match = [[]] * 4
    for i in range(10):
        words.extend(get_words(auto.alphabet.alphabet, i + 1))

    for word in words:
        print('-' * 20)
        run(word)
        # sleep(1)

    pp(match)

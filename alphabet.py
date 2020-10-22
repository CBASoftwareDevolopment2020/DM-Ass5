class Alphabet:
    def __init__(self, symbols: iter):
        self.alphabet = sorted(symbols)

    def index_of(self, symbol: chr) -> int:
        return self.alphabet.index(symbol) if symbol in self.alphabet else -1

    def symbol_of(self, index: int) -> chr:
        return self.alphabet[index]

    def size(self) -> int:
        return len(self.alphabet)

    def __repr__(self) -> str:
        return ', '.join(self.alphabet)


class AbcdAlphabet(Alphabet):
    def __init__(self):
        Alphabet.__init__(self, ['A', 'B', 'C', 'D'])

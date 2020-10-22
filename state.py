class State:
    def __init__(self, index: int = 0, is_final: bool = False):
        self.INDEX = index
        self.IS_FINAL = is_final

    @property
    def index(self) -> int:
        return self.INDEX

    @property
    def is_final(self) -> bool:
        return self.IS_FINAL

    def __repr__(self) -> str:
        return f'{self.INDEX}: {self.IS_FINAL}'

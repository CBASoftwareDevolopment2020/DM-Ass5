from time import time, localtime, asctime


class LogEntry:
    def __init__(self, level: int, system: str, instance: str, action: chr):
        self._LEVEL = level  # 0:Information, 1:Warning, 2:Error
        self._SYSTEM = system  # System id
        self._INSTANCE = instance  # Instance id
        self._ACTION = action  # Action id
        self._TIMESTAMP = time()  # Time of the event

    @property
    def level(self) -> int:
        return self._LEVEL

    @property
    def system(self) -> str:
        return self._SYSTEM

    @property
    def instance(self) -> str:
        return self._INSTANCE

    @property
    def action(self) -> chr:
        return self._ACTION

    @property
    def timestamp(self):
        return asctime(localtime(self._TIMESTAMP))

    def __repr__(self) -> str:
        # return f'{self.level}-{self.system}-{self.instance}-{self.action}'
        return f'{self.level}-{self.system}-{self.instance}-{self.action}-{self.timestamp}'

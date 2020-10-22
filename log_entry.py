class LogEntry:
    def __init__(self, level: int, system: int, instance: int, action: chr, timestamp):
        self._LEVEL = level  # 0:Information, 1:Warning, 2:Error
        self._SYSTEM = system  # System id
        self._INSTANCE = instance  # Instance id
        self._ACTION = action  # Action id
        self._TIMESTAMP = timestamp  # Time of the event

    @property
    def level(self):
        return self._LEVEL

    @property
    def system(self):
        return self._SYSTEM

    @property
    def instance(self):
        return self._INSTANCE

    @property
    def action(self):
        return self._ACTION

    @property
    def timestamp(self):
        return self._TIMESTAMP

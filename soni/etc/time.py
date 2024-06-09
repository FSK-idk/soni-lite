import enum


class TimeFormat(enum.Enum):
    mmss = enum.auto()
    HHmmss = enum.auto()


class Time():
    def __init__(self, milliseconds : int = 0, time_format : TimeFormat = TimeFormat.mmss) -> None:
        self.milliseconds = milliseconds
        self.time_format = time_format

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Time(self.milliseconds - other.milliseconds, self.time_format)
        raise TypeError

    def __str__(self):
        match self.time_format:
            case TimeFormat.mmss:
                return f"{(self.milliseconds // 60000):02d}:{((self.milliseconds // 1000) % 60):02d}"
            case TimeFormat.HHmmss:
                return f"{(self.milliseconds // 3600000):02d}:{((self.milliseconds // 60000) % 60):02d}:{((self.milliseconds // 1000) % 60):02d}"

    def setTime(self, milliseconds : int) -> None:
        self.milliseconds = milliseconds

    def setTimeFormat(self, time_format : TimeFormat) -> None:
        self.time_format = time_format


class TimeSpan():
    def __init__(self) -> None:
        super().__init__()

        self.end = Time()
        self.current = Time()

        self.reversed = False 
    
    def getCurrentText(self) -> str:
        if self.reversed:
            return "-" + str(self.end - self.current)
        else:
            return str(self.current)
    
    def getEndText(self) -> str:
        return str(self.end)

    def setReversed(self, reversed : bool) -> None:
        self.reversed = reversed

    def setCurrentTime(self, milliseconds : int) -> None:
        self.current.setTime(milliseconds)

    def setEndTime(self, milliseconds : int) -> None:
        self.end.setTime(milliseconds)

    def setTimeFormat(self, time_format : TimeFormat) -> None:
        self.end.setTimeFormat(time_format)
        self.current.setTimeFormat(time_format)
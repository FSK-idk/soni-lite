import enum


class TimeFormat(enum.Enum):
    mmss = enum.auto()
    HHmmss = enum.auto()


class Time():
    """
    Stores time in seconds
    """

    def __init__(self, seconds : int = 0, time_format : TimeFormat = TimeFormat.mmss) -> None:
        self.seconds = seconds
        self.time_format = time_format

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Time(self.seconds - other.seconds, self.time_format)
        raise TypeError

    def __str__(self):
        match self.time_format:
            case TimeFormat.mmss:
                return f"{(self.seconds // 60):02d}:{(self.seconds % 60):02d}"
            case TimeFormat.HHmmss:
                return f"{(self.seconds // 3600):02d}:{((self.seconds // 60) % 60):02d}:{(self.seconds % 60):02d}"

    def set_time(self, seconds : int) -> None:
        self.seconds = seconds

    def set_time_format(self, time_format : TimeFormat) -> None:
        self.time_format = time_format


class TimeSpan():
    def __init__(self) -> None:
        super().__init__()

        self.end = Time()
        self.current = Time()

        self.reversed = False 
    
    def get_current_text(self) -> str:
        if self.reversed:
            return "-" + str(self.end - self.current)
        else:
            return str(self.current)
    
    def get_end_text(self) -> str:
        return str(self.end)

    def set_reversed(self, reversed : bool) -> None:
        self.reversed = reversed

    def set_current_time(self, seconds : int) -> None:
        self.current.set_time(seconds)

    def set_end_time(self, seconds : int) -> None:
        self.end.set_time(seconds)

    def set_time_format(self, time_format : TimeFormat) -> None:
        self.end.set_time_format(time_format)
        self.current.set_time_format(time_format)
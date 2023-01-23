Требуется реализовать на языке Python класс Time.

У класса должен быть следующий интерфейс:

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        if hours < 0 or minutes < 0 or seconds < 0 or milliseconds < 0:
            raise ValueError("Time parameters must be non-negative")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds
        self._normalize()

    def _normalize(self):
        self.hours += self.minutes // 60
        self.minutes %= 60
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.seconds += self.milliseconds // 1000
        self.milliseconds %= 1000
        self.hours %= 24

    def GetHour(self):
        return self.hours

    def GetMinute(self):
        return self.minutes

    def GetSecond(self):
        return self.seconds

    def GetMillisecond(self):
        return self.milliseconds

    def Add(self, time):
        self.hours += time.hours
        self.minutes += time.minutes
        self.seconds += time.seconds
        self.milliseconds += time.milliseconds
        self._normalize()

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}.{self.milliseconds}"
          
time = Time(25, 11, 12, 1)
print(str(time))
time.Add(Time(0, 0, 0, 1010))
print(str(time))

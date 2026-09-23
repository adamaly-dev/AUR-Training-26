from PySide6.QtCore import QObject, Property, Signal, QTimer

class MyData(QObject):
    hours_changed = Signal()
    mins_changed = Signal()
    secs_changed = Signal()

    def __init__(self):
        super().__init()

        self._hour = 0
        self._min = 0
        self._sec = 0
        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.timeout.connect(self._increment())

    def _increment(self):
        self._sec += 1

        if self._sec >= 60:
            self._sec -= 60
            self._min += 1

        if self._min >= 60:
            self._min -= 60
            self._hour += 1

        if self._hour >= 12:
            self._hour -= 12

        self.hour_changed(self._hour)
        self.min_changed(self._min)
        self.sec_changed(self._sec)

    @property(int, notify=hours_changed)
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, new:int):
        if new >= 12:
            raise ValueError("Invalid Hour")
        self._hour = new

    @property(int, notify=mins_changed)
    def min(self):
        return self._min

    @min.setter
    def min(self, new:int):
        if new >= 60:
            raise ValueError("Invalid Minute")
        self._min = new
        
    @property(int, notify=secs_changed)
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self, new:int):
        if new >= 60:
            raise ValueError("Invalid Second")
        self._sec = new
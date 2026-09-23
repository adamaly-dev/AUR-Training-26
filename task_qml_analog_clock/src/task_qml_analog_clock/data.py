from PySide6.QtCore import QObject, Property, Signal, QTimer

class MyData(QObject):
    hours_changed = Signal()
    mins_changed = Signal()
    secs_changed = Signal()

    def __init__(self):
        super().__init__()

        self._hour = 0
        self._min = 0
        self._sec = 0
        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.start()
        self._timer.timeout.connect(self._increment)

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

    @Property(int, notify=hours_changed)
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, new:int):
        if new >= 12:
            raise ValueError("Invalid Hour")
        self._hour = new
        self.hours_changed.emit(self._hour)

    @Property(int, notify=mins_changed)
    def min(self):
        return self._min

    @min.setter
    def min(self, new:int):
        if new >= 60:
            raise ValueError("Invalid Minute")
        self._min = new
        self.mins_changed.emit(self._min)
        
    @Property(int, notify=secs_changed)
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self, new:int):
        if new >= 60:
            raise ValueError("Invalid Second")
        self._sec = new
        self.secs_changed.emit(self._sec)
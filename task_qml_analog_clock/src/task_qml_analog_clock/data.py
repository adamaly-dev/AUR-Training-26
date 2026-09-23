from PySide6.QtCore import QObject, Property, Signal, QTimer

class MyData(QObject):
    hours_changed = Signal()
    mins_changed = Signal()
    secs_changed = Signal()

    def __init__(self, parent):
        super().__init__(parent)

        self._hour = 0
        self._min = 0
        self._sec = 0
        self._timer = QTimer()
        self._timer.setInterval(1000)
        self._timer.start()
        self._timer.timeout.connect(self._increment)

    @Property(int, notify=hours_changed)
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, new:int):
        if new >= 12:
            raise ValueError("Invalid Hour")
        self._hour = new
        self.hours_changed.emit()

    @Property(int, notify=mins_changed)
    def min(self):
        return self._min

    @min.setter
    def min(self, new:int):
        if new >= 60:
            raise ValueError("Invalid Minute")
        self._min = new
        self.mins_changed.emit()
        
    @Property(int, notify=secs_changed)
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self, new:int):
        if new >= 60:
            raise ValueError("Invalid Second")
        self._sec = new
        self.secs_changed.emit()

        
    def _increment(self):
        print(self.hour, self.min, self.sec)
        self.sec += 1

        if self.sec >= 60:
            self.sec -= 60
            self.min += 1

        if self.min >= 60:
            self.min -= 60
            self.hour += 1

        if self.hour >= 12:
            self.hour -= 12

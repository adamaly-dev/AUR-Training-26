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
        self._hour = new
        self.hours_changed.emit()

    @Property(int, notify=mins_changed)
    def min(self):
        return self._min

    @min.setter
    def min(self, new:int):
        self._min = new
        self.mins_changed.emit()
        
    @Property(int, notify=secs_changed)
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self, new:int):
        self._sec = new
        self.secs_changed.emit()

        
    def _increment(self):

        if self.sec < 59:
            self.sec += 1
        elif self.min < 59:
            self.sec = 0
            self.min += 1
        elif self.hour < 11:
            self.sec = 0
            self.min = 0
            self.hour += 1
        else:
            self.sec = 0
            self.min = 0
            self.hour = 0

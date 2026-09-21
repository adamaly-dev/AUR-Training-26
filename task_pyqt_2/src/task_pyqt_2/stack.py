from PySide6.QtWidgets import QStackedWidget, QLineEdit, QLabel
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QTimer, Signal

class Stack(QStackedWidget):
    time_running = Signal(bool)

    def __init__(self):
        super().__init__()

        self._line_edit = QLineEdit()
        self._label = QLabel(text='00:00')
        
        self.addWidget(self._line_edit)
        self.addWidget(self._label)

        self.setCurrentIndex(0)

        validator = QIntValidator(0, 3599, self)

        self._line_edit.setValidator(validator)
        self._line_edit.textChanged.connect(self._update_time)

        self._remaining_time = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._tick)

    def _update_time(self):
        if len(self._line_edit.text()) == 0:
            return
        self._remaining_time = int(self._line_edit.text())

    def _update_label(self):
        m, s = self._remaining_time//60, self._remaining_time%60
        m_s = str(m)
        s_s = str(s)
        while len(m_s) < 2:
            m_s = '0'+m_s
        while len(s_s) < 2:
            s_s = '0'+s_s
        self._label.setText(f'{m_s}:{s_s}')

    def start_timer(self):
        if self._remaining_time <= 0:
            return

        self._line_edit.clear()
        self._timer.setInterval(1000)
        self._timer.start()
        self._update_label()
        self.setCurrentIndex(1)
        self.time_running.emit(True)

    def pause_timer(self):
        self._timer.stop()
        self.time_running.emit(False)

    def reset_timer(self):
        self.setCurrentIndex(0)
        self._remaining_time = 0
        self._timer.stop()
        self._line_edit.clear()

    def _tick(self):
        self._remaining_time -= 1
        self._update_label()
        if self._remaining_time == 0:
            self._timer.stop()
            self.setCurrentIndex(0)
            self.time_running.emit(False)

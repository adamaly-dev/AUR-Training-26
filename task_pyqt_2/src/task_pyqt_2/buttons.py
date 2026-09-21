from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Signal


class Buttons(QWidget):
    start = Signal()
    pause = Signal()
    reset = Signal()

    def __init__(self):
        super().__init__()

        self._layout = QHBoxLayout(self)
        self._toggle_state = 0
        self._toggle = QPushButton('Start')
        self._reset = QPushButton('Reset')

        self._layout.addWidget(self._toggle)
        self._layout.addWidget(self._reset)

        self._toggle.clicked.connect(self._b1_clicked)
        self._reset.clicked.connect(self._b2_clicked)

    def _b1_clicked(self):
        if self._toggle_state == 0:
            self.start.emit()
        else:
            self.pause.emit()
    
    def _b2_clicked(self):
        self.reset.emit()
        self._toggle_state = 0
        self._toggle.setText('Start')

    def toggle_states(self, time_stop):
        self._toggle_state = time_stop
        if self._toggle_state == 0:
            self._toggle.setText('Start')
        else:
            self._toggle.setText('Pause')
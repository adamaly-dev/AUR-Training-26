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

    def _toggle_states(self, time_stop=-1):
        if time_stop == -1:
            return
        
        self._toggle_state = not self._toggle_state
        if self._toggle_state == 0:
            self._toggle.setText('Start')
        else:
            self._toggle.setText('Pause')

    def return_to_initial_state(self):
        self._toggle_state = 0
        self._toggle.setText('Start')
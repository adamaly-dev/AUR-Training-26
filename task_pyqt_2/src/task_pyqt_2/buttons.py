from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Signal


class Buttons(QWidget):
    start = Signal()
    pause = Signal()
    reset = Signal()

    def __init__(self):
        super().__init__()

        self._layout = QHBoxLayout(self)
        self._toggle = QPushButton('Start')
        self._reset = QPushButton('Reset')

        self._layout.addWidget(self._toggle)
        self._layout.addWidget(self._reset)

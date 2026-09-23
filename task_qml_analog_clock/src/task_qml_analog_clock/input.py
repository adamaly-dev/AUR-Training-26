from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIntValidator

class Input(QWidget):
    time_submitted = Signal(int, int, int)

    def __init__(self, parent):
        super().__init__(parent)

        self._hour = QLineEdit()
        self._min = QLineEdit()
        self._sec = QLineEdit()

        self._hour.setPlaceholderText('Hour')
        self._min.setPlaceholderText('Minute')
        self._sec.setPlaceholderText('Second')

        self._hour.setAlignment(Qt.AlignCenter)   
        self._min.setAlignment(Qt.AlignCenter)   
        self._sec.setAlignment(Qt.AlignCenter)   

        validator_60 = QIntValidator(0, 59)
        validator_12 = QIntValidator(1, 12)

        self._hour.setValidator(validator_12)
        self._min.setValidator(validator_60)
        self._sec.setValidator(validator_60)

        self._layout2 = QHBoxLayout()

        self._layout2.addWidget(self._hour)
        self._layout2.addWidget(self._min)
        self._layout2.addWidget(self._sec)

        self._btn = QPushButton()
        self._btn.setText('Submit')

        self._layout = QVBoxLayout(self)

        self._layout.addLayout(self._layout2)
        self._layout.addWidget(self._btn)

        self._btn.clicked.connect(self._confirm)

    def _confirm(self):
        if len(self._hour.text()) == 0 or len(self._min.text()) == 0 or len(self._sec.text()) == 0:
            return
        
        h = int(self._hour.text())
        m = int(self._min.text())
        s = int(self._sec.text())

        if h == 12:
            h = 0

        self.time_submitted.emit(h, m, s)
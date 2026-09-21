from PySide6.QtWidgets import QStackedWidget, QLineEdit, QWidget, QLabel
from PySide6.QtGui import QIntValidator
from PySide6.QtCore import QTimer, Signal, Qt

class Stack(QStackedWidget):
    time_stopped = Signal(bool)

    def __init__(self):
        super().__init__()

        self._line_edit = QLineEdit()
        self._label = QLabel(text='00:00')
        
        self.addWidget(self._line_edit)
        self.addWidget(self._label)

        self.setCurrentIndex(0)


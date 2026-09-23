from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from task_qml_analog_clock.data import MyData
from task_qml_analog_clock.status_widget import StatusWidget
from task_qml_analog_clock.input import Input

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self._data = MyData(self)

        self._clock_widget = StatusWidget('clock.qml', self._data)
        self._input_widget = Input()

        self._layout = QVBoxLayout()

        self._layout.addWidget(self._clock_widget)
        self._layout.addWidget(self._input_widget)

        self._central = QWidget()
        self._central.setLayout(self._layout)

        self.setCentralWidget(self._central)

        self.show()


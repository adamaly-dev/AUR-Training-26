from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from task_qml_analog_clock.data import MyData
from task_qml_analog_clock.status_widget import StatusWidget
from task_qml_analog_clock.input import Input

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self._data = MyData(self)

        self._widget = StatusWidget('clock.qml', self._data)

        self.setCentralWidget(self._widget)

        self.show()


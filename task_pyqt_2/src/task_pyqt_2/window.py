from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from task_pyqt_2.buttons import Buttons
from task_pyqt_2.stack import Stack

class Window(QMainWindow):

    def __init__(self):
        super().__init__()


        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self._layout = QVBoxLayout(central_widget)
        self._buttons = Buttons()
        self._stack = Stack()

        self._layout.addWidget(self._stack)
        self._layout.addWidget(self._buttons)

        self._buttons.start.connect(self._stack.start_timer)
        self._stack.time_running.connect(self._buttons._toggle_states)

        self.show()

        
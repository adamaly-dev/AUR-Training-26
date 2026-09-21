from PySide6.QtWidgets import QApplication
from task_pyqt_2.window import Window

def main() -> None:
    app = QApplication()
    win = Window()
    app.exec()
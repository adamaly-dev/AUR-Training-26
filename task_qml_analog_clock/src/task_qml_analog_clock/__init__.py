from PySide6.QtWidgets import QApplication
from task_qml_analog_clock.window import Window

def main() -> None:
    print("Hello from session3!")
    app = QApplication()
    win = Window()
    app.exec()
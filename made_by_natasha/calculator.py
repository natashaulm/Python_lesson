import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')
        self.setGeometry(50, 50, 200, 200)

        self.label = QLabel(0, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label.setStyleSheet("font-size: 24px;")

        self.current_input= ''
        self.result = 0
        self.operation = None

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        button_layout = QGridLayout()

        buttons =  [
            (7, 0, 0), (8, 0, 1), (9, 0, 2), ('/', 0, 3),
            (4, 1, 0), (5, 1, 1), (6, 1, 2), ('*', 1, 3),
            (1, 2, 0), (2, 2, 1), (3, 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('+', 3, 1), ('=', 3, 2), (0, 3, 3)
        ]
 













if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
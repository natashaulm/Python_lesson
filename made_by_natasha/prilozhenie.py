import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Счетчик')
        self.setGeometry(50, 50, 200, 200)
        self.counter = 0
        
        self.label = QLabel(str(self.counter), self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        self.increment_button = QPushButton('+', self)
        self.decrement_button = QPushButton('-', self)

        
        self.increment_button.clicked.connect(self.increment)
        self.decrement_button.clicked.connect(self.decrement)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.increment_button)
        layout.addWidget(self.decrement_button) 

        self.setLayout(layout) 

    def increment(self):
        self.counter += 1
        self.label.setText(str(self.counter))
        
    def decrement(self):
        self.counter -= 1
        self.label.setText(str(self.counter))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
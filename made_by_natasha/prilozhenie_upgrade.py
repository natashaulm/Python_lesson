import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Счетчик')
        self.setGeometry(50, 50, 200, 200)
        self.counter = 0
        
        self.label = QLabel(str(self.counter), self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Поле для ввода значения
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите значение")
        
        self.increment_button = QPushButton('+', self)
        self.decrement_button = QPushButton('-', self)
        self.multiply_button = QPushButton('*', self)

        self.increment_button.clicked.connect(self.increment)
        self.decrement_button.clicked.connect(self.decrement)
        self.multiply_button.clicked.connect(self.multiply)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)  
        layout.addWidget(self.increment_button)
        layout.addWidget(self.decrement_button)
        layout.addWidget(self.multiply_button) 

        self.setLayout(layout) 

    def increment(self):
        try:
            value = float(self.input_field.text())
            self.counter += value
            self.label.setText(str(self.counter))
            self.input_field.clear()  
        except ValueError:
            self.label.setText("Ошибка: Введите число")

    def decrement(self):
        try:
            value = float(self.input_field.text())
            self.counter -= value
            self.label.setText(str(self.counter))
            self.input_field.clear()  
        except ValueError:
            self.label.setText("Ошибка: Введите число")

    def multiply(self):
        try:
            value = float(self.input_field.text())
            self.counter *= value
            self.label.setText(str(self.counter))
            self.input_field.clear()  
        except ValueError:
            self.label.setText("Ошибка: Введите число")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
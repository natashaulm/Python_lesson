import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Варианты строчки")
        self.setGeometry(100, 100, 400, 200)
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите строку...")
        self.increment_button = QPushButton("Показать варианты", self)
        self.increment_button.clicked.connect(self.show_variants) 
        self.capitalized_label = QLabel("", self)  
        self.last_letters_label = QLabel("", self)  
        
        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.increment_button)
        layout.addWidget(self.capitalized_label)
        layout.addWidget(self.last_letters_label)
        self.setLayout(layout)

    def show_variants(self):
        input_string = self.input_field.text().strip()

        capitalized_words = ' '.join(word.capitalize() for word in input_string.split())
        self.capitalized_label.setText(f"Слова с заглавными буквами: {capitalized_words}")

        last_letters = ''.join(word[-1] for word in input_string.split() if word)
        self.last_letters_label.setText(f"Последние буквы: {last_letters}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')
        self.setGeometry(50, 50, 200, 200)

        self.label = QLabel('0', self)  
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label.setStyleSheet("font-size: 24px;")

        self.current_input = ''  
        self.result = 0  
        self.operation = None  

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        button_layout = QGridLayout()

       
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('.', 4, 0)
        ]

        for (text, row, col) in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))  
            button_layout.addWidget(button, row, col)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def on_button_click(self, button_text):
        if button_text == 'C':
            self.current_input = ''  
            self.result = 0  
            self.label.setText('0')
        # elif button_text in {'+', '-', '*', '/'}:
        #     if self.current_input:
        #         self.result = float(self.current_input)
        #         self.current_input = ''
        #     self.operation = button_text  
        #     self.label.setText(str(self.result))
              
        elif button_text == '=':
            self.label.setText(str(eval(self.current_input)))
            # if self.current_input and self.operation:
            #     self.calculate_result()
        else:  # Обработка чисел
            self.current_input += button_text
            self.label.setText(self.current_input)

    def calculate_result(self):
        try:
            if self.operation == '+':
                self.result += float(self.current_input)
            elif self.operation == '-':
                self.result -= float(self.current_input)
            elif self.operation == '*':
                self.result *= float(self.current_input)
            elif self.operation == '/':
                self.result /= float(self.current_input)
           

            self.label.setText(str(self.result))
            self.current_input = ''  
            self.operation = None  
        except ValueError:
            self.label.setText("Ошибка")

    
    def set_operation(self, operation):
        if self.current_input:
            self.result = float(self.current_input)
            self.current_input = ''
            self.operation = operation  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
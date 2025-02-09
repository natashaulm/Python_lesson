import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Добавление и удаление кнопок")
        self.setGeometry(100,100,400,400)
        
        self.layout = QVBoxLayout()
        self.button_list = []
        
        self.add_button = QPushButton("Добавить кнопку")
        self.add_button.clicked.connect(self.add_button_clicked)
        self.layout.addWidget(self.add_button)
        
        
        self.add_button = QPushButton("Удалить")
        self.add_button.clicked.connect(self.del_button_clicked)
        self.layout.addWidget(self.add_button)
        
        self.setLayout(self.layout)
        
        
    def add_button_clicked(self):
        new_button = QPushButton(f"Новая кнопка{len(self.button_list)}")
        self.layout.addWidget(new_button)
        self.button_list.append(new_button)
        
    def del_button_clicked(self):
        if self.button_list:
            last_button = self.button_list.pop()
            last_button.deleteLater()
        
        
        
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
            
                      
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Счетчик')
        self.setGeometry(100,100,200,200)
        self.counter = 0
        
        self.label = QLabel(str(self.counter),self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button = QPushButton('+',self)
        self.button.clicked.connect(self.increment)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout) 
        
        
    def increment(self):
        self.counter += 1
        self.label.setText(str(self.counter))

        









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
    
    
    
    
    
    
    
    
    
# class Cat:
#     def __init__(self,name=""):
#         if name == "":
#             self.name = "VASYA"
#         else:
#             self.name = name 

#     def meow(self):
#         print("meow")
    
#     def sleep(self):
#         print(self.name)
#         print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZzz")
#         self.meow()
                
                

# class DworowiyCat(Cat):
#     def __init__(self):
#         super().__init__("Genadiy")
        
#     def fight(self):
#         print(self.name)
#         print("HFHAFHAHFHFAHFHFAHFHAHFh")
        
        
#     def meow(self):
#         print("hello")
            
    
    
# cat_1 = DworowiyCat()
# cat_1.meow()
    
    
    
    
    
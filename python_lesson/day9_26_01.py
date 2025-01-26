import sys
import requests
from bs4 import BeautifulSoup
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,QLineEdit,QFileDialog



class Exctractor(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Парсинг страниц")
        self.setGeometry(100,100,400,400)
        
        layout = QVBoxLayout()
        
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("ВВедите URL")
        layout.addWidget(self.url_input)
        
        self.exctract_button = QPushButton("Извлечение заголовков",self)
        self.exctract_button.clicked.connect(self.extract_headers)
        layout.addWidget(self.exctract_button)
        
        self.save_button = QPushButton("Сохранить в файл",self)
        self.save_button.clicked.connect(self.save_method)
        layout.addWidget(self.save_button)
        
        self.result_label = QLabel("Заголовки...",self)
        layout.addWidget(self.result_label)
        
        self.headers = []
        
        self.setLayout(layout)
        
    def extract_headers(self):
        url = self.url_input.text()
        if url:
            try:
                response = requests.get(url)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text,'html.parser')
                
                self.headers = []
                for level in range(1,7):
                    headers = soup.find_all(f"h{level}")
                    for header in headers:
                        self.headers.append(header.get_text(strip=True))

                if self.headers:
                    self.result_label.setText('\n'.join(self.headers))
                else:
                    self.result_label.setText("Заголовки не найдены") 
            except requests.RequestException as e:
                self.result_label.setText(f"Ошибка - {str(e)}")
        else:
            self.result_label.setText("Введите URL")

    def save_method(self):
        if self.headers:
            file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить заголовки",'',"Text files (*.txt)")
            
            if file_name:
                try:
                    site_name = self.url_input.text().split('//')[-1].split('/')[0]
                    file_name = f"{site_name}.txt"
                    with open(file_name,'w',encoding='utf-8') as f:
                        for header in self.headers:
                            f.write(header+"\n")
                        self.result_label.setText(f"Заголовки сохранены в файл {file_name}")
                    
                except Exception as ex:
                    self.result_label.setText("Ошибка при создании файла")                    
            else:
                self.result_label.setText("Нет файла")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Exctractor()
    window.show()
    sys.exit(app.exec())
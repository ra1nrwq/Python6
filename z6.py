from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Сигналы и слоты")
        
        self.label = QLabel("Нажмите кнопку", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 14))
        self.label.setStyleSheet("color: black;")

        self.button = QPushButton("Нажми меня", self)
        self.button.setStyleSheet("background-color: lightblue; font-size: 16px;")
        
        self.button.clicked.connect(self.update_text_and_style)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def update_text_and_style(self):
        self.label.setText("Кнопка нажата!")
        self.label.setStyleSheet("color: green; font-size: 20px;")
        self.button.setStyleSheet("background-color: orange; font-size: 18px;")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

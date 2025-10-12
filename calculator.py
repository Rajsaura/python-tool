from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QGridLayout
from PyQt5.QtGui import QFont

import sys

class CalApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator App...")

        self.box = QLineEdit()
        # self.box.setStyleSheet("{background-color: #; color:#ffffff; margin:0px,0px,0px,0px}")
        self.grid = QGridLayout()

        Buttons = ["1","2","3","4","5","6","7","8","9","0","*","/","+" ,"-","C","<"]

        r = 0
        c = 0
        for button in Buttons:
            btn = QPushButton(button)
            # btn.setStyleSheet("QPushButton {font: 25px Comics Sans MS ; background-color:#060606; color:#ffffff; margin:0px,0px,0px,0px;}")
            btn.clicked.connect(self.button_click)
            self.grid.addWidget(btn, r, c)
            c += 1
            if c > 3:
                c = 0
                r += 1
        self.result = QPushButton("=")
        self.result.setStyleSheet("QPushButton {font: 25px Comics Sans MS}")
        self.result.clicked.connect(self.button_click)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.box)
        main_layout.addLayout(self.grid)
        main_layout.addWidget(self.result)
        self.setLayout(main_layout)

        
        # self.result = QFont()

    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            symbol = self.box.text()
            try:
                result = str(eval(symbol))
                self.box.setText(result)
            except Exception:
                self.box.setText("Error")
        elif text == "C":
            self.box.clear()
        elif text == "<":
            current_text = self.box.text()
            self.box.setText(current_text[:-1])
        else:
            current_text = self.box.text()
            self.box.setText(current_text + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalApp()
    window.setStyleSheet("{{background-color: #; color:#625D5D}}")
    window.show()
    sys.exit(app.exec_())




























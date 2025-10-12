from PyQt5.QtCore import Qt
from PyQt5.QtWidgets  import  QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QLineEdit, QGridLayout


#app 
import sys
app =  QApplication(sys.argv)
Main_window = QWidget()
Main_window.setWindowTitle("calculator app...")

#function

def button_click():
    button = app.sender()
    text = button.text()

    if text == "=":
        symbol = box.text()
        try:
            result = str(eval(symbol))
            box.setText(result)
        except Exception as e:
            box.setText("error")
    elif text =="C":
        box.clear()
    elif text == "<":
        current_text = box.text()
        box.setText(current_text[:-1])
    else:
        current_text = box.text()
        box.setText(current_text + text)

#layout

box  =  QLineEdit()
grid = QGridLayout()

Buttons = ["1","2","3","4","5","6","7","8","9","0","*","/","+" ,"-","C","<","="]
button_1 = QPushButton("=")

#looping

r = 0
c = 0

for button in Buttons:
    text_button = QPushButton(button)
    text_button.clicked.connect(button_click)
    grid.addWidget(text_button,r,c)
    c += 1
    if c > 2:
        c = 0
        r += 1

#layout

main_layout = QVBoxLayout()
main_layout.addWidget(box)
main_layout.addLayout(grid)
Main_window.setLayout(main_layout)



Main_window.show()
app.exec_()

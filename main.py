import sys
from PyQt5.QtWidgets  import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout,QColorDialog




class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet("background-color:gray")

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setStyleSheet("height:110px;font-size:30px")
        layout.addWidget(self.display)

        grid = QGridLayout()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setStyleSheet("background-color:pink;font-size:30px")
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn, row, col, 1, 1)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_click(self):
        sender = self.sender()
        text = sender.text()
        current_text = self.display.text()

        if text == '=':
            try:
                result = eval(current_text)
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        else:
            new_text = current_text + text
            self.display.setText(new_text)

def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())


# if name == '__main__':
main()


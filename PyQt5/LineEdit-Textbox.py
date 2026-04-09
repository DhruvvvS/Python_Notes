# PyQt5 Line Edit (Textbox)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Line Edit Example")
        self.setGeometry(700, 400, 500, 500)
        self.line_edit = QLineEdit(self)  # Create a QLineEdit widget
        self.button = QPushButton("Submit", self)  # Create a QPushButton widget
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(50, 50, 200, 30)  # Set the position and size of the line edit
        self.line_edit.setPlaceholderText("Enter your name")  # Set the placeholder text for the line edit
        self.button.setGeometry(260, 50, 100, 30)  # Set the position and size of the button
        self.button.clicked.connect(self.button_clicked)  # Connect the clicked signal to the button_clicked method

    def button_clicked(self):
        text = self.line_edit.text()  # Get the current text from the line edit
        print(f"Hello, {text}!")  # Print the text to the console

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
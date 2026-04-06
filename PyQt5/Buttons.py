# PyQt5 Buttons implementation

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Buttons Example")
        self.setGeometry(700, 400, 500, 500)
        self.button = QPushButton("Click Me", self)  # Create a QPushButton with the text "Click Me"
        self.label = QLabel("Hello!", self)  # Create a QLabel to display some text
        self.initUI()

    def initUI(self):
        self.button.setGeometry(200, 200, 100, 50)  # Set the position and size of the button
        self.button.setStyleSheet("background-color: lightblue; font-size: 16px;")  # Set the style of the button
        
        # signal.connect(slot) is used to connect a signal (like a button click) to a slot (a method that will be called when the signal is emitted).
        self.button.clicked.connect(self.on_button_click)  # Connect the button's clicked signal to the on_button_click method

        self.label.setGeometry(200, 150, 100, 30)  # Set the position and size of the label
        self.label.setStyleSheet("font-size: 16px;")  # Set the style of the label

    # Method that will be called when the button is clicked
    def on_button_click(self):
        print("Button was clicked!")  # Print a message to the console when the button is clicked
        self.label.setText("Button Clicked!")  # Change the text of the label when the button is clicked
        self.button.setText("Clicked")  # Change the text of the button when it is clicked
        self.button.setDisabled(True)  # Disable the button after it is clicked

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
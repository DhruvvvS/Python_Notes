# PyQt5 Labels Example

import sys

# importing QLabel module from PyQt5.QtWidgets pacjkage to create a label in the application
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel  

from PyQt5.QtGui import QFont  # importing QFont module to set font properties for the label

from PyQt5.QtCore import Qt  # importing Qt module to set alignment for the label

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Labels Example")
        self.setGeometry(700, 400, 500, 500)

        # Create a QLabel
        label = QLabel("Hello, PyQt5!", self)
        label.setFont(QFont("Arial", 16))  # Set font and size for the label
        label.setGeometry(50, 50, 200, 50)  # Set the position and size of the label
        label.move(50, 50)  # Move the label to a specific position

        # It is similar to CSS style, you can set various properties like color, background-color, font-size, etc.
        label.setStyleSheet("color: lightblue;" 
                            "background-color: gray;"
                            "font-weight: bold;"
                            "font-style: italic;" 
                            "text-decoration: underline;")

        # label.setAlignment(Qt.AlignLeft)  # Set the alignment of the label text to left
        # label.setAlignment(Qt.AlignRight)  # Set the alignment of the label text to right
        # label.setAlignment(Qt.AlignTop)  # Set the alignment of the label text to top
        # label.setAlignment(Qt.AlignBottom)  # Set the alignment of the label text to bottom
        # label.setAlignment(Qt.AlignVCenter)  # Set the alignment of the label text to vertical center
        # label.setAlignment(Qt.AlignHCenter)  # Set the alignment of the label text to horizontal center
        # label.setAlignment(Qt.AlignHcenter | Qt.AlignVCenter)  # Set the alignment of the label text to both horizontal and vertical center using bitwise OR (|) operator
        label.setAlignment(Qt.AlignCenter)  # Set the alignment of the label text to center  

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
# Cascading Style Sheets (CSS) in PyQt5 
# allow you to customize the appearance of your application by applying styles to widgets. 
# You can define styles for various widget types, such as QPushButton, QLabel, QLineEdit, etc., using CSS syntax.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 CSS Styles Example")
        self.setGeometry(700, 400, 500, 500)
        self.button1 = QPushButton("#1", self)  # Create a QPushButton widget
        self.button2 = QPushButton("#2", self)  # Create another QPushButton widget
        self.button3 = QPushButton("#3", self)  # Create another QPushButton widget
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Set the central widget

        hbox = QHBoxLayout()  # Create a horizontal box layout

        hbox.addWidget(self.button1)  # Add button1 to the layout
        hbox.addWidget(self.button2)  # Add button2 to the layout
        hbox.addWidget(self.button3)  # Add button3 to the layout

        central_widget.setLayout(hbox)  # Set the layout for the central widget

        # Set object names for the buttons to target them in CSS in set StyleSheet method.
        self.button1.setObjectName("button1")  # Set the object name for button1
        self.button2.setObjectName("button2")  # Set the object name for button2
        self.button3.setObjectName("button3")  # Set the object name for button3

        # Instead of setting styles for each button individually, we can use CSS to style all buttons at once.
        # triple quotes allow you to write multi-line strings, which is useful for defining CSS styles in a more readable format.
        self.setStyleSheet("""
            QPushButton {
                /* background-color: lightblue; Set the background color of all QPushButton widgets to light blue */
                color: black;  /* Set the text color of all QPushButton widgets to black */
                font-size: 40px;  /* Set the font size of all QPushButton widgets to 40 pixels */
                font-family: Arial;  /* Set the font family of all QPushButton widgets to Arial */
                padding: 15px 75px;  /* Add padding around the text in all QPushButton widgets i.e., horizontal padding of 15px and vertical padding of 75px */
                margin: 25px;  /* Add a margin of 25 pixels around all QPushButton widgets */
                border: 2px solid black;  /* Add a solid black border with a width of 2 pixels to all QPushButton widgets */
                border-radius: 15px;  /* Add rounded corners to all QPushButton widgets */
            }
                           
            QPushButton#button1 {
                background-color: hsl(357, 96%, 58%);  /* Set the background color of button1 to hue 357, saturation 96%, lightness 58% */
            }
            QPushButton#button2 {
                background-color: hsl(97, 96%, 58%);  /* Set the background color of button2 to hue 97, saturation 96%, lightness 58% */
            }
            QPushButton#button3 {
                background-color: hsl(213, 96%, 58%);  /* Set the background color of button3 to hue 213, saturation 96%, lightness 58 % */
            }
                           
            QPushButton#button1:hover {
                background-color: hsl(357, 96%, 78%);  /* Increase the lightness to 78 on hover */
            }
            QPushButton#button2:hover {
                background-color: hsl(97, 96%, 78%);  /* Increase the lightness to 78 on hover */
            }
            QPushButton#button3:hover {
                background-color: hsl(213, 96%, 78%);  /* Increase the lightness to 78 on hover */
            }
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
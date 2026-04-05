# PyQt5 Layouts 

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QVBoxLayout,
                              QWidget, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Layouts Example")
        self.setGeometry(700, 400, 500, 500)
        self.initUI()

    # Normally we can't add widgets directly to the main window, we need to create a central widget and set it as the central widget of the main window.
    # Then we can add layouts and widgets to this central widget.

    # anything that deals with the UI should be in this method to keep the code organized and clean.
    def initUI(self):
        central_widget = QWidget(self)  # Create a central widget
        self.setCentralWidget(central_widget)  # Set the central widget

        # Create some labels to add to the layouts
        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)

        label1.setStyleSheet("background-color: red; color: white; font-size: 20px;")
        label2.setStyleSheet("background-color: green; color: white; font-size: 20px;")
        label3.setStyleSheet("background-color: blue; color: white; font-size: 20px;")
        label4.setStyleSheet("background-color: yellow; color: black; font-size: 20px;")

        # Create a vertical layout and add some labels to it
        v_layout = QVBoxLayout()
        v_layout.addWidget(label1)
        v_layout.addWidget(label2)
        v_layout.addWidget(label3)

        # Create a horizontal layout and add some labels to it
        h_layout = QHBoxLayout()
        h_layout.addWidget(label1)
        h_layout.addWidget(label2)
        h_layout.addWidget(label3)

        # Create a grid layout and add some labels to it
        # Here this numbers after label are the row and column numbers where the label will be placed in the grid layout.
        grid_layout = QGridLayout()
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(label2, 0, 1)
        grid_layout.addWidget(label3, 1, 0)
        grid_layout.addWidget(label4, 1, 1)

        # Now we can set one of the layouts as the main layout for the central widget
        central_widget.setLayout(grid_layout)  # You can switch this to h_layout or grid_layout to see different layouts

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":    
    main()
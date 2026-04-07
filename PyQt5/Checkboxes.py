# PyQt5 Checkboxes implementation

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel

# Qtcore module is used to handle core non-GUI functionality, such as event handling, timers, and signals/slots in PyQt5 applications.
# It provides the necessary tools to manage the application's event loop and handle user interactions effectively.
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.setWindowTitle("PyQt5 Checkboxes Example")
        self.setGeometry(700, 400, 500, 500)
        self.checkbox1 = QCheckBox("Do You Like Ice Cream?", self)  # Create a QCheckBox with the label "Do You Like Ice Cream?"
        self.checkbox2 = QCheckBox("Do You Like Chocolate?", self)  # Create a QCheckBox with the label "Do You Like Chocolate?"
        self.initUI()

    def initUI(self):
        
        self.checkbox1.setGeometry(50, 50, 200, 30)  # Set the position and size of the first checkbox
        self.checkbox2.setGeometry(50, 100, 200, 30)  # Set the position and size of the second checkbox   
        self.checkbox1.setStyleSheet("font-size: 16px;"
                                     "font-family: Arial;")  # Set the style of the first checkbox
        self.checkbox2.setStyleSheet("font-size: 16px;"
                                     "font-family: Arial;")  # Set the style of the second checkbox

        # To make the checkbox checked by default.
        # self.checkbox1.setChecked(True)  # Set the first checkbox to be checked by default
        self.checkbox1.setChecked(False)  # Set the first checkbox to be unchecked by default
        self.checkbox2.setChecked(False)  # Set the second checkbox to be unchecked by default
        
        self.checkbox1.stateChanged.connect(self.checkbox_state_changed)  # Connect the stateChanged signal of the first checkbox to the checkbox_state_changed method
        self.checkbox2.stateChanged.connect(self.checkbox_state_changed)  # Connect the stateChanged signal of the second checkbox to the checkbox_state_changed method

# checkbox.*signal.*connect(*slot*) is used to connect a signal emitted by the checkbox (like stateChanged) to a slot (a method that will be called when the signal is emitted).
    def checkbox_state_changed(self, state):

        # It shows the value of 2 when the checkbox is checked and 0 when it is unchecked.
        # This is because the stateChanged signal emits an integer value representing the state of the checkbox (2 for checked, 0 for unchecked, and 1 for partially checked).
        # Same thing can be showed by Qt.checked which is more readable and easier to understand.

        if state == Qt.Checked:  # Check if the checkbox is checked
            print("Checkbox is checked!")  # Print a message to the console when the checkbox is checked
        else:
            print("Checkbox is unchecked!")  # Print a message to the console when the checkbox is unchecked

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())   

if __name__ == "__main__":
    main()
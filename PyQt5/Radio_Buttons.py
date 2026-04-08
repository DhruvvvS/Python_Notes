# Radio Buttons 

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QButtonGroup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Radio Buttons Example")
        self.setGeometry(700, 400, 500, 500)
        self.radio1 = QRadioButton("Visa", self)  # Create a QRadioButton with the label "Visa"
        self.radio2 = QRadioButton("Mastercard", self)  # Create a QRadioButton with the label "Mastercard"
        self.radio3 = QRadioButton("Gift Card", self)  # Create a QRadioButton with the label "Gift Card"
        self.radio4 = QRadioButton("In Store", self)  # Create a QRadioButton with the label "In Store"
        self.radio5 = QRadioButton("Online", self)  # Create a QRadioButton with the label "Online"

        self.button_group1 = QButtonGroup(self)  # Create a QButtonGroup to group the radio buttons together
        self.button_group2 = QButtonGroup(self)  # Create another QButtonGroup to group the radio buttons together  
        self.initUI()

    def initUI(self):
        
        self.radio1.setGeometry(50, 50, 200, 30)  # Set the position and size of the first radio button
        self.radio2.setGeometry(50, 100, 200, 30)  # Set the position and size of the second radio button
        self.radio3.setGeometry(50, 150, 200, 30)  # Set the position and size of the third radio button
        self.radio4.setGeometry(50, 200, 200, 30)  # Set the position and size of the fourth radio button
        self.radio5.setGeometry(50, 250, 200, 30)  # Set the position and size of the fifth radio button
        
        self.setStyleSheet("QRadioButton{font-size: 16px; font-family: Arial;}")  # Set the style of the all radio button
        
        # To make the radio button checked by default.
        # self.radio1.setChecked(True)  # Set the first radio button to be checked by default
        self.radio1.setChecked(False)  # Set the first radio button to be unchecked by default
        self.radio2.setChecked(False)  # Set the second radio button to be unchecked by default

        # Create a QButtonGroup to group the radio buttons together
        self.button_group = QButtonGroup(self)
        self.button_group1.addButton(self.radio1)  # Add the first radio button to the button group 1
        self.button_group1.addButton(self.radio2)  # Add the second radio button to the button group 1
        self.button_group1.addButton(self.radio3)  # Add the third radio button to the button group 1
        self.button_group2.addButton(self.radio4)  # Add the fourth radio button to the button group 2
        self.button_group2.addButton(self.radio5)  # Add the fifth radio button to the button group 2

        self.button_group1.buttonClicked.connect(self.radio_button_clicked)  # Connect the buttonClicked signal of the button group 1 to the radio_button_clicked method
        self.button_group2.buttonClicked.connect(self.radio_button_clicked)  # Connect the buttonClicked signal of the button group 2 to the radio_button_clicked method    

    def radio_button_clicked(self):
        if self.radio1.isChecked():  # Check if the first radio button is checked
            print("Visa is selected!")  # Print a message to the console when the first radio button is checked
        elif self.radio2.isChecked():  # Check if the second radio button is checked
            print("Mastercard is selected!")  # Print a message to the console when the second radio button is checked
        elif self.radio3.isChecked():  # Check if the third radio button is checked
            print("Gift Card is selected!")  # Print a message to the console when the third radio button is checked
        elif self.radio4.isChecked():  # Check if the fourth radio button is checked
            print("In Store is selected!")  # Print a message to the console when the fourth radio button is checked
        elif self.radio5.isChecked():  # Check if the fifth radio button is checked
            print("Online is selected!")  # Print a message to the console when the fifth radio button is checked

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
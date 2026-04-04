# PyQt5 Images implementation

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# importing QPixmap module to display and handle images in the application
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 Images Example")
        self.setGeometry(700, 400, 500, 500)

        label = QLabel(self)  # Create a QLabel to display the image
        label.setGeometry(0, 0, 300, 300)  # Set the position and size of the label

        pixmap = QPixmap("image_.gif")  # Load the image using QPixmap
        label.setPixmap(pixmap)  # Set the pixmap to the label to display

        label.setScaledContents(True)  # Scale the image to fit the label size

        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                           label.width(), 
                           label.height())  # Center the label in the window
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
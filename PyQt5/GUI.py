# PyQt5 Introduction
# install PyQt5: pip install PyQt5
# import PyQt5 modules

import sys
# sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
from PyQt5.QtWidgets import QApplication, QMainWindow
# QApplication: manages the GUI application's control flow and main settings.
# QMainWindow: provides a main application window with a menu bar, toolbar, and status bar.

from PyQt5.QtGui import QIcon
# QIcon: provides icons for the application, which can be used in various widgets like buttons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI Example")
        # Set the title of the main window to "PyQt5 GUI Example".
        self.setGeometry(700, 400, 400, 300)
        # Set the geometry of the main window with x=700, y=400, width=400, and height=300.
        # Here x and y specify the position of the window on the screen in pixels.
        self.setWindowIcon(QIcon("image_.gif"))
        # Set the window icon using an image file named "image_.gif". Make sure this file is in the same directory as your script or provide the correct path.

def main():
    app = QApplication(sys.argv)
    # sys.argv is a list of command-line arguments passed to the script. The first argument is the script name itself.
    # Create an instance of the application

    window = MainWindow()
    # Create an instance of the main window

    window.show()
    # Show the main window but only for a brief second, as we will immediately start the event loop.

    sys.exit(app.exec_())
    # Start the application's event loop and .exec_() is a method that starts the event loop and waits for events to occur.

if __name__ == "__main__":
    main()

# This is it for GUI dev next hop to labels file to learn how to add labels to the GUI.
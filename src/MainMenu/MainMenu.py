# Import libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5 import uic
from MainMenu.MainMenuImages import *

class MainMenu(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        
        self.parent = Main
        uic.loadUi("./src/MainMenu/MainMenu.ui", self)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent
    
    def exitEvent(self, event):
        QApplication.quit()

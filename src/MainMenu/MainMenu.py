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

        article_sidebar = self.findChild(QLabel, "label_6")
        article_sidebar.mousePressEvent = self.navigateArticle

        article_image = self.findChild(QLabel, "label_15")
        article_image.mousePressEvent = self.navigateArticle

        article_menu = self.findChild(QLabel, "label_20")
        article_menu.mousePressEvent = self.navigateArticle

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent
    
    def navigateArticle(self, event):
        self.parent.stackedWidget.setCurrentIndex(3)

    def exitEvent(self, event):
        QApplication.quit()
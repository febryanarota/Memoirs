# Import libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QDate
from PyQt5 import uic
from MainMenu.MainMenuImages import *

class MainMenu(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        
        self.parent = Main
        uic.loadUi("./src/MainMenu/MainMenu.ui", self)

        todolist_sidebar = self.findChild(QLabel, "label")
        todolist_sidebar.mousePressEvent = self.navigateToDoList

        todolist_image = self.findChild(QLabel, "label_11")
        todolist_image.mousePressEvent = self.navigateToDoList
        
        harian_sidebar = self.findChild(QLabel, "label_5")
        harian_sidebar.mousePressEvent = self.navigateHarian

        harian_image = self.findChild(QLabel, "label_12")
        harian_image.mousePressEvent = self.navigateHarian

        harian_menu = self.findChild(QLabel, "label_17")
        harian_menu.mousePressEvent = self.navigateHarian

        target_sidebar = self.findChild(QLabel, "label_4")
        target_sidebar.mousePressEvent = self.navigateTarget

        target_image = self.findChild(QLabel, "label_13")
        target_image.mousePressEvent = self.navigateTarget

        target_menu = self.findChild(QLabel, "label_18")
        target_menu.mousePressEvent = self.navigateTarget

        syukur_sidebar = self.findChild(QLabel, "label_8")
        syukur_sidebar.mousePressEvent = self.navigateSyukur

        syukur_image = self.findChild(QLabel, "label_14")
        syukur_image.mousePressEvent = self.navigateSyukur

        syukur_menu = self.findChild(QLabel, "label_19")
        syukur_menu.mousePressEvent = self.navigateSyukur

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
    
    def navigateToDoList(self, event):
        self.parent.stackedWidget.setCurrentIndex(5)

    def navigateSyukur(self, event):
        self.parent.stackedWidget.setCurrentIndex(7)

    def navigateTarget(self, event):
        self.parent.stackedWidget.setCurrentIndex(9)

    def navigateHarian(self, event):
        self.parent.stackedWidget.widget(13).calendar.setSelectedDate(QDate())
        self.parent.stackedWidget.setCurrentIndex(13)

    def exitEvent(self, event):
        QApplication.quit()

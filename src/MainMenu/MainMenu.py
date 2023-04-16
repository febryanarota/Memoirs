# Import libraries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QGraphicsDropShadowEffect
from PyQt5.QtCore import QDate
from PyQt5 import uic
sys.path.append('./src/MainMenu')

class MainMenu(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()

        # Set parent with main
        self.parent = Main
        
        # Load UI
        uic.loadUi("./src/MainMenu/MainMenu.ui", self)

        # Bind sidebar labels, images, and text labels with navigations
        self.todolist_sidebar = self.findChild(QLabel, "label")
        self.todolist_sidebar.mousePressEvent = self.navigateToDoList

        self.todolist_image = self.findChild(QLabel, "label_11")
        self.todolist_image.mousePressEvent = self.navigateToDoList

        self.todolist_menu = self.findChild(QLabel, "label_16")
        self.todolist_menu.mousePressEvent = self.navigateToDoList

        self.harian_sidebar = self.findChild(QLabel, "label_5")
        self.harian_sidebar.mousePressEvent = self.navigateHarian

        self.harian_image = self.findChild(QLabel, "label_12")
        self.harian_image.mousePressEvent = self.navigateHarian

        self.harian_menu = self.findChild(QLabel, "label_17")
        self.harian_menu.mousePressEvent = self.navigateHarian

        self.target_sidebar = self.findChild(QLabel, "label_4")
        self.target_sidebar.mousePressEvent = self.navigateTarget

        self.target_image = self.findChild(QLabel, "label_13")
        self.target_image.mousePressEvent = self.navigateTarget

        self.target_menu = self.findChild(QLabel, "label_18")
        self.target_menu.mousePressEvent = self.navigateTarget

        self.syukur_sidebar = self.findChild(QLabel, "label_8")
        self.syukur_sidebar.mousePressEvent = self.navigateSyukur

        self.syukur_image = self.findChild(QLabel, "label_14")
        self.syukur_image.mousePressEvent = self.navigateSyukur

        self.syukur_menu = self.findChild(QLabel, "label_19")
        self.syukur_menu.mousePressEvent = self.navigateSyukur

        self.article_sidebar = self.findChild(QLabel, "label_6")
        self.article_sidebar.mousePressEvent = self.navigateArticle

        self.article_image = self.findChild(QLabel, "label_15")
        self.article_image.mousePressEvent = self.navigateArticle

        self.article_menu = self.findChild(QLabel, "label_20")
        self.article_menu.mousePressEvent = self.navigateArticle

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        # Styling frame with drop shadow effect
        self.frame2 = self.findChild(QFrame, "frame_2")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setOffset(4,4)
        self.frame2.setGraphicsEffect(shadow)

    def navigateArticle(self, event):
        # Navigate to page article
        self.parent.stackedWidget.setCurrentIndex(3)

    def navigateToDoList(self, event):
        # Navigate to page calendar to do list
        self.parent.stackedWidget.setCurrentIndex(5)

    def navigateSyukur(self, event):
        # Navigate to page syukur
        self.parent.stackedWidget.setCurrentIndex(7)

    def navigateTarget(self, event):
        # Navigate to page target
        self.parent.stackedWidget.setCurrentIndex(9)

    def navigateHarian(self, event):
        # Navigate to page calendar harian
        self.parent.stackedWidget.widget(13).calendar.setSelectedDate(QDate())
        self.parent.stackedWidget.setCurrentIndex(13)

    def exitEvent(self, event):
        # Exit Application
        QApplication.quit()

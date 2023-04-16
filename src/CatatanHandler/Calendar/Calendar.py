# Import libraries
from PyQt5.QtWidgets import QCalendarWidget, QApplication, QMainWindow, QLabel, QPushButton, QToolButton
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from CatatanHandler.Calendar.CalendarImages import *
from CatatanHandler.CatatanHarian.Boundary.HarianDisplay import *

# Class Calendar
class Calendar(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showCalendar()

    def showCalendar(self):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/Calendar/Calendar.ui", self)

        # Sidebar
        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        todolist_sidebar = self.findChild(QLabel, "label")
        todolist_sidebar.mousePressEvent = self.navigateToDoList

        harian_sidebar = self.findChild(QLabel, "label_5")
        harian_sidebar.mousePressEvent = self.navigateHarian

        target_sidebar = self.findChild(QLabel, "label_4")
        target_sidebar.mousePressEvent = self.navigateTarget

        syukur_sidebar = self.findChild(QLabel, "label_8")
        syukur_sidebar.mousePressEvent = self.navigateSyukur

        article_sidebar = self.findChild(QLabel, "label_6")
        article_sidebar.mousePressEvent = self.navigateArticle

        # Calendar Widget
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.calendar.setSelectedDate(QDate.currentDate())
        self.calendar.clicked.connect(self.chooseDate)

        # Navigation Buttons
        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        # Back Button
        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        # Exit Button
        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        # Prev Month Button
        self.prev_month = self.findChild(QToolButton, "qt_calendar_prevmonth")
        self.prev_month.setIcon(QIcon("./img/prev_icon.png"))

        # Next Month Button
        self.next_month = self.findChild(QToolButton, "qt_calendar_nextmonth")
        self.next_month.setIcon(QIcon("./img/next_icon.png"))

    def chooseDate(self, date):
        # Select date and navigate to notes page
        self.parent.stackedWidget.insertWidget(11, HarianDisplay(self.parent, date.toString("d/M/yyyy")))
        self.parent.stackedWidget.setCurrentIndex(11)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(12))

    def back(self, event):
        # Go back to main menu
        self.parent.stackedWidget.setCurrentIndex(2)

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
        # Exit application
        QApplication.quit()

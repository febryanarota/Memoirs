# Import libraries
from PyQt5.QtWidgets import QCalendarWidget, QApplication, QMainWindow, QLabel, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import QDate
from CatatanHandler.ToDoList.Boundary.TDLDisplay import *
from CatatanHandler.ToDoList.Boundary.FormTDL import *
from CatatanHandler.Calendar.CalendarImages import *

# Class Register
class CalendarToDo(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showCalendar()

    def showCalendar(self):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/Calendar/Calendar.ui", self)

        # Calendar Widget
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.calendar.setSelectedDate(QDate.fromString(datetime.now().strftime("%d/%m/%Y")))
        self.calendar.setSelectedDate(QDate())
        self.calendar.clicked.connect(self.chooseDate)

        self.calendar.setStyleSheet('''
            qt_calendar_nextmonth{
                background-image: url(./images/next_icon.png);
                background-repeat: no-repeat;
                width: 5px;
                height: 5px;
            }

            qt_calendar_prevmonth{
                qproperty-icon:"./images/prev_icon.png";
                qproperty-iconSize:10px;
            }
        ''')

        # Navigation Buttons
        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        # Back Button
        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        # Exit Button
        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

    def chooseDate(self, date):
        # Select date and navigate to notes page
        choosen_date = date.toString("dd/MM/yyyy")
        self.parent.date = choosen_date
        self.parent.stackedWidget.insertWidget(5, TDLDisplay(self.parent, choosen_date))
        self.parent.stackedWidget.setCurrentIndex(5)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(6))
    
    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(2)

    def exitEvent(self, event):
        QApplication.quit()
# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from CatatanHandler.ToDoList.Boundary.TDLDisplay import *
from CatatanHandler.ToDoList.Boundary.FormTDL import *
from CatatanHandler.ToDoList.Entity.ToDoList import *
from functools import partial
from CatatanHandler.ToDoList.Controller.TDLController import *
from datetime import datetime

# Class ToDoListDisplay
class TDLDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        today = datetime.now().strftime("%H-%M-%S")
        self.showTDLDisplay(today)

    def showTDLDisplay(self, tanggal):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/ToDoList/Boundary/TDLDisplay.ui", self)
        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.add_button = self.findChild(QPushButton, "pushButton_2")
        self.add_button.clicked.connect(self.showFormTDL)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
        self.scrollArea.verticalScrollBar().setStyleSheet(
        """
        QScrollBar:vertical {
            min-height: 240px;
            width: 13px;
        }

        QScrollBar::handle {
            background: #1C1D22;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical {
            height: 30px;
            width: 5px;
        }
        """)

        today = datetime.now().strftime("%H-%M-%S")
        ListToDo = TDLController().showTDL(today)
        for i in ListToDo:
            print(i[0])

            
        

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(2)
        
    def exitEvent(self, event):
        QApplication.quit()
    
    def showFormTDL(self, event):
        # second_window = FormTDL(self)
        self.parent.stackedWidget.setCurrentIndex(6)
        


# Import libraries
from PyQt5.QtWidgets import QTextEdit, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from functools import partial
from CatatanHandler.ToDoList.Controller.TDLController import *
from CatatanHandler.ToDoList.Boundary.TDLDisplay import *
from CatatanHandler.ToDoList.Boundary.FormTDL import *
from datetime import datetime

class FormTDL(QMainWindow):
    def __init__(self, Main, date):
        super().__init__()
        self.parent = Main
        self.tanggal = date
        self.showFormTDL(self.tanggal)

    def showFormTDL(self, tanggal):
        uic.loadUi("./src/CatatanHandler/ToDoList/Boundary/FORMTDL.ui", self)
        self.inputbox = self.findChild(QLineEdit, "lineEdit")
        self.inputbox.setPlaceholderText("insert your task here...")

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.back)

        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.add)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent
        

        self.date = self.findChild(QLabel, "label_3")
        if(self.parent.editMode):
            self.date.setText(self.parent.date)
        else:
            self.date.setText(datetime.now().strftime("%d/%m/%Y"))


    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(5)
    
    def exitEvent(self, event):
        QApplication.quit()

    def add(self, event):
        task = self.inputbox.text()
        TDLController().addTDL(task, self.tanggal)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(5))
        self.parent.stackedWidget.insertWidget(5, TDLDisplay(self.parent, self.tanggal))
        self.parent.stackedWidget.setCurrentIndex(5)

        # remove the widget
        # self.parent.stackedWidget.removeWidget(widget_to_remove)

        # # create a new widget
        # new_widget = TDLDisplay(self.parent, self.tanggal)

        # add the new widget at the same index
        # self.parent.stackedWidget.insertWidget(5, TDLDisplay(self.parent, self.tanggal))
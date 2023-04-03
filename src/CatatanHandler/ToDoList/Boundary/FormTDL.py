# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from CatatanHandler.ToDoList.Boundary.TDLDisplay import *
from functools import partial
from CatatanHandler.ToDoList.Controller.TDLController import *
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

        self.TDLController = TDLController()
        self.listTDL = self.TDLController.showTDL(tanggal)


    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(5)
    
    def exitEvent(self, event):
        QApplication.quit()

    def add(self, event):
        task = self.inputbox.text()
        temp = TDLController().addTDL(task,self.tanggal)
        # get the widget at index 5
        # widget_to_remove = self.parent.stackedWidget.widget(5)
        self.parent.stackedWidget.setCurrentIndex(5)

        # remove the widget
        # self.parent.stackedWidget.removeWidget(widget_to_remove)

        # # create a new widget
        # new_widget = TDLDisplay(self.parent, self.tanggal)

        # add the new widget at the same index
        # self.parent.stackedWidget.insertWidget(5, TDLDisplay(self.parent, self.tanggal))
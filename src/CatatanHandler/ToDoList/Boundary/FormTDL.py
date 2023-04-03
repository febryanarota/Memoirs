# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from CatatanHandler.ToDoList.Boundary.TDLDisplay import *
from CatatanHandler.ToDoList.Boundary.FormTDL import *
from functools import partial
from CatatanHandler.ToDoList.Controller.TDLController import *
from datetime import datetime

class FormTDL(QMainWindow):
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showFormTDL()

    def showFormTDL(self):
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

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(5)
    
    def exitEvent(self, event):
        QApplication.quit()

    def add(self, event):
        task = self.inputbox.text()
        today = datetime.now().strftime("%H-%M-%S")
        TDLController().addTDL(task, today)
        self.parent.stackedWidget.setCurrentIndex(5)
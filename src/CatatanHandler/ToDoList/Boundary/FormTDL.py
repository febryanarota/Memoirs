# Import libraries
from PyQt5.QtWidgets import QTextEdit, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from functools import partial
from CatatanHandler.ToDoList.Controller.TDLController import *
from CatatanHandler.ToDoList.Boundary.TDLDisplay import *
from CatatanHandler.ToDoList.Boundary.FormTDL import *
from CatatanHandler.ToDoList.Boundary.todolist import *
from datetime import datetime

class FormTDL(QMainWindow):
    def __init__(self, Main, tanggal = datetime.now().strftime("%d/%m/%Y")):
        super().__init__()
        self.formDate = tanggal
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
        
        self.date = self.findChild(QLabel, "label_3")
        self.date.setText(self.formDate)

    def add(self, event):
        task = self.inputbox.text()
        TDLController().addTDL(task, self.date.text())
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(5))
        self.parent.stackedWidget.insertWidget(5,TDLDisplay(self.parent, self.date.text()))
        self.parent.stackedWidget.setCurrentIndex(5)

    def edit(self):
        to_do = self.inputbox.text()
        tanggal = self.date.text()
        done = self.parent.todo_list_lama.getDone()
        TDLController().editTDL(self.parent.todo_list_lama, to_do, tanggal, done)

        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(5))
        self.parent.stackedWidget.insertWidget(5,TDLDisplay(self.parent, self.date.text()))
        self.parent.stackedWidget.setCurrentIndex(5)

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(5)
    
    def exitEvent(self, event):
        QApplication.quit()
# Import libraries
from PyQt5.QtWidgets import QTextEdit, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QDate
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

        self.inputbox = self.findChild(QLineEdit, "lineEdit")
        self.inputbox.setPlaceholderText("insert your task here...")

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.back)

        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.confirm)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent
        
        self.date = self.findChild(QLabel, "label_3")
        self.date.setText(self.formDate)

    def confirm(self, event):
        if(self.parent.editMode):
            self.edit()
        else:
            self.add(event)

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
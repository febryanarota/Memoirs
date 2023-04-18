# Import libraries
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIcon
from CatatanHandler.ToDoList.Controller.TDLController import TDLController
from CatatanHandler.ToDoList.Boundary.TDLDisplay import TDLDisplay
from CatatanHandler.ToDoList.Boundary.todolist import *
from datetime import datetime

class FormTDL(QMainWindow):
    def __init__(self, Main, tanggal = datetime.now().strftime("%d/%m/%Y")):
        super().__init__()

        # Set form date
        self.formDate = tanggal

        # Set parent with Main
        self.parent = Main

        # Show Form TDL
        self.showFormTDL()

    def showFormTDL(self):
        # Load UI
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

        # Inputs and buttons
        self.inputbox = self.findChild(QLineEdit, "lineEdit")
        self.inputbox.setPlaceholderText("insert your task here...")

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.navigateToDoList)

        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.navigateToDoList)

        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.confirm)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent
        
        self.date = self.findChild(QLabel, "label_3")
        self.date.setText(self.formDate)

    def confirm(self, event):
        # Choose confirm type (add or edit)
        if(self.parent.editMode):
            self.edit()
        else:
            self.add(event)

    def add(self, event):
        # Getting all input data from form
        task = self.inputbox.text()
        tanggal = self.date.text()

        if task == "":
            # Show warning message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("To Do cannot be empty.")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QIcon("./img/M.png"))
            msg.exec_()
        else:
            # Getting list of all to do list on the form date
            ListOfTDL = TDLController().showTDL(tanggal)

            # Check if to do list already exist or not
            checkValid = True

            # Iterate all To Do List
            for el in ListOfTDL:
                if(el.getTanggal() == tanggal and el.getToDo() == task):
                    # If to do list exists
                    checkValid = False
                    break

            if checkValid:
                # Create new to do list
                TDLController().addTDL(task, self.date.text())

                # Remove old page and create new page with new data
                self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(5))
                self.parent.stackedWidget.insertWidget(5,TDLDisplay(self.parent, self.date.text()))
                self.parent.stackedWidget.setCurrentIndex(5)
            else:
                # Show warning message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("To Do has already been recorded.")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QIcon("./img/M.png"))
                msg.exec_()

    def edit(self):
        # Getting all input data from form
        to_do = self.inputbox.text()
        tanggal = self.date.text()
        done = self.parent.todo_list_lama.getDone()

        if to_do == "":
            # Show warning message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("To Do cannot be empty.")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QIcon("./img/M.png"))
            msg.exec_()
        else:
            # Getting list of all to do list on the form date
            ListOfTDL = TDLController().showTDL(tanggal)

            # Check if to do list already exist or not
            checkValid = True

            # Iterate all To Do List
            for el in ListOfTDL:
                if(el.getTanggal() == tanggal and el.getToDo() == to_do):
                    # If to do list exists
                    checkValid = False
                    break

            if checkValid:
                # Edit existing to do list
                TDLController().editTDL(self.parent.todo_list_lama, to_do, tanggal, done)
                
                # Remove old page and create new page with new data
                self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(5))
                self.parent.stackedWidget.insertWidget(5,TDLDisplay(self.parent, self.date.text()))
                self.parent.stackedWidget.setCurrentIndex(5)
            else:
                # Show warning message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("To Do has already been recorded.")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QIcon("./img/M.png"))
                msg.exec_()

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
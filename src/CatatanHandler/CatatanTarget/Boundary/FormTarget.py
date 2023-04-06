# Import libraries
from PyQt5.QtWidgets import QDateEdit, QTextEdit, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLineEdit
from PyQt5 import uic
from CatatanHandler.CatatanTarget.Boundary.TargetDisplay import *
from CatatanHandler.CatatanTarget.Boundary.TargetImages import *
from CatatanHandler.CatatanTarget.Controller.TargetController import *
from datetime import datetime

class FormTarget(QMainWindow):
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showFormTarget()

    def showFormTarget(self):
        uic.loadUi("./src/CatatanHandler/CatatanTarget/Boundary/FormTarget.ui", self)

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.back)

        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.submit)

        self.text_edit = self.findChild(QTextEdit, "textEdit")

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        self.date = self.findChild(QLabel, "label_3")
        if(self.parent.editMode):
            self.date.setText(self.parent.date)
        else:
            self.date.setText(datetime.now().strftime("%d/%m/%Y"))
        
        self.edit_date = self.findChild(QDateEdit, "dateEdit")

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(9)
    
    def exitEvent(self, event):
        QApplication.quit()

    def submit(self, event):
        if(self.parent.editMode):
            self.edit()
        else:
            self.add()
    
    def add(self):
        target = self.text_edit.toPlainText()
        self.text_edit.setText("")
        tanggal = self.edit_date.date().toString("d/M/yyyy")
        TargetController().addTarget(target, tanggal)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(9))
        self.parent.stackedWidget.insertWidget(9, TargetDisplay(self.parent))
        self.parent.stackedWidget.setCurrentIndex(9)

    def edit(self):
        target = self.text_edit.toPlainText()
        self.text_edit.setText("")
        tanggal = self.edit_date.date().toString("d/M/yyyy")
        TargetController().editTarget(CatatanTarget(self.parent.targetLama, self.parent.date), target, tanggal)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(9))
        self.parent.stackedWidget.insertWidget(9, TargetDisplay(self.parent))
        self.parent.stackedWidget.setCurrentIndex(9)
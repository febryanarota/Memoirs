# Import libraries
from PyQt5.QtWidgets import QTextEdit, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLineEdit
from PyQt5 import uic
from CatatanHandler.CatatanSyukur.Boundary.SyukurDisplay import *
from CatatanHandler.CatatanSyukur.Boundary.SyukurImages import *
from CatatanHandler.CatatanSyukur.Controller.SyukurController import *
from datetime import datetime

class FormSyukur(QMainWindow):
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showFormSyukur()

    def showFormSyukur(self):
        uic.loadUi("./src/CatatanHandler/CatatanSyukur/Boundary/FormSyukur.ui", self)

        # Back Button
        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)
        
        # Cancel Button
        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.back)

        # Save Button
        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.submit)

        # Text Editor
        self.text_edit = self.findChild(QTextEdit, "textEdit")

        # Exit Button
        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        # Date Label
        self.date = self.findChild(QLabel, "label_3")
        if(self.parent.editMode):
            self.date.setText(self.parent.date)
        else:
            self.date.setText(datetime.now().strftime("%d/%m/%Y"))

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(7)
    
    def exitEvent(self, event):
        QApplication.quit()

    def submit(self, event):
        # Edit mode or add mode
        if(self.parent.editMode):
            self.edit()
        else:
            self.add()
    
    def add(self):
        # Getting all inputs
        syukur = self.text_edit.toPlainText()
        self.text_edit.setText("")
        today = datetime.now().strftime("%d/%m/%Y")

        # Add new note
        SyukurController().addSyukur(syukur, today)

        # Destroy old widget and create new widget
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(7))
        self.parent.stackedWidget.insertWidget(7, SyukurDisplay(self.parent))
        self.parent.stackedWidget.setCurrentIndex(7)

    def edit(self):
        # Getting all inputs
        syukur = self.text_edit.toPlainText()
        self.text_edit.setText("")

        # Edit new note
        SyukurController().editSyukur(self.parent.syukurLama, syukur, self.parent.date)

        # Destroy old widget and create new widget
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(7))
        self.parent.stackedWidget.insertWidget(7, SyukurDisplay(self.parent))
        self.parent.stackedWidget.setCurrentIndex(7)
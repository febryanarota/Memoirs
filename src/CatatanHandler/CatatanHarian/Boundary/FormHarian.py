# Import libraries
from PyQt5.QtWidgets import QTimeEdit, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5 import uic
from CatatanHandler.CatatanHarian.Boundary.HarianDisplay import *
from CatatanHandler.CatatanHarian.Boundary.HarianImages import *
from CatatanHandler.CatatanHarian.Controller.HarianController import *
from datetime import datetime

class FormHarian(QMainWindow):
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showFormHarian()

    def showFormHarian(self):
        uic.loadUi("./src/CatatanHandler/CatatanHarian/Boundary/FormHarian.ui", self)

        # Back Button
        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        # Cancel Button
        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.back)

        # Save Button
        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.submit)

        # Line Edit
        self.line_edit = self.findChild(QLineEdit, "lineEdit")

        # Time Edit
        self.jam_mulai_edit = self.findChild(QTimeEdit, 'timeEdit_2')
        self.jam_berakhir_edit = self.findChild(QTimeEdit, 'timeEdit')

        # Exit Button
        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        # Date
        self.date = self.findChild(QLabel, "label_3")
        if(self.parent.editMode):
            self.date.setText(self.parent.date)
        else:
            self.date.setText(datetime.now().strftime("%d/%m/%Y"))

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(11)
    
    def exitEvent(self, event):
        QApplication.quit()

    def submit(self, event):
        if(self.parent.editMode):
            self.edit()
        else:
            self.add()
    
    def add(self):
        # Getting all input data from form
        harian = self.line_edit.text()
        self.line_edit.setText("")
        tanggal = self.date.text()
        jam_mulai = self.jam_mulai_edit.time().toString("hh.mm")
        jam_berakhir = self.jam_berakhir_edit.time().toString("hh.mm")

        # Create new note
        HarianController().addHarian(jam_mulai, jam_berakhir, harian, tanggal)

        # Remove old widget and create new widget with new data
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(11))
        self.parent.stackedWidget.insertWidget(11, HarianDisplay(self.parent, self.date.text()))
        self.parent.stackedWidget.setCurrentIndex(11)

    def edit(self):
        # Getting all input data from form
        harian = self.line_edit.text()
        self.line_edit.setText("")
        tanggal = self.date.text()
        jam_mulai = self.jam_mulai_edit.time().toString("hh.mm")
        jam_berakhir = self.jam_berakhir_edit.time().toString("hh.mm")

        # Edit old note
        HarianController().editHarian(self.parent.harian_lama, jam_mulai, jam_berakhir, harian, tanggal)

        # Remove old widget and create new widget with new data
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(11))
        self.parent.stackedWidget.insertWidget(11, HarianDisplay(self.parent, self.date.text()))
        self.parent.stackedWidget.setCurrentIndex(11)
# Import libraries
from PyQt5.QtWidgets import QTimeEdit, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QGraphicsDropShadowEffect, QMessageBox, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from CatatanHandler.CatatanHarian.Boundary.HarianDisplay import HarianDisplay
from CatatanHandler.CatatanHarian.Boundary.HarianImages import *
from CatatanHandler.CatatanHarian.Controller.HarianController import HarianController
from datetime import datetime

class FormHarian(QMainWindow):
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showFormHarian()

    def showFormHarian(self):
        uic.loadUi("./src/CatatanHandler/CatatanHarian/Boundary/FormHarian.ui", self)

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

        # Shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setOffset(4,4)

        # Back Button
        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.navigateHarianDisplay)
        self.back_button.setGraphicsEffect(shadow)

        # Cancel Button
        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.navigateHarianDisplay)
        self.cancel_button.setGraphicsEffect(shadow)

        # Save Button
        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.submit)
        self.save_button.setGraphicsEffect(shadow)

        # Line Edit
        self.line_edit = self.findChild(QLineEdit, "lineEdit")
        self.line_edit.setGraphicsEffect(shadow)

        # Time Edit
        self.jam_mulai_edit = self.findChild(QTimeEdit, 'timeEdit_2')
        self.jam_berakhir_edit = self.findChild(QTimeEdit, 'timeEdit')
        self.jam_mulai_edit.setGraphicsEffect(shadow)
        self.jam_berakhir_edit.setGraphicsEffect(shadow)

        # Exit Button
        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        # Date
        self.date = self.findChild(QLabel, "label_3")
        if(self.parent.editMode):
            self.date.setText(self.parent.date)
        else:
            self.date.setText(datetime.now().strftime("%d/%m/%Y"))

        # Main Widget
        self.widget = self.findChild(QWidget, "widget")
        self.widget.setGraphicsEffect(shadow)

    def back(self, event):
        # Go back to main menu
        self.parent.stackedWidget.setCurrentIndex(2)
    
    def exitEvent(self, event):
        # Exit application
        QApplication.quit()

    def submit(self, event):
        # Select submit method (edit or add)
        if(self.parent.editMode):
            self.edit()
        else:
            self.add()
    
    def add(self):
        # Getting all input data from form
        harian = self.line_edit.text()
        tanggal = self.date.text()
        jam_mulai = self.jam_mulai_edit.time().toString("hh.mm")
        jam_berakhir = self.jam_berakhir_edit.time().toString("hh.mm")

        if harian == "":
            # Show warning message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Harian cannot be empty.")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QIcon("./img/M.png"))
            msg.exec_()
        else:
            # Getting list of all catatan harian on the input date
            ListOfHarian = HarianController().showHarian(tanggal)

            # Check if jadwal already exist or not
            checkValid = True

            # Iterate all catatan harian
            for el in ListOfHarian:
                if(el.getTanggal() == tanggal and el.getKegiatan() == harian and el.getJamMulai() == jam_mulai and el.getJamBerakhir() == jam_berakhir):
                    # If jadwal exists
                    checkValid = False
                    break

            if checkValid:
                # Create new note
                HarianController().addHarian(jam_mulai, jam_berakhir, harian, tanggal)

                # Remove old widget and create new widget with new data
                self.line_edit.setText("")
                self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(11))
                self.parent.stackedWidget.insertWidget(11, HarianDisplay(self.parent, self.date.text()))
                self.parent.stackedWidget.setCurrentIndex(11)
            else:
                # Show warning message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Harian has already been recorded.")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QIcon("./img/M.png"))
                msg.exec_()

    def edit(self):
        # Getting all input data from form
        harian = self.line_edit.text()
        tanggal = self.date.text()
        jam_mulai = self.jam_mulai_edit.time().toString("hh.mm")
        jam_berakhir = self.jam_berakhir_edit.time().toString("hh.mm")

        if harian == "":
            # Show warning message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Harian cannot be empty.")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QIcon("./img/M.png"))
            msg.exec_()
        else:
            # Getting list of all catatan harian on the input date
            ListOfHarian = HarianController().showHarian(tanggal)

            # Check if jadwal already exist or not
            checkValid = True

            # Iterate all catatan harian
            for el in ListOfHarian:
                if(el.getTanggal() == tanggal and el.getKegiatan() == harian and el.getJamMulai() == jam_mulai and el.getJamBerakhir() == jam_berakhir):
                    # If jadwal exists
                    checkValid = False
                    break

            if checkValid:
                # Reset text
                self.line_edit.setText("")

                # Edit old note
                HarianController().editHarian(self.parent.harian_lama, jam_mulai, jam_berakhir, harian, tanggal)

                # Remove old page and create new page with new data
                self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(11))
                self.parent.stackedWidget.insertWidget(11, HarianDisplay(self.parent, self.date.text()))
                self.parent.stackedWidget.setCurrentIndex(11)
            else:
                # Show warning message
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Harian has already been recorded.")
                msg.setWindowTitle("Warning")
                msg.setWindowIcon(QIcon("./img/M.png"))
                msg.exec_()
    
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
        self.parent.stackedWidget.setCurrentIndex(13)
    
    def navigateHarianDisplay(self, event):
        # Navigate to page harian
        self.parent.stackedWidget.setCurrentIndex(11)

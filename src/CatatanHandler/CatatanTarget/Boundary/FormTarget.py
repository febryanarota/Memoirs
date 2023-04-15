# Import libraries
from PyQt5.QtWidgets import QDateEdit, QTextEdit, QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QGraphicsDropShadowEffect, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from CatatanHandler.CatatanTarget.Boundary.TargetDisplay import TargetDisplay
from CatatanHandler.CatatanTarget.Boundary.TargetImages import *
from CatatanHandler.CatatanTarget.Controller.TargetController import TargetController
from datetime import datetime

class FormTarget(QMainWindow):
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showFormTarget()

    def showFormTarget(self):
        uic.loadUi("./src/CatatanHandler/CatatanTarget/Boundary/FormTarget.ui", self)

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
        
        # Buttons and inputs
        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.navigateTarget)
        self.back_button.setGraphicsEffect(shadow)

        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.navigateTarget)
        self.cancel_button.setGraphicsEffect(shadow)

        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.submit)
        self.save_button.setGraphicsEffect(shadow)

        self.text_edit = self.findChild(QTextEdit, "textEdit")
        self.text_edit.setGraphicsEffect(shadow)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        self.date = self.findChild(QLabel, "label_3")
        if(self.parent.editMode):
            self.date.setText(self.parent.date)
        else:
            self.date.setText(datetime.now().strftime("%d/%m/%Y"))

        self.edit_date = self.findChild(QDateEdit, "dateEdit")

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
        # Choose submit type (edit or add)
        if(self.parent.editMode):
            self.edit()
        else:
            self.add()

    def add(self):
        # Getting all inputs
        target = self.text_edit.toPlainText()
        tanggal = self.edit_date.date().toString("d/M/yyyy")

        # Check if input target exists or not
        ListOfTarget = TargetController().showTarget()
        checkValid = True

        # Iterate through all target
        for el in ListOfTarget:
            if(el.getTanggal() == tanggal and el.getTarget() == target):
                # If target exists
                checkValid = False
                break

        if checkValid:
            # Add target
            TargetController().addTarget(target, tanggal)

            # Reset input
            self.text_edit.setText("")

            # Remove old page and create new page with new data
            self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(9))
            self.parent.stackedWidget.insertWidget(9, TargetDisplay(self.parent))
            self.parent.stackedWidget.setCurrentIndex(9)
        else:
            # Show Warning Message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Target has already been recorded.")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QIcon("./images/M.png"))
            msg.exec_()

    def edit(self):
        # Getting all inputs
        target = self.text_edit.toPlainText()
        tanggal = self.edit_date.date().toString("d/M/yyyy")

        # Check if input target exists or not
        ListOfTarget = TargetController().showTarget()
        checkValid = True

        # Iterate through all target
        for el in ListOfTarget:
            if(el.getTanggal() == tanggal and el.getTarget() == target):
                # If target exists
                checkValid = False
                break

        if checkValid:
            # Edit target
            TargetController().editTarget(CatatanTarget(self.parent.targetLama, self.parent.date), target, tanggal)

            # Reset input
            self.text_edit.setText("")

            # Remove old page and create new page with new data
            self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(9))
            self.parent.stackedWidget.insertWidget(9, TargetDisplay(self.parent))
            self.parent.stackedWidget.setCurrentIndex(9)
        else:
            # Show Warning Message
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Target has already been recorded.")
            msg.setWindowTitle("Warning")
            msg.setWindowIcon(QIcon("./images/M.png"))
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
        self.parent.stackedWidget.widget(13).calendar.setSelectedDate(QDate())
        self.parent.stackedWidget.setCurrentIndex(13)

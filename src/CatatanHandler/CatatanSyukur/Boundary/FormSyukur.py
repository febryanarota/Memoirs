# Import libraries
from PyQt5.QtWidgets import QTextEdit, QApplication, QMainWindow, QLabel, QPushButton
from PyQt5 import uic
from PyQt5.QtCore import QDate
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
        self.back_button.clicked.connect(self.back)
        self.back_button.setGraphicsEffect(shadow)
        
        # Cancel Button
        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.back)
        self.cancel_button.setGraphicsEffect(shadow)

        # Save Button
        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.submit)

        # Text Editor
        self.text_edit = self.findChild(QTextEdit, "textEdit")
        self.text_edit.setGraphicsEffect(shadow)

        # Exit Button
        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        # Date Label
        self.date = self.findChild(QLabel, "label_3")
        if(self.parent.editMode):
            self.date.setText(self.parent.date)
        else:
            self.date.setText(datetime.now().strftime("%d/%m/%Y"))

        # Main Widget
        self.widget = self.findChild(QWidget, "widget")
        self.widget.setGraphicsEffect(shadow)
        
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
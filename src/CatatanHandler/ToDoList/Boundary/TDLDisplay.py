# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtCore import Qt
from CatatanHandler.ToDoList.Boundary.FormTDL import *
from CatatanHandler.ToDoList.Entity.ToDoList import *
from functools import partial
from CatatanHandler.ToDoList.Controller.TDLController import *
from datetime import datetime

# Class ToDoListDisplay
class TDLDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main, tanggal):
        super().__init__()
        self.parent = Main
        self.tanggal = tanggal
        self.showTDLDisplay(tanggal)

    def showTDLDisplay(self, tanggal):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/ToDoList/Boundary/TDLDisplay.ui", self)
        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.add_button = self.findChild(QPushButton, "pushButton_2")
        self.add_button.clicked.connect(self.showFormTDL)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
        self.scrollArea.verticalScrollBar().setStyleSheet(
        """
        QScrollBar:vertical {
            min-height: 240px;
            width: 13px;
        }

        QScrollBar::handle {
            background: #1C1D22;
            border-radius: 0px;
        }

        QScrollBar::handle:vertical {
            height: 30px;
            width: 5px;
        }
        """)

        todolistController = TDLController()
        listTodo = todolistController.showTDL(tanggal)
        # Container Widget       
        self.widget = QWidget()
        
        # Layout of Container Widget
        listTDL_box = QVBoxLayout()
        listTDL_box.setSpacing(20)

        for i in range (len(listTodo)):
            TDL_widget = QWidget()
            TDL_widget.setStyleSheet("background-color: white; border-radius: 20px; margin-right: 20px")
            TDL_widget.setMinimumSize(1150, 70)
            TDL_widget.setMaximumSize(1150, 70)

            TDL_box = QHBoxLayout()


            spacer = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)
            TDL_box.addItem(spacer)

            button = QPushButton()
            button.setStyleSheet("margin-right: 20px")
            img = QPixmap("./images/checkBox.png")
            image = img.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            button.setIcon(QIcon(image))
            button.setIconSize(image.size())
            TDL_box.addWidget(button)
            
            TDL_content_widget = QWidget()
            TDL_content = QVBoxLayout()
            to_do = QLabel(listTodo[i].getToDo())
            to_do.setFont(QFont("Poppins", 12, QFont.Bold))

            TDL_content.addWidget(to_do)
            TDL_content_widget.setLayout(TDL_content)

            spacer2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)        
            TDL_box.addWidget(TDL_content_widget)
            TDL_box.addItem(spacer2)

            del_button = QPushButton()
            del_button.setStyleSheet("margin-right: 20px")
            img = QPixmap("./images/delete_btn.png")
            image = img.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            del_button.setIcon(QIcon(image))
            del_button.setIconSize(image.size())
            TDL_box.addWidget(del_button)

            edit_button = QPushButton()
            edit_button.setStyleSheet("margin-right: 20px")
            img = QPixmap("./images/edit_btn.png")
            image = img.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            edit_button.setIcon(QIcon(image))
            edit_button.setIconSize(image.size())
            TDL_box.addWidget(edit_button)



            TDL_widget.setLayout(TDL_box)
            listTDL_box.addWidget(TDL_widget)

        self.widget.setLayout(listTDL_box)
        self.scrollArea.setWidget(self.widget)
            
            
        

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(2)
        
    def exitEvent(self, event):
        QApplication.quit()
    
    def showFormTDL(self, event):
        # second_window = FormTDL(self)
        self.parent.stackedWidget.setCurrentIndex(6)
        


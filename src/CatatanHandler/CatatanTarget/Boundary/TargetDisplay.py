# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QGraphicsDropShadowEffect, QSpacerItem, QDialog
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QDate
from functools import partial
from CatatanHandler.CatatanTarget.Boundary.TargetImages import *
from CatatanHandler.CatatanTarget.Controller.TargetController import TargetController
from datetime import datetime
from CatatanHandler.ConfirmPopUp.ConfirmPopUp import ConfirmPopUp

# Class TargetDisplay
class TargetDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()

        # Set parent to Main
        self.parent = Main

        # Show Target Display
        self.showTargetDisplay()

    def showTargetDisplay(self):
        # Load UI
        uic.loadUi("./src/CatatanHandler/CatatanTarget/Boundary/TargetDisplay.ui", self)

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

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        self.add_button = self.findChild(QPushButton, "pushButton_2")
        self.add_button.setStyleSheet("margin-right: 80px; margin-bottom: 30px;")
        self.add_button.clicked.connect(self.addTarget)

        # Scroll Area
        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
        self.scrollArea.setStyleSheet("border: 0px")
        self.scrollArea.verticalScrollBar().setStyleSheet(
        """
        QScrollBar:vertical {
            min-height: 240px;
            width: 13px;
        }

        QScrollBar::handle {
            background: #1C1D22;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical {
            height: 30px;
            width: 5px;
        }
        """)

        # Getting list of targets
        ListAllTarget = TargetController().showTarget()
        ListAllTarget.sort(key=lambda x: datetime.strptime(x.tanggal, "%d/%m/%Y").date(), reverse=False)

        # Container Widget  
        self.widget = QWidget()

        # Layout of Container Widget
        list_target_box = QVBoxLayout()
        list_target_box.setSpacing(40)
        for i in range(len(ListAllTarget)):
            # Create Main Widget
            target_widget = QWidget()
            target_widget.setObjectName("Outer")
            target_widget.setStyleSheet("""
                #Outer {
                    background-color: white; 
                    border-radius: 20px;
                }
                QWidget {
                    margin-right: 80px;
                }
                QLabel {
                    margin-right: 0px;
                }
                #delete {
                    margin-right: 80px;
                }
            """
            )
            target_widget.setContentsMargins(0,0,0,0)
            target_widget.setMinimumSize(0, 70)
            target_widget.setMaximumHeight(70)
            target_widget.setMaximumWidth(1920)

            # Shadow
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(5)
            shadow.setOffset(4,4)
            target_widget.setGraphicsEffect(shadow)

            # Create Main Layout
            target_box = QHBoxLayout()

            # Create Content
            target_content_widget = QWidget()
            target_content = QHBoxLayout()
            
            # Create Date
            date_target = QLabel(ListAllTarget[i].getTanggal())
            date_target.setFont(QFont("Poppins", 12))
            date_target.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            date_target.setWordWrap(True)

            # Create Delete Button
            label_image = QLabel()
            image = QPixmap("./images/delete_btn.png")
            image = image.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            label_image.setPixmap(image)
            label_image.setObjectName("delete")
            label_image.mousePressEvent = partial(self.deleteTarget, targetDelete = ListAllTarget[i].getTarget(), tanggalDelete = ListAllTarget[i].getTanggal())

            # Create Edit Button
            label_edit_image = QLabel()
            image_edit = QPixmap("./images/edit_btn.png")
            image_edit = image_edit.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            label_edit_image.setPixmap(image_edit)
            label_edit_image.mousePressEvent = partial(self.editTarget, targetLama = ListAllTarget[i].getTarget(), tanggal = ListAllTarget[i].getTanggal())

            # Create Batas Label
            batas = QLabel("|")
            batas.setFont(QFont("Poppins", 20))
            batas.setStyleSheet("margin-left: 10px; margin-right: 10px")

            # Create Target Label
            title = QLabel(ListAllTarget[i].getTarget()[:35] + '..' if (len(ListAllTarget[i].getTarget()) > 35) else ListAllTarget[i].getTarget())
            title.setFont(QFont("Poppins", 12))
            title.mousePressEvent = partial(self.showTargetDetailDisplay, target = ListAllTarget[i])

            # Merge Content With Target Widget
            target_content.addWidget(date_target, alignment=Qt.AlignLeft)
            target_content.addWidget(batas, alignment=Qt.AlignLeft)
            target_content.addWidget(title, alignment=Qt.AlignLeft)
            target_content.addWidget(label_edit_image, alignment=Qt.AlignRight)
            target_content.addWidget(label_image, alignment=Qt.AlignRight)
            target_content.setStretchFactor(date_target, 0)
            target_content.setStretchFactor(title, 1)
            target_content.setStretchFactor(label_edit_image, 0)
            target_content.setStretchFactor(label_image, 0)
            target_content_widget.setLayout(target_content)
            target_content_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

            # Merge contents
            target_box.addWidget(target_content_widget)
            target_box.setStretchFactor(target_content_widget, 0)

            # Set Main Layout
            target_widget.setLayout(target_box)
            target_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            list_target_box.addWidget(target_widget)

        # Set Layout and Widget
        self.widget.setLayout(list_target_box)
        self.widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.scrollArea.setWidget(self.widget)

        # Add Spacer
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        list_target_box.addItem(spacer)

    def showTargetDetailDisplay(self, event, target):
        # Show detail target
        # Set content
        self.parent.stackedWidget.widget(10).text_edit.setText(target.getTarget())
        self.parent.stackedWidget.widget(10).text_edit.setReadOnly(True)
        self.parent.stackedWidget.widget(10).edit_date.setReadOnly(True)

        # Set styling
        self.parent.stackedWidget.widget(10).text_edit.setStyleSheet("background-color: white; margin-top: 0px; margin-bottom: 80px; padding: 10px;")
        
        # Hide Button
        self.parent.stackedWidget.widget(10).cancel_button.setHidden(True)
        self.parent.stackedWidget.widget(10).save_button.setHidden(True)
        
        # Change settings
        self.parent.editMode = False
        self.parent.date = target.getTanggal()

        # Change page to form
        self.parent.stackedWidget.setCurrentIndex(10)

    def addTarget(self, event):
        # Add target
        # Reset settings
        self.parent.editMode = False
        self.parent.stackedWidget.widget(10).text_edit.setText("")
        self.parent.stackedWidget.widget(10).edit_date.setDate(QDate.fromString(datetime.now().strftime("%d/%m/%Y"), "d/M/yyyy"))
        
        # Set edit mode
        self.parent.stackedWidget.widget(10).text_edit.setReadOnly(False)
        
        # Set styling
        self.parent.stackedWidget.widget(10).text_edit.setStyleSheet("background-color: white; margin-top: 0px; margin-bottom: 0px; padding: 10px;")
        
        # Show Buttons
        self.parent.stackedWidget.widget(10).cancel_button.setHidden(False)
        self.parent.stackedWidget.widget(10).save_button.setHidden(False)
        
        # Change page to form
        self.parent.stackedWidget.setCurrentIndex(10)

    def editTarget(self, event, targetLama, tanggal):
        # Set input to selected target attributes
        self.parent.stackedWidget.widget(10).text_edit.setText(targetLama)
        self.parent.stackedWidget.widget(10).edit_date.setDate(QDate.fromString(tanggal, "d/M/yyyy"))
        
        # Set Edit Mode
        self.parent.stackedWidget.widget(10).text_edit.setReadOnly(False)
        
        # Set styling
        self.parent.stackedWidget.widget(10).text_edit.setStyleSheet("background-color: white; margin-top: 0px; margin-bottom: 0px; padding: 10px;")
        
        # Show Buttons
        self.parent.stackedWidget.widget(10).cancel_button.setHidden(False)
        self.parent.stackedWidget.widget(10).save_button.setHidden(False)

        # Set parent attributes
        self.parent.editMode = True
        self.parent.date = tanggal
        self.parent.targetLama = targetLama

        # Change page to form
        self.parent.stackedWidget.setCurrentIndex(10)

    def deleteTarget(self, event, targetDelete, tanggalDelete):
        # Show confirm popup
        confirm_popup = ConfirmPopUp("Are you sure want to delete this target?")
        
        # If user confirmed
        if confirm_popup.exec_() == QDialog.Accepted:
            TargetController().deleteTarget(targetDelete, tanggalDelete)
        
        # Remove old display and create new display with new data
        self.parent.stackedWidget.insertWidget(9, TargetDisplay(self.parent))
        self.parent.stackedWidget.setCurrentIndex(9)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(10))

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

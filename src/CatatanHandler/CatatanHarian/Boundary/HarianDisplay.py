# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QGraphicsDropShadowEffect, QSpacerItem
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QDate
from functools import partial
from CatatanHandler.CatatanHarian.Boundary.HarianImages import *
from CatatanHandler.CatatanHarian.Controller.HarianController import *
from datetime import datetime
from CatatanHandler.ConfirmPopUp.ConfirmPopUp import *

# Class HarianDisplay
class HarianDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main, tanggal = datetime.now().strftime("%d/%m/%Y")):
        super().__init__()
        self.parent = Main
        self.parent.date = tanggal
        self.showHarianDisplay()

    def showHarianDisplay(self):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/CatatanHarian/Boundary/HarianDisplay.ui", self)

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

        # Navigation Buttons
        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        # Date Label
        self.date = self.findChild(QLabel, "label_3")
        self.date.setText(self.parent.date)

        # Calendar Button
        self.calendar = self.findChild(QPushButton, "pushButton_3")
        self.calendar.clicked.connect(self.backToCalendar)

        # Back Button
        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        # Exit Button
        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        # Add Button
        self.add_button = self.findChild(QPushButton, "pushButton_2")
        self.add_button.clicked.connect(self.addHarian)

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

        # Fetch All Harian within Date
        ListAllHarian = HarianController().showHarian(datetime.now().strftime("%d/%m/%Y") if (self.parent.date == "") else self.parent.date)
        ListAllHarian.sort(key=lambda x: x.jam_mulai + "-" + x.jam_berakhir, reverse=False)

        # Container Widget       
        self.widget = QWidget()
        
        # Layout of Container Widget
        list_harian_box = QVBoxLayout()
        list_harian_box.setSpacing(40)

        for i in range(len(ListAllHarian)):
            # Create Main Widget
            harian_widget = QWidget()
            harian_widget.setObjectName("Outer")
            harian_widget.setStyleSheet("""
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
            harian_widget.setContentsMargins(0,0,0,0)
            harian_widget.setMinimumSize(1150, 70)
            harian_widget.setMaximumHeight(70)
            harian_widget.setMaximumWidth(1920)

            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(5)
            shadow.setOffset(4,4)
            harian_widget.setGraphicsEffect(shadow)
            # Create Main Layout
            harian_box = QHBoxLayout()

            # Create Content
            harian_content_widget = QWidget()
            harian_content = QHBoxLayout()
            
            # Setup date content
            date_harian = QLabel(ListAllHarian[i].getJamMulai() + " - " + ListAllHarian[i].getJamBerakhir())
            date_harian.setFont(QFont("Poppins", 12))
            date_harian.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            date_harian.setWordWrap(True)

            # Setup Delete Button
            label_image = QLabel()
            image = QPixmap("./images/delete_btn.png")
            image = image.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            label_image.setPixmap(image)
            label_image.setObjectName("delete")
            label_image.mousePressEvent = partial(self.deleteHarian, harianDelete = ListAllHarian[i], tanggal = ListAllHarian[i].getTanggal())

            # Setup Edit Button
            label_edit_image = QLabel()
            image_edit = QPixmap("./images/edit_btn.png")
            image_edit = image_edit.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            label_edit_image.setPixmap(image_edit)
            label_edit_image.mousePressEvent = partial(self.editHarian, harian_lama = ListAllHarian[i], kegiatan_lama = ListAllHarian[i].getKegiatan(), tanggal = ListAllHarian[i].getTanggal(), jam_mulai_lama = ListAllHarian[i].getJamMulai(), jam_berakhir_lama = ListAllHarian[i].getJamBerakhir())

            # Setup batas
            batas = QLabel("|")
            batas.setFont(QFont("Poppins", 20))
            batas.setStyleSheet("margin-left: 10px; margin-right: 10px")

            # Setup activity
            title = QLabel(ListAllHarian[i].getKegiatan())
            title.setFont(QFont("Poppins", 12))

            # Merging all widgets and layouts
            harian_content.addWidget(date_harian, alignment=Qt.AlignLeft)
            harian_content.addWidget(batas, alignment=Qt.AlignLeft)
            harian_content.addWidget(title, alignment=Qt.AlignLeft)
            harian_content.addWidget(label_edit_image, alignment=Qt.AlignRight)
            harian_content.addWidget(label_image, alignment=Qt.AlignRight)
            harian_content.setStretchFactor(date_harian, 0)
            harian_content.setStretchFactor(title, 1)
            harian_content.setStretchFactor(label_edit_image, 0)
            harian_content.setStretchFactor(label_image, 0)
            harian_content_widget.setLayout(harian_content)
            harian_content_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            
            # Merge contents
            harian_box.addWidget(harian_content_widget)
            harian_box.setStretchFactor(harian_content_widget, 0)

            # Set Main Layout
            harian_widget.setLayout(harian_box)
            harian_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            list_harian_box.addWidget(harian_widget)

        # Set Main Widget
        self.widget.setLayout(list_harian_box)
        self.widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.scrollArea.setWidget(self.widget)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        list_harian_box.addItem(spacer)

    def addHarian(self, event):
        # Turn off edit mode
        self.parent.editMode = False

        # Set initial form to blank
        self.parent.stackedWidget.widget(12).line_edit.setText("")

        # Set form date
        self.parent.stackedWidget.widget(12).date.setText(self.parent.date)

        # Change page
        self.parent.stackedWidget.setCurrentIndex(12)

    def editHarian(self, event, harian_lama, kegiatan_lama, jam_mulai_lama, jam_berakhir_lama, tanggal):
        # Set initial form to old note
        self.parent.stackedWidget.widget(12).line_edit.setText(kegiatan_lama)

        # Set initial date to old note's date
        self.parent.stackedWidget.widget(12).date.setText(tanggal)

        # Set initial time
        self.parent.stackedWidget.widget(12).jam_mulai_edit.setTime(QTime.fromString(jam_mulai_lama, "hh.mm"))
        self.parent.stackedWidget.widget(12).jam_berakhir_edit.setTime(QTime.fromString(jam_berakhir_lama, "hh.mm"))

        # Turn on edit mode
        self.parent.editMode = True

        # Save date and old note
        self.parent.date = tanggal
        self.parent.harian_lama = harian_lama

        # Change page
        self.parent.stackedWidget.setCurrentIndex(12)

    def deleteHarian(self, event, harianDelete, tanggal):
        # Create popup confirm
        confirm_popup = ConfirmPopUp("Are you sure want to delete your plan?")

        # Delete if accepted
        if confirm_popup.exec_() == QDialog.Accepted:
            HarianController().deleteHarian(harianDelete)

        # Remove old widget and create new widget with new data
        self.parent.stackedWidget.insertWidget(11, HarianDisplay(self.parent, tanggal))
        self.parent.stackedWidget.setCurrentIndex(11)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(12))

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(2)
    
    def backToCalendar(self, event):
        self.parent.stackedWidget.setCurrentIndex(13)
        
    def exitEvent(self, event):
        QApplication.quit()
    
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

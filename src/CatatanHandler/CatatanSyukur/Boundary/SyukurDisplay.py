# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QGraphicsDropShadowEffect, QSpacerItem
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QDate
from functools import partial
from CatatanHandler.CatatanSyukur.Boundary.SyukurImages import *
from CatatanHandler.CatatanSyukur.Controller.SyukurController import *
from datetime import datetime
from CatatanHandler.ConfirmPopUp.ConfirmPopUp import *

# Class SyukurDisplay
class SyukurDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showSyukurDisplay()

    def showSyukurDisplay(self):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/CatatanSyukur/Boundary/SyukurDisplay.ui", self)
        
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
        self.add_button.clicked.connect(self.addSyukur)

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

        ListAllSyukur = SyukurController().showSyukur()
        ListAllSyukur.sort(key=lambda x: datetime.strptime(x.tanggal, "%d/%m/%Y").date(), reverse=True)

        # Container Widget       
        self.widget = QWidget()
        
        # Layout of Container Widget
        list_syukur_box = QVBoxLayout()
        list_syukur_box.setSpacing(40)
        for i in range(len(ListAllSyukur)):
            # Create Main Widget
            syukur_widget = QWidget()
            syukur_widget.setObjectName("Outer")
            syukur_widget.setStyleSheet("""
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
            syukur_widget.setContentsMargins(0,0,0,0)
            syukur_widget.setMinimumSize(1150, 70)
            syukur_widget.setMaximumHeight(70)
            syukur_widget.setMaximumWidth(1920)

            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(5)
            shadow.setOffset(4,4)
            syukur_widget.setGraphicsEffect(shadow)

            # Create Main Layout
            syukur_box = QHBoxLayout()

            # Create Content
            syukur_content_widget = QWidget()
            syukur_content = QHBoxLayout()
            
            date_syukur = QLabel(ListAllSyukur[i].getTanggal())
            date_syukur.setFont(QFont("Poppins", 12))
            date_syukur.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            date_syukur.setWordWrap(True)

            label_image = QLabel()
            image = QPixmap("./images/delete_btn.png")
            image = image.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            label_image.setPixmap(image)
            label_image.setObjectName("delete")
            label_image.mousePressEvent = partial(self.deleteSyukur, syukurDelete = ListAllSyukur[i].getSyukur(), tanggalDelete = ListAllSyukur[i].getTanggal())

            label_edit_image = QLabel()
            image_edit = QPixmap("./images/edit_btn.png")
            image_edit = image_edit.scaled(30, 30, Qt.KeepAspectRatio, Qt.FastTransformation)
            label_edit_image.setPixmap(image_edit)
            label_edit_image.mousePressEvent = partial(self.editSyukur, syukurLama = ListAllSyukur[i].getSyukur(), tanggal = ListAllSyukur[i].getTanggal())

            batas = QLabel("|")
            batas.setFont(QFont("Poppins", 20))
            batas.setStyleSheet("margin-left: 10px; margin-right: 10px")

            title = QLabel(ListAllSyukur[i].getSyukur()[:35] + '..' if (len(ListAllSyukur[i].getSyukur()) > 35) else ListAllSyukur[i].getSyukur())
            title.setFont(QFont("Poppins", 12))
            title.mousePressEvent = partial(self.showSyukurDetailDisplay, syukur = ListAllSyukur[i])

            syukur_content.addWidget(date_syukur, alignment=Qt.AlignLeft)
            syukur_content.addWidget(batas, alignment=Qt.AlignLeft)
            syukur_content.addWidget(title, alignment=Qt.AlignLeft)
            syukur_content.addWidget(label_edit_image, alignment=Qt.AlignRight)
            syukur_content.addWidget(label_image, alignment=Qt.AlignRight)
            syukur_content.setStretchFactor(date_syukur, 0)
            syukur_content.setStretchFactor(title, 1)
            syukur_content.setStretchFactor(label_edit_image, 0)
            syukur_content.setStretchFactor(label_image, 0)
            syukur_content_widget.setLayout(syukur_content)
            syukur_content_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            
            # Merge contents
            syukur_box.addWidget(syukur_content_widget)
            syukur_box.setStretchFactor(syukur_content_widget, 0)

            # Set Main Layout
            syukur_widget.setLayout(syukur_box)
            syukur_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
            list_syukur_box.addWidget(syukur_widget)

        self.widget.setLayout(list_syukur_box)
        self.widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.scrollArea.setWidget(self.widget)
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)
        list_syukur_box.addItem(spacer)

    def showSyukurDetailDisplay(self, event, syukur):
        self.parent.stackedWidget.widget(8).text_edit.setText(syukur.getSyukur())
        self.parent.stackedWidget.widget(8).text_edit.setReadOnly(True)
        self.parent.stackedWidget.widget(8).text_edit.setStyleSheet("background-color: white; margin-top: 0px; margin-bottom: 80px; padding: 10px;")
        self.parent.stackedWidget.widget(8).cancel_button.setHidden(True)
        self.parent.stackedWidget.widget(8).save_button.setHidden(True)
        self.parent.editMode = False
        self.parent.date = syukur.getTanggal()
        self.parent.stackedWidget.setCurrentIndex(8)

    def addSyukur(self, event):
        self.parent.editMode = False
        self.parent.stackedWidget.widget(8).text_edit.setText("")
        self.parent.stackedWidget.widget(8).text_edit.setReadOnly(False)
        self.parent.stackedWidget.widget(8).text_edit.setStyleSheet("background-color: white; margin-top: 0px; margin-bottom: 0px; padding: 10px;")
        self.parent.stackedWidget.widget(8).cancel_button.setHidden(False)
        self.parent.stackedWidget.widget(8).save_button.setHidden(False)
        self.parent.stackedWidget.setCurrentIndex(8)

    def editSyukur(self, event, syukurLama, tanggal):
        self.parent.stackedWidget.widget(8).text_edit.setText(syukurLama)
        self.parent.stackedWidget.widget(8).text_edit.setReadOnly(False)
        self.parent.stackedWidget.widget(8).text_edit.setStyleSheet("background-color: white; margin-top: 0px; margin-bottom: 0px; padding: 10px;")
        self.parent.stackedWidget.widget(8).cancel_button.setHidden(False)
        self.parent.stackedWidget.widget(8).save_button.setHidden(False)
        self.parent.editMode = True
        self.parent.date = tanggal
        self.parent.syukurLama = syukurLama
        self.parent.stackedWidget.setCurrentIndex(8)

    def deleteSyukur(self, event, syukurDelete, tanggalDelete):
        confirm_popup = ConfirmPopUp()
        if confirm_popup.exec_() == QDialog.Accepted:
            SyukurController().deleteSyukur(syukurDelete, tanggalDelete)
        self.parent.stackedWidget.insertWidget(7, SyukurDisplay(self.parent))
        self.parent.stackedWidget.setCurrentIndex(7)
        self.parent.stackedWidget.removeWidget(self.parent.stackedWidget.widget(8))

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(2)
        
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
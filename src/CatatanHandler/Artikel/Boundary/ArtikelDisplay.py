# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsDropShadowEffect, QSizePolicy
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QDate, Qt
from CatatanHandler.Artikel.Boundary.ArtikelImages import *
from functools import partial
from CatatanHandler.Artikel.Controller.ArtikelController import *

# Class ArtikelDisplay
class ArtikelDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showArtikelDisplay()

    def showArtikelDisplay(self):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/Artikel/Boundary/ListArtikel.ui", self)

        # Sidebar and other buttons
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
        
        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

        # Styling Scroll Area
        self.scrollArea = self.findChild(QScrollArea, "scrollArea")
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

        # Styling Title
        self.title = self.findChild(QLabel, "label_9")
        self.title.setStyleSheet("margin: 40px 0;")

        # Getting list of articles
        articleController = ArtikelController()
        listOfArticle = articleController.showArtikel()

        # Container Widget       
        self.widget = QWidget()
        
        # Layout of Container Widget
        list_article_box = QVBoxLayout()
        list_article_box.setSpacing(40)

        for i in range(len(listOfArticle)):
            # Create Main Widget
            article_widget = QWidget()
            
            # Styling Main Widget
            article_widget.setStyleSheet("""
                QWidget {
                    background-color: white; border-radius: 20px; margin-right: 40px
                }
                QLabel {
                    margin-right: 0px;
                }
            """)
            article_widget.setContentsMargins(20,20,20,20)

            # Add drop shadow effect to main widget
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(5)
            shadow.setOffset(4,4)
            article_widget.setGraphicsEffect(shadow)

            # Create Main Layout
            article_box = QHBoxLayout()

            # Create First Content
            label_image = QLabel()
            image = QPixmap()
            image.loadFromData(listOfArticle[i].getImage())
            image = image.scaled(300, 188)
            label_image.setPixmap(image)

            # Create Second Content
            article_content_widget = QWidget()
            article_content = QVBoxLayout()

            # Create title of article
            title = QLabel(listOfArticle[i].getTitle())
            title.setFont(QFont("Poppins", 18, QFont.Bold))
            title.setWordWrap(True)
            title.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

            # Create description of article
            description = QLabel(listOfArticle[i].getContent()[8:120] + "...")
            description.setFont(QFont("Poppins", 12))
            description.setWordWrap(True)
            description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Add second content to content widget
            article_content.addWidget(title)
            article_content.addWidget(description, alignment=Qt.AlignTop)
            article_content_widget.setLayout(article_content)
            article_content_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

            # Create Third Content
            button_read_more = QPushButton()
            button_read_more.setText("Read More")
            button_read_more.setFont(QFont("Poppins", 12))
            button_read_more.setStyleSheet("margin: 60px 40px 0px auto; padding : 5px 10px; border-radius: 15px; color: white; background-color: #00C2C3; font-weight: bold")
            button_read_more.setMaximumWidth(250)
            button_read_more.clicked.connect(partial(self.showArtikelDetailDisplay, listOfArticle[i]))

            # Merge contents
            article_box.addWidget(label_image)
            article_box.addWidget(article_content_widget)
            article_box.addWidget(button_read_more)

            # Set Main Layout
            article_widget.setLayout(article_box)
            list_article_box.addWidget(article_widget)

        self.widget.setLayout(list_article_box)
        self.scrollArea.setWidget(self.widget)

    def showArtikelDetailDisplay(self, article):
        # Set title of article
        self.parent.stackedWidget.widget(4).article_title.setText(article.getTitle())

        # Set image of article
        image = QPixmap()
        image.loadFromData(article.getImage())
        image = image.scaled(500,313)

        # Set content of article
        self.parent.stackedWidget.widget(4).content.setText(article.getContent())
        self.parent.stackedWidget.widget(4).label_image.setPixmap(image)

        # Change page to detail article
        self.parent.stackedWidget.setCurrentIndex(4)

    def back(self, event):
        # Go back to main menu
        self.parent.stackedWidget.setCurrentIndex(2)

    def exitEvent(self, event):
        # Exit application
        QApplication.quit()

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

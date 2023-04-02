# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPixmap
from CatatanHandler.Artikel.Boundary.ArtikelDisplay import *
from CatatanHandler.Artikel.Boundary.ArtikelImages import *
from functools import partial
from CatatanHandler.Artikel.Controller.ArtikelController import *

# Class Register
class ArtikelDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showArtikelDisplay()

    def showArtikelDisplay(self):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/Artikel/Boundary/ListArtikel.ui", self)

        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.back)

        self.exit = self.findChild(QLabel, "label_7")
        self.exit.mousePressEvent = self.exitEvent

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
        self.title = self.findChild(QLabel, "label_9")
        self.title.setStyleSheet("margin: 40px 0;")
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
            article_widget.setStyleSheet("background-color: white; border-radius: 20px; margin-right: 20px")
            article_widget.setContentsMargins(20,20,20,20)
            # Create Main Layout
            article_box = QHBoxLayout()

            # Create First Content
            label_image = QLabel()
            image = QPixmap("./src/CatatanHandler/Artikel/Boundary/DummyArtikel.png")
            label_image.setPixmap(image)
            label_image.setMaximumWidth(200)

            # Create Second Content
            article_content_widget = QWidget()
            article_content = QVBoxLayout()
            title = QLabel(listOfArticle[i].getTitle())
            title.setFont(QFont("Poppins", 18, QFont.Bold))
            title.setWordWrap(True)
            description = QLabel(listOfArticle[i].getContent()[8:120] + "...")
            description.setFont(QFont("Poppins", 12))
            description.setWordWrap(True)
            article_content.addWidget(title)
            article_content.addWidget(description)
            article_content_widget.setLayout(article_content)

            # Create Third Content
            button_read_more = QPushButton()
            button_read_more.setText("Read More")
            button_read_more.setFont(QFont("Poppins", 12))
            button_read_more.setStyleSheet("margin: 60px auto 0px auto; padding : 5px 10px; border-radius: 15px; color: white; background-color: #00C2C3; font-weight: bold")
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
        self.parent.stackedWidget.widget(4).article_title.setText(article.getTitle())
        self.parent.stackedWidget.widget(4).content.setText(article.getContent())
        self.parent.stackedWidget.setCurrentIndex(4)

    def back(self, event):
        self.parent.stackedWidget.setCurrentIndex(2)

    def exitEvent(self, event):
        QApplication.quit()
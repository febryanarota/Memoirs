# Import libraries
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QGraphicsDropShadowEffect
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QDate

# Class Register
class ArtikelDetailDisplay(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()
        self.parent = Main
        self.showArtikelDetailDisplay()

    def showArtikelDetailDisplay(self):
        # Set main window as parent
        uic.loadUi("./src/CatatanHandler/Artikel/Boundary/ListArtikel.ui", self)

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

        self.main_menu = self.findChild(QLabel, "label_2")
        self.main_menu.mousePressEvent = self.back

        self.back_button = self.findChild(QPushButton, "pushButton")
        self.back_button.clicked.connect(self.showArtikelDisplay)

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

        # Container Widget
        self.widget = QWidget()

        # Layout of Container Widget
        main_article_box = QVBoxLayout()
        main_article_box.setSpacing(0)
        main_article_box.setStretch(0, 0)

        self.article_title = QLabel()
        self.article_title.setText("Judul Artikel")
        self.article_title.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.article_title.setFont(QFont("Poppins", 18, QFont.Bold))

        # Create Main Widget
        article_widget = QWidget()
        article_widget.setStyleSheet("background-color: white; border-radius: 20px; margin-right: 20px; margin-top: 10px;")
        article_widget.setContentsMargins(20,20,20,20)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setOffset(4,4)
        article_widget.setGraphicsEffect(shadow)
        sp2 = article_widget.sizePolicy()
        sp2.setVerticalPolicy(QSizePolicy.Expanding)
        article_widget.setSizePolicy(sp2)

        # Create Main Layout
        article_box = QHBoxLayout()

        # Create First Content
        label_image = QLabel()
        image = QPixmap("./src/CatatanHandler/Artikel/Boundary/DummyArtikel.png")
        label_image.setPixmap(image)
        label_image.setMaximumWidth(200)

        # Create Second Content
        self.content = QLabel()
        self.content.setFont(QFont("Poppins", 12))
        self.content.setAlignment(QtCore.Qt.AlignJustify)
        self.content.setWordWrap(True)

        # Merge contents
        article_box.addWidget(label_image, alignment = QtCore.Qt.AlignTop)
        article_box.addWidget(self.content, alignment = QtCore.Qt.AlignTop)

        # Set Main Layout
        article_widget.setLayout(article_box)
        main_article_box.addWidget(self.article_title, alignment = QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        main_article_box.addWidget(article_widget, alignment = QtCore.Qt.AlignTop)
        main_article_box.setStretchFactor(self.article_title, 0)
        main_article_box.setStretchFactor(article_widget, 1)

        self.widget.setLayout(main_article_box)
        self.scrollArea.setWidget(self.widget)

    def showArtikelDisplay(self):
        self.parent.stackedWidget.setCurrentIndex(3)

    def back(self):
        self.parent.stackedWidget.setCurrentIndex(2)

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

    def exitEvent(self):
        QApplication.quit()

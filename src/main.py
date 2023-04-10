# Import libraries
import sys
from datetime import date
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from AuthHandler.Boundary.Login import Login
from AuthHandler.Boundary.Register import Register
from MainMenu.MainMenu import MainMenu
from CatatanHandler.Artikel.Boundary.ArtikelDisplay import ArtikelDisplay
from CatatanHandler.Artikel.Boundary.ArtikelDetailDisplay import ArtikelDetailDisplay
from CatatanHandler.ToDoList.Boundary.TDLDisplay import TDLDisplay
from CatatanHandler.ToDoList.Boundary.FormTDL import FormTDL
from CatatanHandler.CatatanSyukur.Boundary.SyukurDisplay import SyukurDisplay
from CatatanHandler.CatatanSyukur.Boundary.FormSyukur import FormSyukur
from CatatanHandler.CatatanTarget.Boundary.TargetDisplay import TargetDisplay
from CatatanHandler.CatatanTarget.Boundary.FormTarget import FormTarget
from CatatanHandler.CatatanHarian.Boundary.HarianDisplay import HarianDisplay
from CatatanHandler.CatatanHarian.Boundary.FormHarian import FormHarian
from CatatanHandler.Calendar.Calendar import Calendar
from CatatanHandler.Calendar.CalendarToDo import CalendarToDo

# Creating connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("./src/Database/memoirs.sqlite")

# Open the connection
if not con.open():
    print(f"Database Error: {con.lastError().databaseText()}")
    sys.exit(1)

# Create Passcode Table
createPasscodeTableQuery = QSqlQuery()
createPasscodeTableQuery.exec(
    """
    CREATE TABLE passcode(
        passcode CHAR(6) PRIMARY KEY
    )
    """
)

# Create Article Table
createArticleTableQuery = QSqlQuery()
createArticleTableQuery.exec(
    """
    CREATE TABLE article(
        title VARCHAR(100) PRIMARY KEY,
        tanggal VARCHAR(100),
        content VARCHAR(5000) NOT NULL,
        image VARCHAR(100)
    )
    """
)

# Create To Do List Table
createToDoListTableQuery = QSqlQuery()
createToDoListTableQuery.exec(
    """
    CREATE TABLE to_do_list(
        to_do VARCHAR(105) PRIMARY KEY,
        tanggal VARCHAR(100) PRIMARY KEY,
        done INT default 0
    )
    """
)

# Create Catatan Harian Table
createCatatanHarianTableQuery = QSqlQuery()
createCatatanHarianTableQuery.exec(
    """
    CREATE TABLE catatan_harian(
        tanggal VARCHAR(100),
        jam_mulai VARCHAR(100),
        jam_berakhir VARCHAR(100),
        nama_kegiatan VARCHAR(40),
        PRIMARY KEY (tanggal, jam_mulai, jam_berakhir, nama_kegiatan)
    )
    """
)

# Create Catatan Target Table
createCatatanTargetTableQuery = QSqlQuery()
createCatatanTargetTableQuery.exec(
    """
    CREATE TABLE catatan_target(
        target VARCHAR(1000),
        tanggal VARCHAR(100),
        PRIMARY KEY (target, tanggal)
    )
    """
)

# Create Catatan Syukur Table
createCatatanSyukurTableQuery = QSqlQuery()
createCatatanSyukurTableQuery.exec(
    """
    CREATE TABLE catatan_syukur(
        syukur VARCHAR(1000),
        tanggal VARCHAR(100) PRIMARY KEY
    )
    """
)

# Class MainWindow
class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        self.initializeMain()

    def initializeMain(self):
        # Set initial size and window title
        self.resize(1280, 840)
        self.setWindowTitle("Memoirs")
        self.initializeDataArticle()
        self.date = date.today().strftime('%d/%m/%Y')
        self.editMode = False

        # Create stackedWidget for navigation
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(Login(self))
        self.stackedWidget.addWidget(Register(self))
        self.stackedWidget.addWidget(MainMenu(self))
        self.stackedWidget.addWidget(ArtikelDisplay(self))
        self.stackedWidget.addWidget(ArtikelDetailDisplay(self))
        self.stackedWidget.addWidget(TDLDisplay(self, self.date))
        self.stackedWidget.addWidget(FormTDL(self, self.date))
        self.stackedWidget.addWidget(SyukurDisplay(self))
        self.stackedWidget.addWidget(FormSyukur(self))
        self.stackedWidget.addWidget(TargetDisplay(self))
        self.stackedWidget.addWidget(FormTarget(self))
        self.stackedWidget.addWidget(HarianDisplay(self))
        self.stackedWidget.addWidget(FormHarian(self))
        self.stackedWidget.addWidget(Calendar(self))
        self.stackedWidget.addWidget(CalendarToDo(self))

        # Set central widget
        self.setCentralWidget(self.stackedWidget)

        # Check if passcode already created or not
        query = QSqlQuery()
        query.exec(
            """
            SELECT * FROM passcode
            """
        )

        # If passcode exists, switch to login form, else switch to register form
        if query.first():
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def initializeDataArticle(self):
        with open("./dataseed/dataArtikel.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()

            readTitle = True
            title = ""
            tanggal = ""
            content = ""
            image = ""
            for line in lines:
                if readTitle:
                    title = line
                    readTitle = False
                elif line == "\n":
                    readTitle = True
                    query = QSqlQuery()
                    query.prepare(
                    """
                    INSERT INTO article VALUES (?, ?, ?, ?)
                    """
                    )
                    content = content[:len(content) - 1]
                    query.addBindValue(title)
                    query.addBindValue(tanggal)
                    query.addBindValue(content)
                    query.addBindValue(image)
                    query.exec()
                    title = ""
                    content = ""
                else:
                    content += "        " + line + "\n"

# Run Application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

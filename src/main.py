# Import libraries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from AuthHandler.Boundary.Login import *
from AuthHandler.Boundary.Register import *
from MainMenu.MainMenu import *
from CatatanHandler.Artikel.Boundary.ArtikelDisplay import *
from CatatanHandler.Artikel.Boundary.ArtikelDetailDisplay import *
from CatatanHandler.ToDoList.Boundary.TDLDisplay import *
from CatatanHandler.ToDoList.Boundary.FormTDL import *
from CatatanHandler.CatatanSyukur.Boundary.SyukurDisplay import *
from CatatanHandler.CatatanSyukur.Boundary.FormSyukur import *
from CatatanHandler.CatatanTarget.Boundary.TargetDisplay import *
from CatatanHandler.CatatanTarget.Boundary.FormTarget import *
from CatatanHandler.CatatanHarian.Boundary.HarianDisplay import *
from CatatanHandler.CatatanHarian.Boundary.FormHarian import *
from CatatanHandler.Calendar.Calendar import *

# Creating connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("./src/Database/memoirs.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
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
        
        # Set initial size and window title
        self.resize(1280, 840)
        self.setWindowTitle("Memoirs")
        self.initializeDataArticle()
        self.date = datetime.date.today().strftime('%Y-%m-%d')
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
        if(query.first()):
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def initializeDataArticle(self):
        f = open("./dataseed/dataArtikel.txt", 'r')
        lines = f.readlines()

        readTitle = True
        title = ""
        tanggal = ""
        content = ""
        image = ""
        for line in lines:
            if(readTitle):
                title = line
                readTitle = False
            elif(line == "\n"):
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
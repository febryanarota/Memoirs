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
#------------------TESTING------------------#
# createToDoListTableQuery.exec(
#     """
#     INSERT INTO to_do_list (to_do, tanggal, done) VALUES ('Makan', '2021-05-01', 0)
#     """
# )

createToDoListTableQuery.exec(
    "SELECT * FROM to_do_list"
)

while (createToDoListTableQuery.next()):
    print(createToDoListTableQuery.value(0))
    print(createToDoListTableQuery.value(1))
    print(createToDoListTableQuery.value(2))


# deletePasscodeQuery = QSqlQuery()
# deletePasscodeQuery.exec(
#     """
#     DELETE FROM to_do_list
#     """
# )
#----------------------------------------------#

# To reset passcode for the mean time, execute this code below.
# Delete Current Passcode
# deletePasscodeQuery = QSqlQuery()
# deletePasscodeQuery.exec(
#     """
#     DELETE FROM passcode
#     """
# )



# Class MainWindow
class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        
        # Set initial size and window title
        self.resize(1280, 840)
        self.setWindowTitle("Memoirs")
        self.initializeDataArticle()

        # Create stackedWidget for navigation
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(Login(self))
        self.stackedWidget.addWidget(Register(self))
        self.stackedWidget.addWidget(MainMenu(self))
        self.stackedWidget.addWidget(ArtikelDisplay(self))
        self.stackedWidget.addWidget(ArtikelDetailDisplay(self))
        self.stackedWidget.addWidget(TDLDisplay(self))
        self.stackedWidget.addWidget(FormTDL(self))

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
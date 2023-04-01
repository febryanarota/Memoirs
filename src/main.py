# Import libraries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from AuthHandler.Boundary.Login import *
from AuthHandler.Boundary.Register import *
from MainMenu.MainMenu import *

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

# To reset passcode for the mean time, execute this code below.
# Delete Current Passcode
#deletePasscodeQuery = QSqlQuery()
#deletePasscodeQuery.exec(
    #"""
    #DELETE FROM passcode
    #"""
#)

# Class MainWindow
class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        super().__init__()
        
        # Set initial size and window title
        self.resize(1280, 840)
        self.setWindowTitle("Memoirs")

        # Create stackedWidget for navigation
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(Login(self))
        self.stackedWidget.addWidget(Register(self))
        self.stackedWidget.addWidget(MainMenu(self))

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

# Run Application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
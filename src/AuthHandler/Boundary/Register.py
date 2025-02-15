# Import libraries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QFont
from AuthHandler.Controller.AuthController import AuthController

# Class Register
class Register(QMainWindow):
    # Constructor
    def __init__(self, Main):
        super().__init__()

        # Set main window as parent
        self.parent = Main

        # Create Title
        self.label1 = QLabel(self)
        self.label1.setText("Register")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Poppins", 25, QFont.Bold))
        self.label1.setStyleSheet("margin: 150px 0px 0px 0px; letter-spacing: 2px; color: #2F2F2F")

        self.label2 = QLabel(self)
        self.label2.setText("new passcode")
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(QFont("Poppins", 10, QFont.Bold))
        self.label2.setStyleSheet("margin: 5px 0px 0px 0px; letter-spacing: 5px; color: #2F2F2F")

        # Create input box for passcode
        self.passcode = ""
        self.input = QLineEdit(self)
        self.input.textChanged.connect(self.handleChangePasscode)
        self.input.setAlignment(Qt.AlignCenter)
        self.input.setMinimumWidth(350)
        self.input.setStyleSheet("margin: 80px auto 0px auto; padding: 15px 15px; font-size: 25px; letter-spacing: 5px; border-radius: 10px; border: 1px solid; color: #2F2F2F")

        # Create label warning
        self.label3 = QLabel(self)
        self.label3.setText("Please insert 6 passcode numbers")
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setStyleSheet("margin-top: 10px; color: #2F2F2F; font-size: 14px")

        # Create register button
        self.button = QPushButton(self)
        self.button.clicked.connect(self.register)
        self.button.setText("Register")
        self.button.setFont(QFont("Poppins", 15))
        self.button.setStyleSheet("margin: 40px auto 0px auto; padding : 10px 40px; border-radius: 10px; color: white; background-color: #00C2C3; font-weight: bold")
        self.button.setMaximumWidth(300)

        # Create vertical layout
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0,0,0,0)

        # Create horizontal spacer
        horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Add widgets and spacer to layout
        vbox.addItem(horizontalSpacer)
        vbox.addWidget(self.label1, 0, Qt.AlignTop)
        vbox.addWidget(self.label2, 0, Qt.AlignTop)
        vbox.addWidget(self.input, 0, Qt.AlignCenter)
        vbox.addWidget(self.label3, 0, Qt.AlignTop)
        vbox.addWidget(self.button, 0, Qt.AlignCenter)
        vbox.setAlignment(Qt.AlignCenter | Qt.AlignTop)

        # Set layout
        container = QWidget()
        container.setLayout(vbox)

        # Set central widget
        self.setCentralWidget(container)

    def handleChangePasscode(self):
        # Method to handle input change
        self.passcode = self.input.text()

    def register(self):
        # Method to handle event button to register

        # Create controller class
        controller = AuthController()
        condition = controller.register(self.passcode)

        # Check return value
        if condition == 0 :
            self.parent.stackedWidget.setCurrentIndex(0)
        else:
            self.label3.setText("Passcode Tidak Valid!")
            self.label3.setStyleSheet("margin-top: 10px; color: red; font-size: 14px")

# Import libraries
from PyQt5.QtWidgets import QTextEdit, QApplication, QDialog, QLabel, QPushButton
from PyQt5 import uic
from CatatanHandler.ConfirmPopUp.ConfirmImages import *
from datetime import datetime

class ConfirmPopUp(QDialog):
    def __init__(self, title = ""):
        super().__init__()
        self.title = title
        self.showConfirmPopUp()
        self.resize(400, 250)
        self.setWindowTitle("Confirm Delete")

    def showConfirmPopUp(self):
        uic.loadUi("./src/CatatanHandler/ConfirmPopUp/ConfirmDialog.ui", self)

        # Cancel Button
        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.reject)

        # Save Button
        self.save_button = self.findChild(QPushButton, "save")
        self.save_button.clicked.connect(self.accept)

        # Set title
        self.title_label = self.findChild(QLabel, "label_10")
        if(self.title != ""):
            self.title_label.setText(self.title)

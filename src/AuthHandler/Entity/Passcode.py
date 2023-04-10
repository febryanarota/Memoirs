from PyQt5.QtSql import QSqlQuery

class Passcode():
    # Constructor
    def __init__(self, passcode = ""):
        self.passcode = passcode

    def getPasscode(self):
        # Method to execute query get passcode
        query = QSqlQuery()
        query.exec("SELECT * FROM passcode")
        query.first()
        return query.value(0)

    def setPasscode(self):
        # Method to execute query insert new passcode
        createPasscodeQuery = QSqlQuery()
        createPasscodeQuery.prepare(
            """
            INSERT INTO passcode VALUES (?)
            """
        )
        createPasscodeQuery.addBindValue(self.passcode)
        createPasscodeQuery.exec()
        return

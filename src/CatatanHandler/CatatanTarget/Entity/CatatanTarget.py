from PyQt5.QtSql import QSqlQuery

class CatatanTarget():
    def __init__(self, target = "", tanggal = ""):
        self.target = target
        self.tanggal = tanggal

    def getTarget(self):
        return (self.target)

    def getTanggal(self):
        return (self.tanggal)

    def getAllTarget(self):
        # Method to execute query select all target
        query = QSqlQuery()
        query.prepare("SELECT * FROM catatan_target")
        query.exec()

        listOfTarget = []
        while query.next():
            content = CatatanTarget(query.value(0), query.value(1))
            listOfTarget.append(content)
        return listOfTarget

    def save(self):
        # Method to execute query insert to do list
        query = QSqlQuery()

        # Prepare and execute an INSERT query
        query.prepare("INSERT INTO catatan_target (target, tanggal) VALUES (?, ?)")
        query.addBindValue(self.target)
        query.addBindValue(self.tanggal)
        query.exec()

        # Execute query to retrieve the updated to do list
        newListOfTarget = self.getAllTarget()
        return newListOfTarget

    def edit(self, prev_target):
        # Method to execute query update to do list
        query = QSqlQuery()

        # Prepare and execute an UPDATE query
        query.prepare("UPDATE catatan_target SET target = ?, tanggal = ? WHERE target = ? AND tanggal = ?")
        query.addBindValue(self.target)
        query.addBindValue(self.tanggal)
        query.addBindValue(prev_target.target)
        query.addBindValue(prev_target.tanggal)
        query.exec()

        # Execute query to retrieve the updated to do list
        newListOfTarget = self.getAllTarget()
        return (newListOfTarget)

    def delete(self):
        # Method to execute query delete to do list
        query = QSqlQuery()

        # Prepare and execute an DELETE query
        query.prepare("DELETE from catatan_target WHERE target = ? AND tanggal = ?")
        query.addBindValue(self.target)
        query.addBindValue(self.tanggal)
        query.exec()

        # Execute query to retrieve the updated to do list
        newListOfTarget = self.getAllTarget()
        return (newListOfTarget)

from PyQt5.QtSql import QSqlQuery

class CatatanTarget():
    def __init__(self, target = "", tanggal = ""):
        self.target = target
        self.tanggal = tanggal
    
    def getTarget(self):
        return (self.target)
    
    def getTanggal(self):
        return (self.tanggal)
    
    # CatatanTarget[*] save(self):
    #     query = QSqlQuery()
    #     query.prepare("INSERT INTO CatatanTarget VALUES (?, ?)")
    #     query.addBindValue(self.target)
    #     query.addBindValue(self.tanggal)
    #     query.exec()

    #     listOfTarget = self.getAllTarget()
    #     return (listOfTarget)
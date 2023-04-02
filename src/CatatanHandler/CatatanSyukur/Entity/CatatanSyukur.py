from PyQt5.QtSql import QSqlQuery

class CatatanSyukur:
    def __init__(self, tanggal, syukur = ""):
        self.tanggal = tanggal
        self.syukur = syukur

    def getSyukur(self):
        return self.syukur
    
    def getTanggal(self):
        return self.tanggal

    def getAllSyukur():
        getAllQuery = QSqlQuery()
        getAllQuery.exec("SELECT * FROM catatanSyukur")
        allSyukur = []
        while getAllQuery.next():
            content = CatatanSyukur(getAllQuery.value(0), getAllQuery.value(1))
            allSyukur.append(content)
        return allSyukur

    def save(self):
        saveQuery = QSqlQuery()
        saveQuery.prepare(
            """
            INSERT INTO catatanSyukur VALUES (?,?)
            """
        )
        saveQuery.addBindValue(self.tanggal)
        saveQuery.addBindValue(self.syukur)
        saveQuery.exec()
        return self.getAllSyukur()
    
    def edit(self, syukurLama):
        editQuery = QSqlQuery()
        editQuery.prepare(
            """
            UPDATE catatanSyukur
            SET
                tanggal = ?
                syukur = ?
            WHERE tanggal = ? AND syukur = ?
            """
        )
        editQuery.addBindValue(self.tanggal)
        editQuery.addBindValue(self.syukur)
        editQuery.addBindValue(syukurLama.tanggal)
        editQuery.addBindValue(syukurLama.syukur)
        editQuery.exec()
        return self.getAllSyukur()

    def delete(self):
        deleteQuery = QSqlQuery()
        deleteQuery.prepare(
            """
            DELETE FROM catatanSyukur
            WHERE tanggal = ? AND syukur = ?
            """
        )
        deleteQuery.addBindValue(self.tanggal)
        deleteQuery.addBindValue(self.syukur)
        deleteQuery.exec()
        return self.getAllSyukur()




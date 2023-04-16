from PyQt5.QtSql import QSqlQuery

class CatatanSyukur:
    def __init__(self, syukur = "", tanggal = ""):
        self.tanggal = tanggal
        self.syukur = syukur

    def getSyukur(self):
        return self.syukur

    def getTanggal(self):
        return self.tanggal

    def getAllSyukur(self):
        # Prepare query
        getAllQuery = QSqlQuery()
        getAllQuery.exec("SELECT * FROM catatan_syukur")

        # Getting list of syukur
        allSyukur = []
        while getAllQuery.next():
            content = CatatanSyukur(getAllQuery.value(0), getAllQuery.value(1))
            allSyukur.append(content)
        return allSyukur

    def save(self):
        # Prepare query
        saveQuery = QSqlQuery()
        saveQuery.prepare(
            """
            INSERT INTO catatan_syukur (syukur, tanggal) VALUES (?,?)
            """
        )

        # Bind values to query
        saveQuery.addBindValue(self.syukur)
        saveQuery.addBindValue(self.tanggal)
        saveQuery.exec()
        return self.getAllSyukur()

    def edit(self, syukurLama):
        # Prepare query
        editQuery = QSqlQuery()
        editQuery.prepare(
            """
            UPDATE catatan_syukur
            SET syukur = ?
            WHERE tanggal = ? AND syukur = ?
            """
        )

        # Bind values to query
        editQuery.addBindValue(self.syukur)
        editQuery.addBindValue(self.tanggal)
        editQuery.addBindValue(syukurLama)
        editQuery.exec()
        return self.getAllSyukur()

    def delete(self):
        # Prepare query
        deleteQuery = QSqlQuery()
        deleteQuery.prepare(
            """
            DELETE FROM catatan_syukur
            WHERE syukur = ? AND tanggal = ?
            """
        )

        # Bind values to query
        deleteQuery.addBindValue(self.syukur)
        deleteQuery.addBindValue(self.tanggal)
        deleteQuery.exec()
        return self.getAllSyukur()

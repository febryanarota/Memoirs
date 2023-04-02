from PyQt5.QtSql import QSqlQuery

class CatatanSyukur:
    def __init__(self, tanggal, syukur = ""):
        self.tanggal = tanggal
        self.syukur = syukur

    def getSyukur(self):
        return self.syukur
    
    def getTanggal(self):
        return self.tanggal
    
    #TODO: save, edit, delete, getAllSyukur

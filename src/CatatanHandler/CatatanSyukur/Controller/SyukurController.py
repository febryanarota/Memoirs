from CatatanHandler.CatatanSyukur.Entity.CatatanSyukur import *

class SyukurController:
    def showSyukur(self):
        allSyukur = CatatanSyukur().getAllSyukur()
        return allSyukur
    
    def addSyukur(self,syukurBaru, tanggal):
        newSyukur = CatatanSyukur(syukurBaru, tanggal)
        allSyukur = newSyukur.save()
        return allSyukur

    def editSyukur(self, syukurLama ,syukurBaru, tanggal):
        newSyukur = CatatanSyukur(syukurBaru, tanggal)
        allSyukur = newSyukur.edit(syukurLama)
        return allSyukur

    def deleteSyukur(self, syukurDelete, tanggalDelete):
        deletedSyukur = CatatanSyukur(syukurDelete, tanggalDelete)
        allSyukur = deletedSyukur.delete()
        return allSyukur
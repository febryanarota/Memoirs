from CatatanHandler.CatatanSyukur.Entity.CatatanSyukur import CatatanSyukur

class SyukurController:
    def showSyukur(self):
        # Getting all syukur
        allSyukur = CatatanSyukur().getAllSyukur()
        return allSyukur
    
    def addSyukur(self,syukurBaru, tanggal):
        # Add new catatan syukur
        newSyukur = CatatanSyukur(syukurBaru, tanggal)
        allSyukur = newSyukur.save()
        return allSyukur

    def editSyukur(self, syukurLama ,syukurBaru, tanggal):
        # Edit existing catatan syukur
        newSyukur = CatatanSyukur(syukurBaru, tanggal)
        allSyukur = newSyukur.edit(syukurLama)
        return allSyukur

    def deleteSyukur(self, syukurDelete, tanggalDelete):
        # Delete selected catatan syukur
        deletedSyukur = CatatanSyukur(syukurDelete, tanggalDelete)
        allSyukur = deletedSyukur.delete()
        return allSyukur

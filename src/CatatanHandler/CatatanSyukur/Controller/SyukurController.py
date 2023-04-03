from CatatanSyukur.Entity.CatatanSyukur import *

class SyukurController:
    def showSyukur():
        allSyukur = CatatanSyukur().getAllSyukur
        # TODO: create SyukurDisplay object and call showSyukurDisplay() method
    
    def addSyukur(syukurBaru, tanggal):
        newSyukur = CatatanSyukur(tanggal, syukurBaru)
        allSyukur = newSyukur.save()
        # TODO: create SyukurDisplay object and call showSyukurDisplay() method

    def editSyukur(syukurBaru, tanggalBaru, tanggalLama):
        newSyukur = CatatanSyukur(tanggalBaru, syukurBaru)
        allSyukur = newSyukur.edit(tanggalLama)
        # TODO: create SyukurDisplay object and call showSyukurDisplay() method

    def deleteSyukur(tanggalDelete):
        deletedSyukur = CatatanSyukur(tanggalDelete)
        allSyukur = deletedSyukur.delete()
        # TODO: create SyukurDisplay object and call showSyukurDisplay() method

        
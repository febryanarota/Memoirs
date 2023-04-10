from CatatanHandler.CatatanHarian.Entity.CatatanHarian import *

class HarianController():
    def showHarian(self, tanggal):
        # Create entity
        entityHarian = CatatanHarian(tanggal=tanggal)
        
        # Get list of CatatanHarian by date
        listOfCatatanHarian = entityHarian.getHarian(tanggal)
        return listOfCatatanHarian
    
    def addHarian(self, jam_mulai, jam_berakhir, nama_kegiatan, tanggal):
        # Create entity
        entityHarian = CatatanHarian(tanggal, jam_mulai, jam_berakhir, nama_kegiatan)
        
        # Add new CatatanHarian
        listOfCatatanHarian = entityHarian.save()
        return listOfCatatanHarian
    
    def editHarian(self, harianLama, jam_mulai, jam_berakhir, nama_kegiatan, tanggal):
        # Create entity
        entityHarian = CatatanHarian(tanggal,jam_mulai,jam_berakhir,nama_kegiatan)
        
        # Edit CatatanHarian
        listOfCatatanHarian = entityHarian.edit(harianLama.getJamMulai(), harianLama.getJamBerakhir(), harianLama.getKegiatan())
        return listOfCatatanHarian
    
    def deleteHarian(self, harian):
        # Create Entity
        entityHarian = harian
        
        # Delete CatatanHarian
        listOfCatatanHarian = entityHarian.delete()
        return listOfCatatanHarian
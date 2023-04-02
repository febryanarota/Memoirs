from PyQt5.QtSql import QSqlQuery
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
    
    def editHarian(self, jam_mulai_baru, jam_mulai_lama, jam_berakhir, nama_kegiatan, tanggal):
        # Create entity
        entityHarian = CatatanHarian(tanggal,jam_mulai_baru,jam_berakhir,nama_kegiatan)
        
        # Edit CatatanHarian
        listOfCatatanHarian = entityHarian.editHarian(tanggal,jam_mulai_lama)
        return listOfCatatanHarian
    
    def deleteHarian(self, jam_mulai,tanggal):
        # Create Entity
        entityHarian = CatatanHarian(tanggal= tanggal,jam_mulai = jam_mulai)
        
        # Delete CatatanHarian
        listOfCatatanHarian = entityHarian.deleteHarian()
        return listOfCatatanHarian
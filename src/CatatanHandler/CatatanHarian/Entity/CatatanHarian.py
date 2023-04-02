from PyQt5.QtSql import QSqlQuery

class CatatanHarian():
    # Constructor
    def __init__(self, tanggal = "", jam_mulai = "", jam_berakhir= "", nama_kegiatan= ""):
        self.tanggal = tanggal
        self.jam_mulai = jam_mulai
        self.jam_berakhir =jam_berakhir
        self.nama_kegiatan = nama_kegiatan
        
    # Get jam_mulai
    def getJamMulai(self):
        return self.jam_mulai
    
    # Get jam_berakhir
    def getJamBerakhir(self):
        return self.jam_berakhir
    
    # Get nama_kegiatan
    def getKegiatan(self):
        return self.nama_kegiatan
    
    def getTanggal(self):
        return self.tanggal
    
    def getHarian(self, tanggal):
        # Method to execute query get harian by Tanggal
        query = QSqlQuery()

        # Prepare and execute query
        query.prepare("SELECT * FROM catatan_harian WHERE tanggal = (?) ORDER BY jam_mulai ASC")
        query.addBindValue(tanggal)
        query.exec()

        # Iterate rows of query
        query.first()

        # Initialize list
        listOfCatatanHarian = []

        # Append each row
        for row in query.fetchall():
            listOfCatatanHarian.append(CatatanHarian(row.value(0), row.value(1), row.value(2), row.value(3)))
        
        # Return List of CatatanHarian
        return listOfCatatanHarian 
    
    def save(self):
        # TO DO (SAVE QUERY)
        query = QSqlQuery()

        # Prepare and execute query to insert a CatatanHarian
        query.prepare("INSERT INTO catatan_harian (tanggal, jam_mulai, jam_berakhir, nama_kegiatan) VALUES (?,?,?,?)")
        query.addBindValue(self.tanggal)
        query.addBindValue(self.jam_mulai)
        query.addBindValue(self.jam_berakhir)
        query.addBindValue(self.nama_kegiatan)
        query.exec()

        # Call a function to show all CatatanHarian
        listOfCatatanHarian = self.getHarian(self.tanggal)
        return listOfCatatanHarian
    
    def edit(self,jam_mulai_lama):
        # TO DO (EDIT QUERY)
        query = QSqlQuery()

        # Prepare and execute query to update a CatatanHarian
        query.prepare("UPDATE catatan_harian SET tanggal = (?), jam_mulai = (?), jam_berakhir = (?), nama_kegiatan = (?) WHERE tanggal = (?) AND jam_mulai = (?)")
        query.addBindValue(self.tanggal)
        query.addBindValue(self.jam_mulai)
        query.addBindValue(self.jam_berakhir)
        query.addBindValue(self.nama_kegiatan)
        query.addBindValue(self.tanggal)
        query.addBindValue(jam_mulai_lama)
        query.exec()

        # Call a function to show all CatatanHarian
        listOfCatatanHarian = self.getHarian(self.tanggal)
        return listOfCatatanHarian
    
    def delete(self):
        # TO DO (DELETE QUERY)
        query = QSqlQuery()

        # Prepare and execute query to delete a CatatanHarian
        query.prepare("DELETE FROM catatan_harian WHERE tanggal = (?) AND jam_mulai = (?)")
        query.addBindValue(self.tanggal)
        query.addBindValue(self.jam_mulai)
        query.exec()
        
        # Call a function to show all CatatanHarian
        listOfCatatanHarian = self.getHarian(self.tanggal)
        return listOfCatatanHarian
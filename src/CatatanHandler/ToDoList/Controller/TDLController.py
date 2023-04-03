from PyQt5.QtSql import QSqlQuery
from CatatanHandler.ToDoList.Entity.ToDoList import *

class TDLController():
    def showTDL(self, tanggal):
        # Create entity
        entityTDL = ToDoList()

        # Get TDL by date
        listOFTDL = entityTDL.getTDL(tanggal)
        return listOFTDL
    
    def addTDL(self, to_do, tanggal):
        # Create entity
        entityTDL = ToDoList(to_do, 0, tanggal)

        # Add new TDL
        return entityTDL.save()
    
    def editTDL(self, to_do_lama, to_do_baru, tanggal, done):
        # Create entity
        entityTDL = ToDoList(to_do_baru, done, tanggal)

        # Update edited TDL
        return entityTDL.edit(to_do_lama)
    
    def deleteTDL(self, to_do, tanggal):
        # Create entity
        entityTDL = ToDoList(to_do, 0, tanggal)

        # Update deleted TDL
        return entityTDL.delete()

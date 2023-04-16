from CatatanHandler.ToDoList.Entity.ToDoList import ToDoList

class TDLController():
    def showTDL(self, tanggal):
        # Create entity
        entityTDL = ToDoList()

        # Get TDL by date
        listOFTDL = entityTDL.getTDL(tanggal)
        return listOFTDL

    def addTDL(self, to_do, tanggal):
        # Create entity
        entityTDL = ToDoList(to_do, tanggal, 0)

        # Add new TDL
        return entityTDL.save()

    def editTDL(self, to_do_lama, to_do_baru, tanggal, done):
        # Create entity
        entityTDL = ToDoList(to_do_baru, tanggal, done)

        # Update edited TDL
        return entityTDL.edit(to_do_lama)

    def deleteTDL(self, to_do, tanggal):
        # Create entity
        entityTDL = ToDoList(to_do, tanggal, 0)

        # Update deleted TDL
        return entityTDL.delete()

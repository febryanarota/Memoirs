from CatatanHandler.CatatanTarget.Entity.CatatanTarget import *

class TargetController():
    def showTarget(self):
        entityTarget = CatatanTarget()
        listOfTarget = entityTarget.getAllTarget()
        return (listOfTarget)

    def addTarget(self, target, tanggal):
        entityTarget = CatatanTarget(target, tanggal)
        return (entityTarget.save())
    
    def editTarget(self, prev_target, new_target, tanggal):
        entityTarget = CatatanTarget(new_target, tanggal)
        return (entityTarget.edit(prev_target))
    
    def deleteTarget(self, target, tanggal):
        entityTarget = CatatanTarget(target, tanggal)
        return (entityTarget.delete())
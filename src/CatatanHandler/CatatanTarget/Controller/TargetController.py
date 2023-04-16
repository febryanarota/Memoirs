from CatatanHandler.CatatanTarget.Entity.CatatanTarget import CatatanTarget

class TargetController():
    def showTarget(self):
        # Return list of targets
        entityTarget = CatatanTarget()
        listOfTarget = entityTarget.getAllTarget()
        return (listOfTarget)

    def addTarget(self, target, tanggal):
        # Add new target
        entityTarget = CatatanTarget(target, tanggal)
        return (entityTarget.save())

    def editTarget(self, prev_target, new_target, tanggal):
        # Edit existing target
        entityTarget = CatatanTarget(new_target, tanggal)
        return (entityTarget.edit(prev_target))

    def deleteTarget(self, target, tanggal):
        # Delete selected target
        entityTarget = CatatanTarget(target, tanggal)
        return (entityTarget.delete())

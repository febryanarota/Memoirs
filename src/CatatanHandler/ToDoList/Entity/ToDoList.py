from PyQt5.QtSql import QSqlQuery

class ToDoList():
    def __init__(self, to_do = "", done = 0, tanggal = ""):
        self.to_do = to_do
        self.done = done
        self.tanggal = tanggal

    def getToDo(self):
        return self.to_do
    
    def getDone(self):
        return self.done
    
    def getTanggal(self):
        return self.tanggal

    def getTDL(self, tanggal):
        # Method to execute query get TDL by tanggal
        query = QSqlQuery()

        # Prepare and execute query
        query.prepare("SELECT * FROM to_do_list WHERE tanggal = (?)")
        query.addBindValue(tanggal)
        query.exec()

        listOfTDL = []
        while query.next():
            TDL = []
            for i in range(query.record().count()):
                TDL.append(query.value(i))
            listOfTDL.append(TDL)
        
        return listOfTDL

    def save(self):
        # Method to execute query insert to do list
        query = QSqlQuery()

        # Prepare and execute an INSERT query
        query.prepare("INSERT INTO to_do_list (to_do, done, tanggal) VALUES (?, ?, ?)")
        query.addBindValue(self.to_do)
        query.addBindValue(0)
        query.addBindValue(self.tanggal)
        query.exec()

        # Execute query to retrieve the updated to do list
        newListOfTDL = self.getTDL(self.tanggal)

        return newListOfTDL
    
    def edit(self, to_do_lama):
        # Method to execute query update to do list

        query = QSqlQuery()

        # Prepare and execute an UPDATE query
        query.prepare("UPDATE to_do_list SET to_do = (?), done = (?), tanggal = (?) WHERE to_do = (?) AND done = (?) AND tanggal = (?)")
        query.addBindValue(self.to_do)
        query.addBindValue(self.done)
        query.addBindValue(self.tanggal)
        query.addBindValue(to_do_lama.to_do)
        query.addBindValue(to_do_lama.done)
        query.addBindValue(to_do_lama.tanggal)

        # Execute query to retrieve the updated to do list
        newListOfTDL = self.getTDL(self.tanggal)

        return newListOfTDL
        
    def delete(self):
        # Method to execute query delete to do list

        query = QSqlQuery()

        # Prepare and execute an DELETE query
        query.prepare("DELETE from to_do_list WHERE tanggal = (?) AND to_do = (?)")
        query.addBindValue(self.tanggal)
        query.addBindValue(self.to_do)
        
        # Execute query to retrieve the updated to do list
        newListOfTDL = self.getTDL(self.tanggal)

        return newListOfTDL

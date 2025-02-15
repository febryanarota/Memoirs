from PyQt5.QtSql import QSqlQuery

class Artikel():
    # Constructor
    def __init__(self, title = "", content = "", image = ""):
        self.title = title
        self.content = content
        self.image = image

    # Getter
    def getTitle(self):
        return self.title

    def getContent(self):
        return self.content

    def getImage(self):
        return self.image

    def getListArtikel(self):
        # Method to execute query get All Artikel
        query = QSqlQuery()

        # Execute query
        query.exec("SELECT * FROM article")

        # Construct list of all article
        listOfArtikel = []

        while query.next():
            listOfArtikel.append(Artikel(query.value(0), query.value(1), query.value(2)))

        return listOfArtikel
 
    def getArtikel(self):
        # Method to execute query get Artikel by title
        query = QSqlQuery()

        # Prepare and execute query
        query.prepare("SELECT * FROM artikel WHERE title = (?)")
        query.addBindValue(self.title)
        query.exec()

        return Artikel(query.value(0), query.value(1), query.value(2))

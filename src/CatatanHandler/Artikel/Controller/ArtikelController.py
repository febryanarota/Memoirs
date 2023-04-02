from CatatanHandler.Artikel.Entity.Artikel import *

class ArtikelController():
    def showArtikel(self):
        # Create entity
        entityArtikel = Artikel()

        # Get All Artikel
        listOfArtikel = entityArtikel.getListArtikel()

        return listOfArtikel
    
    def showArtikelDetail(self, title):
        # Create entity
        entityArtikel = Artikel(title)

        # Get All Artikel
        artikel = entityArtikel.getArtikel()

        return artikel
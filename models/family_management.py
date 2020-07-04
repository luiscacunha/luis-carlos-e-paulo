"""
    Esta class é reponsavel pela getão dos objectos relacionados com familia.
"""

from models.family import family

class familyManagement:
    familyList = []

    def has_family(self,family_name):
      #Verifica se já existe familia.
        if family_name in self.familyList:
            return True
        return False

    def add_family(self,family_name):
        #Adiciona familia
        newFamily = family(family_name)
        self.familyList.append(newFamily)
    
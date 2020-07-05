"""
    Esta class é reponsavel pela gestão dos objectos relacionados com familia.
"""

from models.family import family

class familyManagement:
    familyList = []

    def has_family(self,family_name):
      #Verifica se já existe familia.
        for family in self.familyList:
            if family.family_name == family_name:
                return True
        return False

    def add_family(self,family_name):
        #Adiciona familia
        newFamily = family(family_name)
        self.familyList.append(newFamily)
        if len(self.familyList) >1:
            self.sort_families()

    
    def has_families(self):
        if len(self.familyList) == 0:
            return False
        return True
    
    def show_families(self):
        #Mostrar todas as familias por ordem alfabética.
        for family in self.familyList:
            print(family.family_name)

    def sort_families(self):
        for i in range(len(self.familyList)):
            for j in range(len(self.familyList)-i-1):
                if self.familyList[j].family_name > self.familyList[j+1].family_name:
                    tmp = self.familyList[j]
                    self.familyList[j] = self.familyList[j+1]
                    self.familyList[j+1] = tmp
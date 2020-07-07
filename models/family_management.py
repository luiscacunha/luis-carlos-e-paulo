"""
    Esta class é reponsavel pela gestão dos objectos relacionados com familia.
"""

from models.family import family

class familyManagement:
    familyList = []
    unknown_Family = []
    
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
            print ("{}.".format (family.family_name))

    def show_family(self,family_name):
        for family in self.familyList:
            if family.family_name == family_name:
                family_shown = family
                self.sort_familyMembers(family_shown.family_members)
                self.sort_age(family_shown.family_members)
                for user in family_shown.family_members:
                    print ("{} {}.".format (user.age,user.name))                

    def sort_families(self):
        for i in range(len(self.familyList)):
            for j in range(len(self.familyList)-i-1):
                if self.familyList[j].family_name > self.familyList[j+1].family_name:
                    tmp = self.familyList[j]
                    self.familyList[j] = self.familyList[j+1]
                    self.familyList[j+1] = tmp
    
    def sort_familyMembers(self,family):
        for i in range(len(family)):
            for j in range(len(family)-i-1):
                if family[j].name > family[j+1].name:
                    tmp = family[j]
                    family[j] = family[j+1]
                    family[j+1] = tmp

    def sort_age(self,family):
        ages = ["Jovem","Adulto","Idoso"]
        for i in range(len(family)):
            for j in range(len(family)-i-1):
                if ages.index(family[j].age) > ages.index(family[j+1].age):
                    tmp = family[j]
                    family[j] = family[j+1]
                    family[j+1] = tmp

    def all_family_members_list(self):
        families = list()
        for family in familyManagement.familyList:
            if len(family.family_members) > 0:
                families += family.family_members
        familyManagement.sort_familyMembers(self,families)
        familyManagement.sort_age(self,families)
        return families
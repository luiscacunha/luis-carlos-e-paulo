
"""
    Esta class é responsavel pela gestão dos objectos relacionados com
    os utentes.
"""
from models.user import user
from models.family_management import familyManagement
from models.category import category
from models.category_manager import categoryManagement

class UserManagement:
    userList = []
    categoria = category ()
     # retorna True se o nome do utente já existir na lista,
    # caso contrario retorna False
    def has_user(self,name):
        for user in self.userList:
            if user.name == name:
                return True
        return False

    #retorna True se a faixa etária existe.
    def has_age_range(self,age_range):
        if age_range in ["Jovem","Adulto","Idoso"]:
            return True
        return False

    def add_user(self,name,age_range):
        #Adiciona utente, utente tem uma faixa etária e um nome
        newUser = user(name,age_range)
        self.userList.append(newUser)
        familyManagement.unknown_Family.append(name)
    
    def disassociate_user(self,user_name):
        #Desassocia utente de familia
        for user in self.userList:
            if user_name == user.name:
                for i in range(len(familyManagement.familyList)-1):
                    if familyManagement.familyList[i].family_name == user.family:
                        del (familyManagement.familyList[i])
                        familyManagement.unknown_Family.append(user)
                        self.sort_familyMembers(familyManagement.unknown_Family)
                user.family= None

    def associate_family(self,user_name,family_name):
        #Associa um utente a uma familia
        for user in self.userList:
            if user_name == user.name:
                user.family= family_name    
                for i in range(len(familyManagement.familyList)-1):
                    if familyManagement.familyList[i].family_name == family_name:
                        familyManagement.familyList[i].family_members.append(user)
                        del (familyManagement.unknown_Family[i])

    def user_have_family(self,user_name):
        #Verifica se utente pertence à uma familia.
        for user in self.userList:
            if user_name == user.name:
                if user.family == None:
                    return False
                return True

    def has_users(self):
        #Verifica se lista de utentes está vázia
        if len(self.userList) == 0:
            return False
        return True

    def show_users (self):
        #Mostrar os utentes em ordem alfabetica
        all_users = self.sort_family_age(self.sort_familyMembers(self.all_family_members_list()))
        for user in all_users:
            user.toString()

    def sort_familyMembers(self,family):
        for i in range(len(family)):
            for j in range(len(family)-i-1):
                if family[j].name > family[j+1].name:
                    tmp = family[j]
                    family[j] = family[j+1]
                    family[j+1] = tmp

    def sort_family_age(self,family):
        ages = ["Jovem","Adulto","Idoso"]
        for i in range(len(family)):
            for j in range(len(family)-i-1):
                if ages.index(family[j].age) > ages.index(family[j+1].age):
                    tmp = family[j]
                    family[j] = family[j+1]
                    family[j+1] = tmp

    def all_family_members_list(self):
        for family in familyManagement.familyList:
            families += family
        self.sort_familyMembers(families)
        self.sort_family_age(families)
        return families
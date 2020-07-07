
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
    integrantes_scheduled = []

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
        familyManagement.unknown_Family.append(newUser)
    
    def disassociate_user(self,user_name):
        #Desassocia utente de familia
        for user in self.userList:
            if user_name == user.name:
                for i in range(len(familyManagement.familyList)-1):
                    if familyManagement.familyList[i].family_name == user.family:
                        del (familyManagement.familyList[i])
                        familyManagement.unknown_Family.append(user)
                user.family= None

    def associate_family(self,user_name,family_name):
        #Associa um utente a uma familia
        for user in self.userList:
            if user_name == user.name:
                user.family= family_name    
                for i in range(len(familyManagement.familyList)):
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
        all_users = familyManagement.all_family_members_list(self)
        familyManagement.sort_familyMembers(self,all_users)
        familyManagement.sort_age(self,all_users)
        for user in all_users:
            print(user.toString())
        familyManagement.sort_familyMembers(self,familyManagement.unknown_Family)          
        familyManagement.sort_age(self,familyManagement.unknown_Family)
        for user in familyManagement.unknown_Family:
            print ("{} {}.".format (user.age,user.name))

    def has_scheduled(self,name):
        for user in self.userList:
            if name == user.name:
                if len(user.scheduled) == 0 :
                    return False
                return True

    def has_scheduled_members (self, family_name): # devia estar no family_management mas nao consigo fazer o import do user_management
        integrantes = 0
        for family in familyManagement.familyList:
            if family_name == family.family_name:
                integrantes = len(family.family_members)
                for i in range (integrantes):
                    familiar = family.family_members[i]
                    if self.has_scheduled(familiar.name):
                        self.integrantes_scheduled.append (family.family_members[i])
        if len (self.integrantes_scheduled) == 0:
            return False
        else:
            return True

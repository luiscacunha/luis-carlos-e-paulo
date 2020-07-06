
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
    
    def disassociate_user(self,user_name):
        #Desassocia utente de familia
        for user in self.userList:
            if user_name == user.name:
                for family in familyManagement.familyList:
                    if family.family_name == user.family:
                        family.family_members.append(user.family)
                user.family= None

    def associate_family(self,user_name,family_name):
        #Associa um utente a uma familia
        for user in self.userList:
            if user_name == user.name:
                user.family= family_name    
                for family in familyManagement.familyList:
                    if family.family_name == family_name:
                        family.family_members.append(user_name)

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
        for user in self.userList:
            if self.user_has_family (user.name):
                print ("encontrei")
            else:
                print ("vamos seguir em frente")
                
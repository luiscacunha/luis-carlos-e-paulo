
"""
<<<<<<< HEAD
    Esta class é responsavel pela gestão dos objectos relacionados com
=======
    Esta class é reponsavel pela gestão dos objectos relacionados com
>>>>>>> 332a12045f9990c54a9a15b4406336d1e99d6482
    os utentes.
"""
from models.user import user

class UserManagement:
    userList = []
    
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
    
    def disassociate_family(self,user_name):
        #Desassocia utente de familia
        for user in self.userList:
            if user_name == user.name:
                user.family= None

    def associate_family(self,user_name,family_name):
        #Associa um utente a uma familia
        for user in self.userList:
            if user_name == user.name:
                user.family= family_name

    def user_have_family(self,user_name):
        #Verifica se utente pertence à uma familia.
        for user in self.userList:
            if user_name == user.name:
                if user.family == None:
                    return True
                return False

    def has_users(self):
        #Verifica se lista de utentes está vázia
        if len(self.userList) == 0:
            return False
        return True


                

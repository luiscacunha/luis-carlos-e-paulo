
"""
    Esta class é reponsavel pela getão dos objectos relacionados com
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

   def has_age_range(self,age_range):
      #Verifica se existe faixa etária
      pass

   def add_user(self,name,age_range):
      #Adiciona utente, utente tem uma faixa etária e um nome
      pass
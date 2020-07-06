"""
    Esta class é reponsavel pela gestão dos objectos relacionados com as marcações.
"""
from models.user_management import UserManagement
from models.user import user
from models.service import service
from models.scheduled import scheduled
from models.services_Manager import serviceManagement
from models.professional import professional

class scheduledManagment:
    def add_scheduled(self,professionals,name):
        for user in UserManagement.userList:
            if name == user.name:
                newscheduled = scheduled(user,professionals[2],professional(professionals[0],professionals[1]))
                user.scheduled.append(newscheduled)

    def show_user_scheduled(self,name):
      """
      Mostrar listagem de todos os profissionais de saúde associados a marcações do utente, de acordo com o serviço da marcação, e a sua categoria)
      Serviço˽Categoria˽NomeProfissional.↵
      """
      for user in UserManagement.userList:
            if name == user.name:
                for scheduled in user.scheduled:
                    print(scheduled.toString("LCU"))
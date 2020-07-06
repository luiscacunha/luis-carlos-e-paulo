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
        i = 0
        for user in UserManagement.userList:
            if name == user.name:
                for scheduledProfessional in professionals:
                    newscheduled = scheduled(user,scheduledProfessional[2],professional(scheduledProfessional[0],scheduledProfessional[1]))
                    UserManagement.userList[i].scheduled.append(newscheduled)
            i+=1


    def show_user_scheduled(self,name):
      """
      Mostrar listagem de todos os profissionais de saúde associados a marcações do utente, de acordo com o serviço da marcação, e a sua categoria)
      Serviço˽Categoria˽NomeProfissional.↵
      """
      for user in UserManagement.userList:
            if name == user.name:
                for scheduled in user.scheduled:
                    print("%s %s %s." %(scheduled.service, scheduled.professional.category,scheduled.professional.name))
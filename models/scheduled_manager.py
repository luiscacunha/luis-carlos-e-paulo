"""
    Esta class é reponsavel pela gestão dos objectos relacionados com as marcações.
"""
from models.user_management import UserManagement
from models.user import user
from models.service import service
from models.scheduled import scheduled
from models.services_Manager import serviceManagement
from models.professional import professional
from models.professional_management import professionalManagement
from models.family_management import familyManagement

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
        Mostrar listagem de todos os profissionais de saúde associados a marcações do utente, de acordo com o serviço da marcação, 
        e a sua categoria)
        Serviço˽Categoria˽NomeProfissional.↵
        """
        for user in UserManagement.userList:
            if name == user.name:
                self.sort_user_scheduled(user.scheduled)
                for scheduled in user.scheduled:
                    print(scheduled.toString("LCU"))
    
    def sort_user_scheduled(self,userscheduledList):
        services = ["Consulta","Enfermagem","PequenaCirurgia"]
        categories = ["Medicina","Enfermagem","Auxiliar"]
        for i in range(len(userscheduledList)):
            for j in range(len(userscheduledList)-i-1):
                if services.index(userscheduledList[j].service) > services.index(userscheduledList[j+1].service):
                    tmp = userscheduledList[j]
                    userscheduledList[j] = userscheduledList[j+1]
                    userscheduledList[j+1] = tmp
                else:
                    if categories.index(userscheduledList[j].professional.category) > categories.index(userscheduledList[j+1].professional.category):
                        tmp = userscheduledList[j]
                        userscheduledList[j] = userscheduledList[j+1]
                        userscheduledList[j+1] = tmp
    
    def cancel_user_scheduled (self, name):
        for i in range (len (UserManagement.userList)):
            if UserManagement.userList[i].name == name:
                UserManagement.userList[i].scheduled = []
    
    def show_family_scheduled(self, family_name):
        scheduled_familiares = UserManagement.integrantes_scheduled
        familyManagement.sort_age (self, scheduled_familiares)
        familyManagement.sort_familyMembers (self, scheduled_familiares)     
        for i in range (len (scheduled_familiares)):
            professionalManagement.sort_professionals (self,scheduled_familiares[i].scheduled)
            for schedules in scheduled_familiares[i].scheduled:
                print("{} {}".format(scheduled_familiares[i].name,schedules.toString("LCU")))

    def has_scheduled_professional (self, category, professional_name): # vou fazer mais tarde um ciclo utilizando range para aceder bem os condimnetos
        apointments = 0 # beijos vou dormir
        apointmentList = []
        for user in UserManagement.userList:
            print (user.scheduled[0].professional.name)
            print (user.scheduled.professional)
            if user.scheduled.professional.name == professional_name and user.scheduled.professional.category == category:
                apointments += apointments
                apointmentList.append (user.scheduled)
        print (apointments)
        print (apointmentList)


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
    def add_scheduled(self,services_to_schedule,name):
        i = 0
        for user in UserManagement.userList:
            if name == user.name:
                for scheduledProfessional in services_to_schedule:
                    newscheduled = scheduled(user,scheduledProfessional[2],professional(scheduledProfessional[0],scheduledProfessional[1]))
                    UserManagement.userList[i].scheduled.append(newscheduled)
                    self.add_scheduled_professional(newscheduled)
            i+=1

    def add_scheduled_professional(self,newscheduled):
        for p in professionalManagement.professionalList:
            if p.category == newscheduled.professional.category and p.name == newscheduled.professional.name:
                p.scheduled.append(newscheduled)

    def has_scheduled_professional (self, category, professional_name): 
        for professional in professionalManagement.professionalList:
            if professional.name == professional_name and professional.category == category:
                if len(professional.scheduled) >0 :
                    return True
                else:
                    return False

    def cancel_user_scheduled (self, name):
        for i in range (len (UserManagement.userList)):
            if UserManagement.userList[i].name == name:
                self.cancel_professional_scheduled(UserManagement.userList[i].scheduled)
                UserManagement.userList[i].scheduled = []

    def cancel_professional_scheduled(self,scheduleds):
        for s in scheduleds:
            for p in professionalManagement.professionalList:
                if s.professional.name == p.name:
                    for professionalScheduled in p.scheduled:
                        if professionalScheduled.user.name == s.user.name:
                            p.scheduled.remove(professionalScheduled)

    def show_user_scheduled(self,name):
        for user in UserManagement.userList:
            if name == user.name:
                self.sort_user_scheduled(user.scheduled)
                for scheduled in user.scheduled:
                    print(scheduled.toString("LCU"))    
    
    def show_family_scheduled(self, family_name):
        scheduled_familiares = UserManagement.integrantes_scheduled
        familyManagement.sort_age (self, scheduled_familiares)
        familyManagement.sort_familyMembers (self, scheduled_familiares)     
        for i in range (len (scheduled_familiares)):
            professionalManagement.sort_professionals (self,scheduled_familiares[i].scheduled)
            for schedules in scheduled_familiares[i].scheduled:
                print(schedules.toString("LCF"))

    def show_professional_scheduled(self,category,name):
        for professional in professionalManagement.professionalList:
            if professional.name == name and professional.category == category:
                self.sort_professional_scheduled(professional.scheduled)
                for schedules in professional.scheduled:
                    print(schedules.toString("LSP"))

    
    def sort_professional_scheduled(self,professionalScheduled):
        services = ["Consulta","Enfermagem","PequenaCirurgia"]
        for i in range(len(professionalScheduled)):#ordena por ordem alfabetica
            for j in range(len(professionalScheduled)-i-1):
                if professionalScheduled[j].user.name > professionalScheduled[j+1].user.name:
                                tmp = professionalScheduled[j]
                                professionalScheduled[j] = professionalScheduled[j+1]
                                professionalScheduled[j+1] = tmp
        for i in range(len(professionalScheduled)):#ordena por service
            for j in range(len(professionalScheduled)-i-1):
                if services.index(professionalScheduled[j].service) > services.index(professionalScheduled[j+1].service):
                    tmp = professionalScheduled[j]
                    professionalScheduled[j] = professionalScheduled[j+1]
                    professionalScheduled[j+1] = tmp
    
    def sort_scheduled (self, Scheduled):
        categories = ["Medicina","Enfermagem","Auxiliar"]
        for i in range(len(Scheduled)):#ordena por ordem alfabetica de professional
            for j in range(len(Scheduled)-i-1):
                if Scheduled[j].professional.name > Scheduled[j+1].professional.name:
                                tmp = Scheduled[j]
                                Scheduled[j] = Scheduled[j+1]
                                Scheduled[j+1] = tmp
        for i in range(len(Scheduled)):#ordena por categoria
            for j in range(len(Scheduled)-i-1):
                if categories.index(Scheduled[j].professional.category) > categories.index(Scheduled[j+1].professional.category):
                    tmp = Scheduled[j]
                    Scheduled[j] = Scheduled[j+1]
                    Scheduled[j+1] = tmp
        for i in range(len(Scheduled)):#ordena por ordem alfabetica de utente
            for j in range(len(Scheduled)-i-1):
                if Scheduled[j].user.name > Scheduled[j+1].user.name:
                                tmp = Scheduled[j]
                                Scheduled[j] = Scheduled[j+1]
                                Scheduled[j+1] = tmp

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
    
    def show_service_scheduled (self):
        scheduledList = serviceManagement.scheduledList
        self.sort_scheduled(scheduledList)
        for schedules in scheduledList:
                    print(schedules.toString("LMS"))
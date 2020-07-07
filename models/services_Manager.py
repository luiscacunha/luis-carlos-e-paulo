"""
    Esta class é reponsavel pela gestão dos objectos relacionados com serviços.
"""
from models.service import service
from models.professional import professional
from models.professional_management import professionalManagement

class serviceManagement:
    scheduledList = []

    def has_services(self,listServices):
        for service_to_scheduled in listServices:
            if self.has_service(service_to_scheduled) == False:
                return False
        return True
        
    def has_service(self,service):
        if service in ["Consulta","Enfermagem","PequenaCirurgia"]:
            return True
        return False

    def canDoit(self,category,service):
        if category == "Medicina" and service in ["Consulta","PequenaCirurgia"]:
            return True
        elif category in ["Enfermagem","Auxiliar"] and service in ["PequenaCirurgia","Enfermagem"]:
            return True 
        else:
            return False
              
    def has_scheduled_service (self,service):
        scheduled_service = 0
        for professional in professionalManagement.professionalList:
            for schedules in professional.scheduled:
                if schedules.service == service:
                    self.scheduledList.append (schedules)
                    scheduled_service = scheduled_service + 1
        if scheduled_service == 0:
            return False
        return True
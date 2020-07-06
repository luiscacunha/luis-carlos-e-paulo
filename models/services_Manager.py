"""
    Esta class é reponsavel pela gestão dos objectos relacionados com serviços.
"""
from models.service import service

class serviceManagement:
    def has_services(self,listServices):
        for service in listServices:
            if service.has_service(self,service) == False:
                return False
        return True

        
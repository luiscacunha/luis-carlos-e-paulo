""" 
    Esta class representa o objecto que contem todos os atributos
    relativos a uma marcação.
"""
from models.user import user
from models.professional import professional
from models.family import family

class scheduled():
    def __init__(self,user,service,professional):
        self.service = service
        self.professional = professional
        self.user = user

    def toString(self,typeofList):
        if "LCU" == typeofList:
            return "%s %s %s." %(self.service, self.professional.category,self.professional.name)

        
"""
class familyScheduled():
    pass

class professionalScheduled():
    pass

class serviceScheduled():
    pass
"""
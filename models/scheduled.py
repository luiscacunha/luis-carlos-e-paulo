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
        elif "LCF" == typeofList:
            return "%s %s %s %s." %(self.user.name,self.service, self.professional.category,self.professional.name)
        elif "LCP" == typeofList:
            return "%s %s." %(self.service ,self.user.name)

        
"""
class familyScheduled():
    pass

class professionalScheduled():
    pass

class serviceScheduled():
    pass
"""
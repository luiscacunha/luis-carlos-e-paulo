""" 
    Esta class representa o objecto que contem todos os atributos
    relativos a um serviço.
"""
class service:
    def __init__(self):
        self.nursing = []
        self.smallSurgery = []
        self.appointment = []

    def has_service(self,service):
        if service in ["Consulta","Enfermagem","Enfermagem"]:
            return True
        return False

    def canDoit(self,category,service):
        if category == "Medicina" and service in ["Consulta","PequenaCirurgia"]:
            return True
        elif category in ["Enfermagem","Auxiliar"] and service in ["PequenaCirurgia","Enfermagem"]:
            return True 
        else:
            return False
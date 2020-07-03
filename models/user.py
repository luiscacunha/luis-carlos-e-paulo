""" 
    Esta class representa o objecto que contem todos os atributos
    relativos a um utente.
"""
class user:
    def __init__(self,name,age,family):
        self.family = family
        self.age = age
        self.name = name


    def get_family(self):
        return self.family

""" 
    Esta class representa o objecto que contem todos os atributos
    relativos a um utente.
    User são criados sem familia associada.
"""
family = None # User começa sem familia associada.

class user:
    def __init__(self,name,age):
        self.family = family
        self.age = age
        self.name = name

    def toString(self):
      return "%s %s %s" %(self.family, self.age,self.name)


"""
    Esta class é responsavel pela gestão dos objectos relacionados com profissional.
"""

from models.professional import professional
from models.category_manager import categoryManagement
class professionalManagement:
    professionalList = []
    
    def has_professional(self,name,category):
        #Verifica se existe profissional já registado
        if name in self.professionalList:
            return True
        return False 

    def add_profissional(self,name,category):
        #Adiciona profissional de saúde
        newProfessional = professional(name,category)
        self.professionalList.append(newProfessional)
        categoryManagement.add_professional_in_category(category,name)
        

    def has_professionals(self):
      #Verificar se lista de profissionais está vázia
        if len(self.professionalList) == 0:
            return True
        return False

    def show_professionals(self):
      #Mostrar profissionals "Categoria_Nome", por ordem alfabética dentro de cada categoria
      pass

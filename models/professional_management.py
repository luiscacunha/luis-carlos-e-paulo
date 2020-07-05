"""
    Esta class é responsavel pela gestão dos objectos relacionados com profissional.
"""

from models.professional import professional
from models.category_manager import categoryManagement
from models.category import category

class professionalManagement:
    professionalList = []
    categoria = category()    
    
    def has_professional(self,name,category_name):
        #Verifica se existe profissional já registado
        for professional in self.professionalList:
            if name == professional.name:
                return True
        return False 

    def add_profissional(self,name,category_name):
        #Adiciona profissional de saúde
        newProfessional = professional(name,category_name)
        self.professionalList.append(newProfessional)
        self.add_professional_in_category(category_name,name,self.categoria)
        

    def has_professionals(self):
      #Verificar se lista de profissionais está vázia
        if len(self.professionalList) == 0:
            return True
        return False

    def show_professionals(self):
      #Mostrar profissionals "Categoria_Nome", por ordem alfabética dentro de cada categoria
      pass
  
    def add_professional_in_category(self,category_name,name,categoria):
        if category_name == "Medicina":
            categoryManagement.add_medicine(self,name,categoria)
        elif category_name == "Auxiliar":
            categoryManagement.add_helper(self,name,categoria)
        else:
            categoryManagement.add_nursing(self,name,categoria)
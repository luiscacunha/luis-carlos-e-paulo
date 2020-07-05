
"""
    Esta class é reponsavel pela gestão dos objectos relacionados com
    as cateregorias.
"""
from models.category import category

class categoryManagement:

    def has_category(self,Category):
        if Category in ["Medicina","Enfermagem","Auxiliar"]:
            return True
        return False
    
    def add_medicine(self,name,categoria):
        categoria.medicine.append(name)

    def add_nursing(self,name,categoria):
        categoria.nursing.append(name)

    def add_helper(self,name,categoria):
        categoria.helper.append(name)

    def has_helper(self,name,categoria):
        if name in categoria.helper:
            return True
        return False

    def has_medicine(self,name):
        if name in categoria.medicine:
            return True
        return False
        
    def has_nursing(self,name):
        if name in categoria.nursing:
            return True
        return False

 
            
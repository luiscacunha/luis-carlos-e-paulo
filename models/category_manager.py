
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
    
    def has_categories(self,categoriesList):
        for category in categoriesList:
            if self.has_category(category) == False:
                return False
        return True
    
    def add_medicine(self,name,categoria):
        categoria.medicine.append(name)
        #self.sort_categorys(categoria.medicine)

    def add_nursing(self,name,categoria):
        categoria.nursing.append(name)
        #self.sort_categorys(categoria.nursing)

    def add_helper(self,name,categoria):
        categoria.helper.append(name)
        #self.sort_categorys(categoria.helper)

    def has_helper(self,name,categoria): 
        for helper in categoria.helper:
            if name ==  helper:
                return True
            return False

    def has_medicine(self,name,categoria):
        for medicine in categoria.medicine:
            if name ==  medicine:
                return True
            return False
        
    def has_nursing(self,name,categoria):
        for nursing in categoria.nursing:
            if name ==  nursing:
                return True
            return False

    def sort_categorys(self,categorylist):
        for i in range(len(categorylist)):
            for j in range(len(categorylist)-i-1):
                if categorylist[j] > categorylist[j+1]:
                    tmp = categorylist[j]
                    categorylist[j] = categorylist[j+1]
                    categorylist[j+1] = tmp
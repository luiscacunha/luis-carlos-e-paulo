
"""
    Esta class é reponsavel pela gestão dos objectos relacionados com
    as cateregorias.
"""
from models.category import category

class categoryManagement:
        def has_category(self,category):
            if category in ["Medicina","Enfermagem","Auxiliar"]:
                return True
            return False

        def add_medicine(self,name):
            category.medicine.append(name)

        def add_nursing(self,name):
            category.nursing.append(name)

        def add_helper(self,name):
            category.helper.append(name)

        def has_helper(self,name):
            if name in category.helper:
                return True
            return False

        def has_medicine(self,name):
            if name in category.medicine:
                return True
            return False
        
        def has_nursing(self,name):
            if name in category.nursing:
                return True
            return False

        def add_professional_in_category(self,category,name):
            if category == "Medicina":
                self.add_medicine(name)
            elif category == "Auxiliar":
                self.add_helper(name)
            else:
                self.add_nursing(name)
            
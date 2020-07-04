from models.professional_management import professionalManagement
from models.user_management import UserManagement
from models.family_management import familyManagement
from models.category_manager import categoryManagement
from controllers.task_list_controller import TaskListController


class HM:
   def __init__(self):
      controller = TaskListController()
      pm = professionalManagement()
      fm = familyManagement()
      um = UserManagement()
      cm = categoryManagement()
      while True:
         line = input()
         if not line:
            exit(0)
         commands = line.split(" ")
         if commands[0] == "RP":
            self.commandRP(commands,pm,cm)
         elif commands[0] == "RU":
            self.commandRU(commands,um)
         elif commands[0] == "RF":
            self.commandRF(commands)
         elif commands[0] == "AF":
            self.commandAF(commands)
         elif commands[0] == "DF":
            self.commandDF(commands)
         elif commands[0] == "LP":
            self.commandLP()
         elif commands[0] == "LU":
            self.commandLU()
         elif commands[0] == "LF":
            self.commandLF(lm)
         elif commands[0] == "MF":
            self.commandMF(commands)
         elif commands[0] == "MC":
            self.commandMC(commands)
         elif commands[0] == "CC":
            self.commandCC(commands)
         elif commands[0] == "LCU":
            self.commandLCU(commands)
         elif commands[0] == "LCF":
            self.commandLCF(commands)   
         elif commands[0] == "LSP":
            self.commandLSP(commands)         
         elif commands[0] == "LMS":
            self.commandLMS(commands)              
         else:
            print("Instrução inválida.")
   
   def commandRP(self,commands,pm,cm):
   #Regista profissional
      category = commands[1]
      name = commands[2]
      if cm.has_category(category):
         if pm.has_professional(name,category):
            print("Profissional existente.")
         else:
            pm.add_profissional(name,category)
            print("Profissional registado com sucesso.")
      else:
         print("Categoria inexistente.")
   
   def commandRU(self,commands,um):
   #Registar utente
      name = commands[1]
      age_range= commands[2]
      if um.has_user(name):
         print("Utente existente.")
      else:
         if um.has_age_range(age_range):
            um.add_user(name,age_range)
            print("Utente registado com sucesso.")
         else:
            print("Faixa etária inexistente.")
            
   def commandRF(self,commands):
   #Registar família
      family_name = commands[1]
      if fm.has_family(family_name):
         print("Família existente.")
      else:
         fm.add_family(family_name)
         print("Família registada com sucesso.")
   
   def commandAF(self,commands):
   #Associar utente a família 
      user_name = commands[1]
      family_name = commands[2]
      if um.has_family(family_name):
         if um.has_user(user_name):
            if not um.user_have_family(user_name):
               um.associate_family(user_name,family_name)
               print("Utente associado a família.")
            else:
               print("Utente pertence a família.")
         else:
            print("Utente inexistente.")
      else:
         print("Família inexistente.")
   
   def commandDF(self,commands):
   #Desassociar utente de famíla
      user_name = commands[1]
      if um.has_user(user_name):
         if um.user_have_family(user_name):
            um.disassociate_user(user_name)
            print("Utente desassociado de família.")
         else:
            print("Utente não pertence a família.")
      else:
         print("Utente inexistente.")
   
   
   def commandLP(self):
   #Listar profissionais
      if pm.has_professionals():
         pm.show_professionals()
      else:
         print("Sem profissionais registados.")
   
   def commandLU(self):
   #Listar utentes
      if controller.has_users():
         controller.show_users()
      else:
         print("Sem utentes registados.")
   
   
   def commandLF(self,lm):
   #Listar famílias
      if lm.has_families():
         lm.show_families()
      else:
         print("Sem famílias registadas.")
   
   def commandMF(self,commands):
   #Mostrar família
      family_name = commands[1]
      if controller.has_family(family_name):
         controller.show_family(family_name)
      else:
         print("Família inexistente.")
   
   def commandMC(self,commands):
   #Marcar cuidados a utente
      pass
   
   def commandCC(self,commands):
   #Cancelar cuidados marcados a utente
      name = commands[1]
      if controller.has_user(name):
         if controller.has_scheduled(name,"utente"):
            controller.cancel_user_scheduled(name)
            print("Cuidados de saúde desmarcados com sucesso.")
         else:
            print("Utente sem cuidados de saúde marcados.")
      else:
         print("Utente inexistente.")
   
   def commandLCU(self,commands):
   #Listar cuidados marcados a utente
      name = commands[1]
      if controller.has_user(name):
         if controller.has_scheduled(name,"utente"): 
            controller.show_user_scheduled(name)
         else:
            print("Utente sem cuidados de saúde marcados.")
      else:
         print("Utente inexistente.")
   
   def commandLCF(self,commands):
   #Listar cuidados marcados a família  
      family_name = commands[1]
      if controller.has_family(family_name):
         if controller.has_scheduled(family_name,"família"): 
            controller.show_family_scheduled(family_name)
         else:
            print("Familia sem cuidados de saúde marcados.")
      else:
         print("Família inexistente.")
   
   def commandLSP(self,commands):
   #Listar serviços marcados a profissional 
      category = commands[1]
      professional_name = commands[2]
      if controller.has_professional(professional_name,category):
         if controller.has_scheduled(professional_name,"profissional"):
            controller.show_professional_scheduled(professional_name)
         else:
            print("Profissional de saúde sem marcações.")
      else:
         print("Profissional de saúde inexistente.")
   
   def commandLMS(self,commands):
   #Listar marcações por tipo de serviço
      service = commands[1]
      if controller.has_service(service):
         if controller.has_scheduled(service,"serviço"):
            controller.show_service_scheduled()
         else:
            print("Serviço sem marcações.")
      else:
         print("Serviço inexistente.")

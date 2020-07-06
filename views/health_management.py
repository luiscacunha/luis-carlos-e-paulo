from models.professional_management import professionalManagement
from models.user_management import UserManagement
from models.family_management import familyManagement
from models.category_manager import categoryManagement
from models.services_Manager import serviceManagement
from controllers.task_list_controller import TaskListController

class HM:
   def __init__(self):
      #controller = TaskListController()
      pm = professionalManagement()
      fm = familyManagement()
      um = UserManagement()
      cm = categoryManagement()
      sm = serviceManagement()
      controllers = {"Professional":pm,"Family":fm,"User":um,"Category":cm,"Service":sm}
      while True:
         line = input()
         if not line:
            exit(0)
         commands = line.split(" ")
         if commands[0] == "RP":
            self.commandRP(commands,controllers)
         elif commands[0] == "RU":
            self.commandRU(commands,controllers)
         elif commands[0] == "RF":
            self.commandRF(commands,controllers)
         elif commands[0] == "AF":
            self.commandAF(commands,controllers)  
         elif commands[0] == "DF":
            self.commandDF(commands,controllers) 
         elif commands[0] == "LP":
            self.commandLP(controllers)         
         elif commands[0] == "LF":
            self.commandLF(controllers)          
         elif commands[0] == "LU":
            self.commandLU(controllers)
         elif commands[0] == "MF":
            self.commandMF(commands,controllers)
         elif commands[0] == "MC":
            self.commandMC(commands,controllers)
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
                 
   def commandRP(self,commands,controllers):
   #Regista profissional
      category = commands[1]
      name = commands[2]
      if controllers["Category"].has_category(category):
         if controllers["Professional"].has_professional(name,category):
            print("Profissional existente.")
         else:
            controllers["Professional"].add_profissional(name,category)
            print("Profissional registado com sucesso.")
      else:
         print("Categoria inexistente.")
   
   def commandRU(self,commands,controllers):
   #Registar utente
      name = commands[1]
      age_range= commands[2]
      if controllers["User"].has_user(name):
         print("Utente existente.")
      else:
         if controllers["User"].has_age_range(age_range):
            controllers["User"].add_user(name,age_range)
            print("Utente registado com sucesso.")
         else:
            print("Faixa etária inexistente.")
            
   def commandRF(self,commands,controllers):
   #Registar família
      family_name = commands[1]
      if controllers["Family"].has_family(family_name):
         print("Família existente.")
      else:
         controllers["Family"].add_family(family_name)
         print("Família registada com sucesso.") 
         
   def commandAF(self,commands,controllers):
   #Associar utente a família 
      user_name = commands[1]
      family_name = commands[2]
      if controllers["Family"].has_family(family_name):
         if controllers["User"].has_user(user_name):
            if not controllers["User"].user_have_family(user_name):
               controllers["User"].associate_family(user_name,family_name)
               print("Utente associado a família.")
            else:
               print("Utente pertence a família.")
         else:
            print("Utente inexistente.")
      else:
         print("Família inexistente.")
   
   def commandDF(self,commands,controllers):
   #Desassociar utente de famíla
      user_name = commands[1]
      if controllers["User"].has_user(user_name):
         if controllers["User"].user_have_family(user_name):
            controllers["User"].disassociate_user(user_name)
            print("Utente desassociado de família.")
         else:
            print("Utente não pertence a família.")
      else:
         print("Utente inexistente.")

   def commandLF(self,controllers):
   #Listar famílias
      if controllers["Family"].has_families():
         controllers["Family"].show_families()
      else:
         print("Sem famílias registadas.")
   
   def commandLP(self,controllers):
   #Listar profissionais
      if controllers["Professional"].has_professionals():
         controllers["Professional"].show_professionals()
      else:
         print("Sem profissionais registados.")   
   
   def commandLU(self,controllers):
   #Listar utentes
      if controllers["User"].has_users():
         controllers["User"].show_users()
      else:
         print("Sem utentes registados.")
   
   def commandMF(self,commands,controllers):
   #Mostrar família
      family_name = commands[1]
      if controllers["Family"].has_family(family_name):
         controllers["Family"].show_family(family_name)
      else:
         print("Família inexistente.")
      
   def commandMC(self,commands,controllers):
   #Marcar cuidados a utente
      i = 0
      marcacoes =[]
      while i !=1:
         text = input()
         if not text:
            i+=1
         marcacoes.append(text.split(" "))
      del marcacoes[len(marcacoes)-1]
      services = []
      name= commands[2]
      for service in marcacoes:
         if len(service) == 1:
            services.append(service)
         else:
            if controllers["Category"].has_category(service[0]) ==  False:
               print("Categoria inexistente.")
      if controllers["User"].has_user(name):      
         print("Utente existente.")
      elif controllers["Serivce"].has_services(services) == False:
         print("Serviço inexistente.")
      # FUNÇÃO INACABADAAAAA
         

       
      
      
   """
     
   
   
   def commandCC(self,commands,controller):
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
   
   def commandLCU(self,commands,controller):
   #Listar cuidados marcados a utente
      name = commands[1]
      if controller.has_user(name):
         if controller.has_scheduled(name,"utente"): 
            controller.show_user_scheduled(name)
         else:
            print("Utente sem cuidados de saúde marcados.")
      else:
         print("Utente inexistente.")
   
   def commandLCF(self,commands,controller):
   #Listar cuidados marcados a família  
      family_name = commands[1]
      if controller.has_family(family_name):
         if controller.has_scheduled(family_name,"família"): 
            controller.show_family_scheduled(family_name)
         else:
            print("Familia sem cuidados de saúde marcados.")
      else:
         print("Família inexistente.")
   
   def commandLSP(self,commands,controller):
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
   
   def commandLMS(self,commands,controller):
   #Listar marcações por tipo de serviço
      service = commands[1]
      if controller.has_service(service):
         if controller.has_scheduled(service,"serviço"):
            controller.show_service_scheduled()
         else:
            print("Serviço sem marcações.")
      else:
         print("Serviço inexistente.") """

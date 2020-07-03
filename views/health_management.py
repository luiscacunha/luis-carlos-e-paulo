from ..controllers.task_list_controller import TaskListController

class HM:
   def __init__(self):
      controller = TaskListController()
   
      while True:
         line = input()
         if not line:
            exit(0)
         commands = line.split(" ")
         if commands[0] == "RP":
            commandRP(commands)
         elif commands[0] == "RU":
            commandRU(commands)
         elif commands[0] == "RF":
            commandRF(commands)
         elif commands[0] == "AF":
            commandAF(commands)
         elif commands[0] == "DF":
            commandDF(commands)
         elif commands[0] == "LP":
            commandLP()
         elif commands[0] == "LU":
            commandLU()
         elif commands[0] == "LF":
            commandLF()
         elif commands[0] == "MF":
            commandMF(commands)
         elif commands[0] == "MC":
            commandMC(commands)
         elif commands[0] == "CC":
            commandCC(commands)
         elif commands[0] == "LCU":
            commandLCU(commands)
         elif commands[0] == "LCF":
            commandLCF(commands)   
         elif commands[0] == "LSP":
            commandLSP(commands)         
         elif commands[0] == "LMS":
            commandLMS(commands)              
         else:
            print("Instrução inválida.")
   
   def commandRP(commands):
   #Regista profissional
      category = commands[1]
      name = commands[2]
      if controller.has_category(category):
         if controller.has_professional(name,category):
            print("Profissional existente.")
         else:
            controller.add_profissional(name,category)
            print("Profissional registado com sucesso.")
      else:
         print("Categoria inexistente.")
   
   def commandRU(commands):
   #Registar utente
      name = commands[1]
      age_range= commands[2]
      if controller.has_user(name):
         print("Utente existente.")
      else:
         if controller.has_age_range(age_range):
            controller.add_user(name,age_range)
            print("Utente registado com sucesso.")
         else:
            print("Faixa etária inexistente.")
            
   def commandRF(commands):
   #Registar família
      family_name = commands[1]
      if controller.has_family(family_name):
         print("Família existente.")
      else:
         controller.add_family(family_name)
         print("Família registada com sucesso.")
   
   def commandAF(commands):
   #Associar utente a família 
      user_name = commands[1]
      family_name = commands[2]
      if controller.has_family(family_name):
         if controller.has_user(user_name):
            if not controller.user_have_family(user_name):
               controller.associate_family(user_name,family_name)
               print("Utente associado a família.")
            else:
               print("Utente pertence a família.")
         else:
            print("Utente inexistente.")
      else:
         print("Família inexistente.")
   
   def commandDF(commands):
   #Desassociar utente de famíla
      user_name = commands[1]
      if controller.has_user(user_name):
         if controller.user_have_family(user_name):
            controller.disassociate_user(user_name)
            print("Utente desassociado de família.")
         else:
            print("Utente não pertence a família.")
      else:
         print("Utente inexistente.")
   
   
   def commandLP():
   #Listar profissionais
      if controller.has_professionals():
         controller.show_professionals()
      else:
         print("Sem profissionais registados.")
   
   def commandLU():
   #Listar utentes
      if controller.has_users():
         controller.show_users()
      else:
         print("Sem utentes registados.")
   
   
   def commandLF():
   #Listar famílias
      if controller.has_families():
         controller.show_families()
      else:
         print("Sem famílias registadas.")
   
   def commandMF(commands):
   #Mostrar família
      family_name = commands[1]
      if controller.has_family(family_name):
         controller.show_family(family_name)
      else:
         print("Família inexistente.")
   
   def commandMC(commands):
   #Marcar cuidados a utente
      pass
   
   def commandCC(commands):
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
   
   def commandLCU(commands):
   #Listar cuidados marcados a utente
      name = commands[1]
      if controller.has_user(name):
         if controller.has_scheduled(name,"utente"): 
            controller.show_user_scheduled(name)
         else:
            print("Utente sem cuidados de saúde marcados.")
      else:
         print("Utente inexistente.")
   
   def commandLCF(commands):
   #Listar cuidados marcados a família  
      family_name = commands[1]
      if controller.has_family(family_name):
         if controller.has_scheduled(family_name,"família"): 
            controller.show_family_scheduled(family_name)
         else:
            print("Familia sem cuidados de saúde marcados.")
      else:
         print("Família inexistente.")
   
   def commandLSP(commands):
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
   
   def commandLMS(commands):
   #Listar marcações por tipo de serviço
      service = commands[1]
      if controller.has_service(service):
         if controller.has_scheduled(service,"serviço"):
            controller.show_service_scheduled()
         else:
            print("Serviço sem marcações.")
      else:
         print("Serviço inexistente.")
   

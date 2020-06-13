import healthsystem as spsus
# NÃO FIZ A FUNÇÃO MC 

def main():

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
      elif commands[0] == "G":
         commandG(commands)
      elif commands[0] == "L":
         commandL(commands)      
      else:
         print("Instrução inválida.")

def commandRP(commands):
#Regista profissional
   category = commands[1]
   name = commands[2]
   if spsus.has_category(category):
      if spsus.has_professional(name,category):
         print("Profissional existente.")
      else:
         spsus.add_profissional(name,category)
         print("Profissional registado com sucesso.")
   else:
      print("Categoria inexistente.")

def commandRU(commands):
#Registar utente
   name = commands[1]
   age_range= commands[2]
   if spsus.has_user(name):
      print("Utente existente.")
   else:
      if spsus.has_age_range(age_range):
         spsus.add_user(name,age_range)
         print("Utente registado com sucesso.")
      else:
         print("Faixa etária inexistente.")
         
def commandRF(commands):
#Registar família
   family_name = commands[1]
   if spsus.has_family(family_name):
      print("Família existente.")
   else:
      spsus.add_family(family_name)
      print("Família registada com sucesso.")

def commandAF(commands):
#Associar utente a família 
   user_name = commands[1]
   family_name = commands[2]
   if spsus.has_family(family_name):
      if spsus.has_user(user_name):
         if not spsus.user_have_family(user_name):
            spsus.associate_family(user_name,family_name)
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
   if spsus.has_user(user_name):
      if spsus.user_have_family(user_name):
         spsus.disassociate_user(user_name)
         print("Utente desassociado de família.")
      else:
         print("Utente não pertence a família.")
   else:
      print("Utente inexistente.")


def commandLP():
#Listar profissionais
   if spsus.has_professionals():
      spsus.show_professionals()
   else:
      print("Sem profissionais registados.")

def commandLU():
#Listar utentes
   if spsus.has_users():
      spsus.show_users()
   else:
      print("Sem utentes registados.")


def commandLF():
#Listar famílias
   if spsus.has_families():
      spsus.show_families()
   else:
      print("Sem famílias registadas.")

def commandMF(commands):
#Mostrar família
   family_name = commands[1]
   if spsus.has_family(family_name):
      spsus.show_family(family_name)
   else:
      print("Família inexistente.")

def commandMC(commands):
#Marcar cuidados a utente
   pass

def commandCC(commands):
#Cancelar cuidados marcados a utente
   name = commands[1]
   if spsus.has_user(name):
      if spsus.has_scheduled(name,"utente"):
         spsus.cancel_user_scheduled(name)
         print("Cuidados de saúde desmarcados com sucesso.")
      else:
         print("Utente sem cuidados de saúde marcados.")
   else:
      print("Utente inexistente.")

def commandLCU(commands):
#Listar cuidados marcados a utente
   name = commands[1]
   if spsus.has_user(name):
      if spsus.has_scheduled(name,"utente"): 
         spsus.show_user_scheduled(name)
      else:
         print("Utente sem cuidados de saúde marcados.")
   else:
      print("Utente inexistente.")

def commandLCF(commands):
#Listar cuidados marcados a família  
   family_name = commands[1]
   if spsus.has_family(family_name):
      if spsus.has_scheduled(family_name,"família"): 
         spsus.show_family_scheduled(family_name)
      else:
         print("Familia sem cuidados de saúde marcados.")
   else:
      print("Família inexistente.")

def commandLSP(commands):
#Listar serviços marcados a profissional 
   category = commands[1]
   professional_name = commands[2]
   if spsus.has_professional(professional_name,category):
      if spsus.has_scheduled(professional_name,"profissional"):
         spsus.show_professional_scheduled(professional_name)
      else:
         print("Profissional de saúde sem marcações.")
   else:
      print("Profissional de saúde inexistente.")

def commandLMS(commands):
#Listar marcações por tipo de serviço
   service = commands[1]
   if spsus.has_service(service):
      if spsus.has_scheduled(service,"serviço"):
         spsus.show_service_scheduled()
      else:
         print("Serviço sem marcações.")
   else:
      print("Serviço inexistente.")

def commandG(commands):
#Gravar unidade de saúde
   """
   try:
      #CODIGO PARA GRAVAÇÃO
      print("Unidade de saúde gravada.")
   except Exception as e:
      print("Ocorreu um erro na gravação.")
   """
   pass

def commandL(commands):
#Ler unidade de saúde
   """
   try:
      #CODIGO PARA CARREGAR
      print("Unidade de saúde carregada.")
   except Exception as e:
      print("Ocorreu um erro no carregamento.")
   """
   pass

if __name__ == "__main__":
    main()

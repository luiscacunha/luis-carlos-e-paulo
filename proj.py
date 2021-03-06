import healthsystem as spsus

def main():

   while True:
      line = input()
      if not line:
         exit(0)
      commands = line.split(" ")
      if commands[0] == "RP":
         commandRP(commands,spsus)
      elif commands[0] == "RU":
         commandRU(commands,spsus)
      elif commands[0] == "RF":
         commandRF(commands,spsus)
      elif commands[0] == "AF":
         commandAF(commands,spsus)
      elif commands[0] == "DF":
         commandDF(commands,spsus)
      elif commands[0] == "LP":
         commandLP(commands,spsus)
      elif commands[0] == "LU":
         commandLU(commands,spsus)
      elif commands[0] == "LF":
         commandLF(commands,spsus)
      elif commands[0] == "MF":
         commandMF(commands,spsus)
      elif commands[0] == "MC":
         commandMC(commands,spsus)
      elif commands[0] == "CC":
         commandCC(commands,spsus)
      elif commands[0] == "LCU":
         commandLCU(commands,spsus)
      elif commands[0] == "LCF":
         commandLCF(commands,spsus)   
      elif commands[0] == "LSP":
         commandLSP(commands,spsus)         
      elif commands[0] == "LMS":
         commandLMS(commands,spsus)         
      elif commands[0] == "G":
         commandG(commands,spsus)
      elif commands[0] == "L":
         commandL(commands,spsus)      
      else:
         print("Instrução inválida.")

def commandRP(commands,spsus):
#Regista profissional
   category = commands[0]
   name = commands[1]
   if spsus.has_category(category):
      if spsus.has_professional(name,category):
         print("Profissional existente.")
      else:
         spsus.add_profissional(name,category)
         print("Profissional registado com sucesso.")
   else:
      print("Categoria inexistente.")

def commandRU(commands,spsus):
#Registar utente
   pass

def commandRF(commands,spsus):
#Registar família
   pass

def commandAF(commands,spsus):
#Associar utente a família 
   pass

def commandDF(commands,spsus):
#Desassociar utente de famíla
   pass

def commandLP(commands,spsus):
#Listar profissionais
   pass

def commandLU(commands,spsus):
#Listar utentes
   pass

def commandLF(commands,spsus):
#Listar famílias
   pass

def commandMF(commands,spsus):
#Mostrar família
   pass

def commandMC(commands,spsus):
#Marcar cuidados a utente
   pass

def commandCC(commands,spsus):
#Cancelar cuidados marcados a utente
   pass

def commandLCU(commands,spsus):
#Listar cuidados marcados a utente
   pass

def commandLCF(commands,spsus):
#Listar cuidados marcados a família  
   pass

def commandLSP(commands,spsus):
#Listar serviços marcados a profissional 
   pass

def commandLMS(commands,spsus):
#Listar marcações por tipo de serviço
   pass

def commandG(commands,spsus):
#Gravar
   pass

def commandL(commands,spsus):
#Ler
   pass

if __name__ == "__main__":
    main()

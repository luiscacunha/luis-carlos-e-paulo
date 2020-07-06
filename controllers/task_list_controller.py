from models.user import user
from models.professional import professional

class TaskListController:
   def __init__(self):
      pass
   
   def has_scheduled(self,name,entity):
      #Verifica se name da entity(self,utente/familia/serviço/medico)tem cuidados marcados 
      pass

   def cancel_user_scheduled(self,name):
      #Cancelar cuidados marcados do utente.
      pass



   def show_family_scheduled(self,family_name):
      """
      Mostrar listagem de todos os profissionais de saúde associados a marcações dos utentes da família indicada, de acordo com o serviço da marcação, e a sua categoria
      Nome˽Serviço˽Categoria˽NomeProfissional.↵
      """
      pass

   def show_professional_scheduled(self,professional_name):
      """
      listagem de marcações de um profissioonal de saude, com indicação de serviço e nome de utente)
      Serviço˽Nome.↵
      """
      pass

   def has_service(self,service):
      #Validar se exister serviço
      pass

   def show_service_scheduled(self):
      #Mostrar lista de marcações por tipo de serviço
      pass
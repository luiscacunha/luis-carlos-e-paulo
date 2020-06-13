from lists import singly_linked_list
from dictionaries import hash_table

def has_category(category):
    #Verifica se existe categoria
    pass

def has_professional(name,category):
    #Verifica se existe profissional já registado
    pass

def add_profissional(name,category):
    #Adiciona profissional de saúde
    pass

def has_user(name):
    #Verifica se existe utente já registado, profissional de saúde tem uma categoria e um nome
    pass

def has_age_range(age_range):
    #Verifica se existe faixa etária
    pass

def add_user(name,age_range):
    #Adiciona utente, utente tem uma faixa etária e um nome
    pass

def has_family(family_name):
    #Adiciona Familia
    pass

def add_family(family_name):
    #Adiciona nome de familia
    pass

def user_have_family(user_name):
    #Verifica se utente pertence à uma familia.
    pass

def associate_family(user_name,family_name):
    #Associa um utente a uma familia
    pass

def disassociate_user(user_name):
    #Desassocia utente de familia
    pass

def has_professionals():
    #Verificar se lista de profissionais está vázia
    pass

def show_professionals():
    #Mostrar profissionals "Categoria_Nome", por ordem alfabética dentro de cada categoria
    pass

def has_users():
    #Verifica se lista de utentes está vázia
    pass

def show_users():
    """
    Lista todos os utentes por faixa etária, por ordem alfabética de família em cada faixa etária, e por ordem alfabética de nome dentro de cada família. 
    As faixas etárias devem ser listadas de acordo com a ordem apresentada na Tabela 2.
    Se um utente não tiver família associada, deve ser só indicada a faixa etária
    Familia FaixaEtária Nome ou FaixaEtária Nome
    """
    pass

def has_families():
    #Verifica se lista familias está vázia
    pass

def show_families():
    #Mostrar todas as familias por ordem alfabética.
    pass

def show_family(family_name):
    """
    Lista todos os utentes de uma família, por ordem de faixa etária, e por ordem alfabética dentro de cada faixa etária. 
    As faixas etárias devem ser listadas de acordo com a ordem apresentada na Tabela 2
    Saída com sucesso (listagem de utentes da mesma família)
    FaixaEtária˽Nome.↵
    """
    pass

def has_scheduled(name,entity):
    #Verifica se name da entity(utente/familia/serviço/medico)tem cuidados marcados 
    pass

def cancel_user_scheduled(name):
    #Cancelar cuidados marcados do utente.
    pass

def show_user_scheduled(name):
    """
    Mostrar listagem de todos os profissionais de saúde associados a marcações do utente, de acordo com o serviço da marcação, e a sua categoria)
    Serviço˽Categoria˽NomeProfissional.↵
    """
    pass

def show_family_scheduled(family_name):
    """
    Mostrar listagem de todos os profissionais de saúde associados a marcações dos utentes da família indicada, de acordo com o serviço da marcação, e a sua categoria
    Nome˽Serviço˽Categoria˽NomeProfissional.↵
    """
    pass

def show_professional_scheduled(professional_name):
    """
    listagem de marcações de um profissioonal de saude, com indicação de serviço e nome de utente)
    Serviço˽Nome.↵
    """
    pass

def has_service(service):
    #Validar se exister serviço
    pass

def show_service_scheduled():
    #Mostrar lista de marcações por tipo de serviço
    pass
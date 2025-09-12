class Empresa:
    #Função de inicialização de objetos da classe
    def __init__(self, id_empresa : int, id_tipo_empresa : int, id_indice_classificacao : int,id_status_aprovacao : int , nome : str, cnpj : str, email : str, telefone : str):
        self.id_empresa = id_empresa
        self.id_tipo_empresa = id_tipo_empresa
        self.id_indice_classificacao = id_indice_classificacao
        self.id_status_aprovacao = id_status_aprovacao
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.telefone = telefone
    

    #Função de saída de objetos da classe
    def __repr__(self):
        return f"id empresa: {self.id_empresa} | id tipo empresa: {self.id_tipo_empresa} | id indice de classificação: {self.id_indice_classificacao} | id status de aprovação: {self.id_status_aprovacao} | nome: {self.nome} | cnpj: {self.cnpj} | email: {self.email} | telefone: {self.telefone}"
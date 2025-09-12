#Importação do date para lidar com variáveis tipo date
from datetime import date
class Status_aprovacao:
    #Função de inicialização de objetos da classe
    def __init__(self, id_status_aprovacao : int, motivo_rejeicao : str, status : str, data_solicitacao : date, data_aprovacao : date):
        self.id_status_aprovacao = id_status_aprovacao
        self.motivo_rejeicao = motivo_rejeicao
        self.status = status
        self.data_solicitacao = data_solicitacao
        self.data_aprovacao = data_aprovacao
    

    #Função de saída de objetos da classe
    def __repr__(self):
        return f"id status aprovação: {self.id_status_aprovacao} | motivo_rejeição: {self.motivo_rejeicao} | status: {self.status} | data de solicitação: {self.data_solicitacao} | data de aprovação: {self.data_aprovacao}"
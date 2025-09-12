class Indice_classificacao:
    #Função de inicialização de objetos da classe
    def __init__(self, id_indice_classificacao : int, recomendacao : str, preocupacao: str, porcentagem_minima : float, porcentagem_maxima : float):
        self.id_indice_classificacao = id_indice_classificacao
        self.recomendacao = recomendacao
        self.preocupacao = preocupacao
        self.porcentagem_minima = porcentagem_minima
        self.porcentagem_maxima = porcentagem_maxima
    

    #Função de saída de objetos da classe
    def __repr__(self):
        return f"id indice classificação: {self.id_indice_classificacao} | recomendação: {self.recomendacao} | preocupação: {self.preocupacao} | porcentagem mínima: {self.porcentagem_minima} | porcentagem máxima: {self.porcentagem_maxima}"
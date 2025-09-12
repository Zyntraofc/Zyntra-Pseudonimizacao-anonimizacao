class Administrador:
    #Função de inicialização de objetos da classe
    def __init__(self, id_adm : int, email : str, hash_senha : str):
        self.id_adm = id_adm
        self.email = email
        self.hash_senha = hash_senha
    
    #Função de saída de objetos da classe
    def __repr__(self):
        return f"Id administrador: {self.id_adm} | Email: {self.email} | Hash senha: {self.hash_senha}"
    
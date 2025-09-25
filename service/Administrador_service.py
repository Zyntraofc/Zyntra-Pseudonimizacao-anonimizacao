import hashlib

# Método para pseudonimizar o e-mail do administrador
def anonimizar_email_administrador(email: str) -> str:
    """
    Recebe um e-mail e retorna uma versão pseudonimizada usando hash.
    """
    # Transformar o e-mail em bytes para o hash
    email_bytes = email.encode('utf-8')  
    # Gerar hash SHA-256 do e-mail
    hashed_email = hashlib.sha256(email_bytes).hexdigest()  
    # Devolver o e-mail pseudonimizado
    return hashed_email

# Método para pseudonimizar o nome do administrador
def anonimizar_nome_administrador(nome: str) -> str:
    """
    Substitui todas as letras do nome por '*', mantendo o tamanho original.
    """
    # Gerar string de asteriscos do mesmo tamanho
    return '*' * len(nome)

# Método para pseudonimizar telefone
def anonimizar_telefone_administrador(telefone: str) -> str:
    """
    Mantém os últimos 2 dígitos visíveis e oculta o resto.
    """
    return 'X'*(len(telefone)-2) + telefone[-2:]

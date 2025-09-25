import hashlib

# Método para pseudonimizar e-mail da empresa
def anonimizar_email_empresa(email: str) -> str:
    email_bytes = email.encode('utf-8')
    hashed_email = hashlib.sha256(email_bytes).hexdigest()
    return hashed_email

# Método para pseudonimizar CNPJ da empresa
def anonimizar_cnpj_empresa(cnpj: str) -> str:
    return 'X'*(len(cnpj)-4) + cnpj[-4:]

# Método para pseudonimizar nome da empresa
def anonimizar_nome_empresa(nome: str) -> str:
    return '*'*len(nome)

# Importação de classes necessárias para manipulação do database
from dao import Conexao
from model.Administrador import Administrador

# Função para listagem de administradores da tabela administradores
def listar_administradores():
    
    # Atribuindo a variável conn de conexão o valor retornado pelo método 'get_connection'
    conn = Conexao.get_connection()
    # Verificação se a conexão é nula, se for retorna lista vazia
    if not conn:
        return []

    try:
        # Abrindo cursor para manipular o database
        cur = conn.cursor()
        # Query a ser executada na tabela Administrador
        query = "SELECT id_adm, email, hash_senha FROM administrador"
        # Execução da query pelo cursor
        cur.execute(query)
        # Atribuido a uma variável todos os valores e linhas encontrados no database
        administradores = cur.fetchall()
        
        # List comprehension para atribuir objetos tipo Administrador a lista
        admins = [Administrador(a[0], a[1], a[2]) for a in administradores]
        # Retornando a lista
        return admins 

    # Em caso de erros, printa que houve erros e o erro, depois retorna lista vazia
    except Exception as e:
        print("Erro ao listar:", e)
        return []
    # Desconecta antes do retorno
    finally:
        cur.close()
        conn.close()

# Função para inserção na tabela administradores_anonimo
def inserir_administrador(administrador: Administrador):
    # Atribuindo a variável conn de conexão o valor retornado pelo método 'get_connection'
    conn = Conexao.get_connection()
    # Verificação de se a conexão não é nula, se for, retorna False
    if not conn:
        return False
    
    try:
        # Abrindo cursor para manipulação do database
        cur = conn.cursor()
        # Insert a ser executado na tabela administrador_anonimo
        insert = "INSERT INTO administrador_anonimo (email, hash_senha) VALUES (%s, %s)"
        # Execução do insert pelo cursor, e substituição dos valores
        cur.execute(insert, (administrador.email, administrador.hash_senha))
        
        # COMMIT necessário para salvar as alterações
        conn.commit()
        
        # Retorna True indicando sucesso
        return True
        
    # Em caso de erro retorna qual é o erro e False
    except Exception as e:
        print("Erro ao inserir:", e)
        # Rollback em caso de erro
        conn.rollback()
        return False
        
    # Desconecta antes do retorno
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
#Importações de classes a serem usadas para manipular tabela empresa
from dao import Conexao
from model.Status_aprovacao import Status_aprovacao
import psycopg2

#Função de listagem da tabela status_aprovacao
def listar_status_aprovacao():
    #Atribuindo a variável conn de conexão o valor retornado pelo método 'get_connection'
    conn = Conexao.get_connection()

     # Verificação se a conexão é nula, se for retorna lista vazia
    if not conn:
        return []
    
    try:
        #Variável de cursor para manipulação do database
        cur = conn.cursor()

        #Variável contenddo o comando a ser rodado no database
        query = "select * from status_aprovacao"

        #Executando o comando
        cur.execute(query)

        #Colocando todos os registros em uma variável
        status_aprovacoes = cur.fetchall()

        #List comprehension para atribuir objetos da classe Indice_classificacao com os registros em uma list
        status = [Status_aprovacao(i[0], i[1], i[2], i[3], i[4]) for i in status_aprovacoes]

        #Retornando lista com status
        return status
    
    
    except Exception as e:
        #Printando o erro e retornando lista vazia em caso de excessão
        print("Erro ao listar: ",e)
        return []
    finally:
        #Fechando cursor e conexão antes do retorno
        conn.close()
        cur.close()
    
#Função de inserção na tabela status_aprovacao_anonimo
def inserir_status_aprovacao(status_aprovacao : Status_aprovacao):

    #Função get_connection atribuida a variável de controle da conexão
    conn = Conexao.get_connection()

    try:

        #Retorna false se a conexão não existir
        if not conn:
            return False
        
        #Variável de cursor para manipulação do database
        cur = conn.cursor()

        #Comando de inserção na tabela status_aprovacao_anonimo
        insert = """
    insert into status_aprovacao_anonimo (
        motivo_rejeicao,
        status,
        data_solicitacao,
        data_aprovacao
    ) values (%s, %s, %s, %s)
"""
        #Executando comando de conexão e atribuindo os parametros
        cur.execute(insert, (status_aprovacao.motivo_rejeicao, status_aprovacao.status, status_aprovacao.data_solicitacao, status_aprovacao.data_aprovacao))
        #Commitando a inserção na conexão
        conn.commit()
        #Retornando true
        return True
    #Printa o erro e retorna falso caso haja alguma exceção
    except Exception as e:
        print("Erro ao inserir: ", e)
        return False
    #Desconectando e fechando cursor antes do retorno
    finally:
        if conn:
            conn.close()
        if cur:
            cur.close()

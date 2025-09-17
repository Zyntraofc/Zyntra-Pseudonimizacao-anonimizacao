#Importações de classes a serem usadas para manipular tabela empresa
from dao import Conexao
from model.Indice_classificacao import Indice_classificacao
import psycopg2

#Função de listagem da tabela indice_classificacao
def listar_indices_classificacao():
    #Atribuindo a variável conn de conexão o valor retornado pelo método 'get_connection'
    conn = Conexao.get_connection()

     # Verificação se a conexão é nula, se for retorna lista vazia
    if not conn:
        return []
    
    try:
        #Variável de cursor para manipulação do database
        cur = conn.cursor()

        #Variável contenddo o comando a ser rodado no database
        query = "select * from indice_classificacao"

        #Executando o comando
        cur.execute(query)

        #Colocando todos os registros em uma variável
        indices_classificacao = cur.fetchall()

        #List comprehension para atribuir objetos da classe Indice_classificacao com os registros em uma list
        indices = [Indice_classificacao(i[0], i[1], i[2], i[3], i[4]) for i in indices_classificacao]

        #Retornando lista com empresas
        return indices
    
    
    except Exception as e:
        #Printando o erro e retornando lista vazia em caso de excessão
        print("Erro ao listar: ",e)
        return []
    finally:
        #Fechando cursor e conexão antes do retorno
        conn.close()
        cur.close()
    
#Função de inserção na tabela indice_classificacao_anonimo
def inserir_indice_classificacao(indice_classificacao : Indice_classificacao):

    #Função get_connection atribuida a variável de controle da conexão
    conn = Conexao.get_connection()

    try:

        #Retorna false se a conexão não existir
        if not conn:
            return False
        
        #Variável de cursor para manipulação do database
        cur = conn.cursor()

        #Comando de inserção na tabela indice_classificacao_anonimo
        insert = """
    insert into indice_classificacao_anonimo (
        recomendacao,
        preocupacao,
        porcentagem_minima,
        porcentagem_maxima
    ) values (%s, %s, %s, %s)
"""
        #Executando comando de conexão e atribuindo os parametros
        cur.execute(insert, (indice_classificacao.recomendacao, indice_classificacao.preocupacao, indice_classificacao.porcentagem_minima, indice_classificacao.porcentagem_maxima))
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
    






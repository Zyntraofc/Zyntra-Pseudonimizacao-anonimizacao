#Importações de classes a serem usadas para manipular tabela empresa
from dao import Conexao
from model.Empresa import Empresa
import psycopg2

#Função de listagem da tabela empresa
def listar_empresas():
    #Atribuindo a variável conn de conexão o valor retornado pelo método 'get_connection'
    conn = Conexao.get_connection()

     # Verificação se a conexão é nula, se for retorna lista vazia
    if not conn:
        return []
    
    try:
        #Variável de cursor para manipulação do database
        cur = conn.cursor()

        #Variável contenddo o comando a ser rodado no database
        query = "select * from empresa"

        #Executando o comando
        cur.execute(query)

        #Colocando todos os registros em uma variável
        empresas = cur.fetchall()

        #List comprehension para atribuir objetos da classe Empresa com os registros em uma list
        empres = [Empresa(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7]) for e in empresas]

        #Retornando lista com empresas
        return empres
    
    
    except Exception as e:
        #Printando o erro e retornando lista vazia em caso de excessão
        print("Erro ao listar: ",e)
        return []
    finally:
        #Fechando cursor e conexão antes do retorno
        conn.close()
        cur.close()
    
#Função de inserção na tabela empresa_anonimo
def inserir_empresa(empresa : Empresa):

    #Função get_connection atribuida a variável de controle da conexão
    conn = Conexao.get_connection()

    try:

        #Retorna false se a conexão não existir
        if not conn:
            return False
        
        #Variável de cursor para manipulação do database
        cur = conn.cursor()

        #Comando de inserção na tabela empresa_anonimo
        insert = """
    insert into empresa_anonimo (
        id_indice_classificacao, 
        id_status_aprovacao, 
        nome, 
        cnpj, 
        email, 
        telefone, 
        id_tipo_empresa
    ) values (%s, %s, %s, %s, %s, %s, %s)
)"""
        #Executando comando de conexão e atribuindo os parametros
        cur.execute(insert, (empresa.id_indice_classificacao, empresa.id_status_aprovacao, empresa.nome, empresa.cnpj, empresa.email, empresa.telefone, empresa.id_tipo_empresa))

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
    






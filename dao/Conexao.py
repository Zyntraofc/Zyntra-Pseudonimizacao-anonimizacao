#Importação de bibliotecas e frameworks necessários para a leitura de .env e manipulação do database
from dotenv import load_dotenv
import os
from psycopg2 import sql
import psycopg2

#Localizando o .env na raíz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) 
DOTENV_PATH = os.path.join(BASE_DIR, ".env")

load_dotenv(DOTENV_PATH)

#Lendo .env e obtendo variáveis necessárias para a conexão
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

#Função para conectar com o banco de dados
def get_connection():
    try:
        #Conectando com o banco de dados
        conn = psycopg2.connect(
            host = DB_HOST,
            port = DB_PORT,
            dbname = DB_NAME,
            user = DB_USER,
            password = DB_PASS
        )
        #Retornando a conexão estabelecida
        return conn
    #Em caso de erro de conexão, printa o erro
    except psycopg2.OperationalError as e:
        print("Erro de conexão:", e)
    #Fechando a conexão antes do retorno
    finally:
        conn.close

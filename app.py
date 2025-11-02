#!/usr/bin/env python3
"""
app.py - Arquivo principal para executar anonimização e pseudonimização de dados
Funciona mesmo com espaços e acentos na pasta.
"""

import sys
import os
from dotenv import load_dotenv
import pandas as pd

# 🔹 Adiciona a pasta raiz do projeto no sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 🔹 Carrega variáveis do .env
load_dotenv()

# 🔹 Imports dos services
from service.Administrador_service import anonimizar_e_persistir_administradores
from service.Empresa_service import anonimizar_e_persistir_empresas
from service.Indice_classificacao_service import anonimizar_e_persistir_indices
from service.Status_aprovacao_service import anonimizar_e_persistir_status

# 🔹 Mostra configuração (sem exibir senha)
def mostrar_config():
    print("\n=== CONFIGURAÇÃO DO BANCO ===")
    print("Host:", os.getenv("DB_HOST"))
    print("Porta:", os.getenv("DB_PORT"))
    print("Banco:", os.getenv("DB_NAME"))
    print("Usuário:", os.getenv("DB_USER"))
    print("SALT:", os.getenv("SALT"))
    print("(Senha oculta por segurança)")
    print("==============================\n")

# 🔹 Funções para rodar cada serviço
def run_administradores():
    print("▶ Anonimizando ADMINISTRADORES...")
    df = anonimizar_e_persistir_administradores()
    _mostrar_resultado(df)

def run_empresas():
    print("▶ Anonimizando EMPRESAS...")
    df = anonimizar_e_persistir_empresas()
    _mostrar_resultado(df)

def run_indices():
    print("▶ Anonimizando ÍNDICES DE CLASSIFICAÇÃO...")
    df = anonimizar_e_persistir_indices()
    _mostrar_resultado(df)

def run_status():
    print("▶ Anonimizando STATUS DE APROVAÇÃO...")
    df = anonimizar_e_persistir_status()
    _mostrar_resultado(df)

def run_all():
    print("\n=== EXECUTANDO TODAS AS ANONIMIZAÇÕES ===\n")
    run_administradores()
    run_empresas()
    run_indices()
    run_status()
    print("\n✅ Tudo finalizado com sucesso!")

# 🔹 Função auxiliar para exibir resultados
def _mostrar_resultado(df: pd.DataFrame):
    if df is None or df.empty:
        print("Nenhum dado retornado.\n")
        return
    print(f"Linhas processadas: {len(df)}")
    print(df.head().to_string(index=False))
    print("-" * 60 + "\n")

# 🔹 Menu interativo
def interactive_menu():
    mostrar_config()
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1 - Administradores")
        print("2 - Empresas")
        print("3 - Índices de classificação")
        print("4 - Status de aprovação")
        print("5 - Rodar tudo")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            run_administradores()
        elif opcao == "2":
            run_empresas()
        elif opcao == "3":
            run_indices()
        elif opcao == "4":
            run_status()
        elif opcao == "5":
            run_all()
        elif opcao == "0":
            print("Encerrando... 👋")
            break
        else:
            print("Opção inválida.\n")

# 🔹 Ponto de entrada
def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd in ("adm", "administrador", "administradores"):
            run_administradores()
        elif cmd in ("empresas", "empresa"):
            run_empresas()
        elif cmd in ("indices", "indice"):
            run_indices()
        elif cmd in ("status", "status_aprovacao"):
            run_status()
        elif cmd in ("all", "tudo"):
            run_all()
        else:
            print("Comando não reconhecido. Use 'python app.py' para o menu.")
    else:
        interactive_menu()

if __name__ == "__main__":
    main()

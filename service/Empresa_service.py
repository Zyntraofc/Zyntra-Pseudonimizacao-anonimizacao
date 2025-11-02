# service/Empresa_service.py
import os
import hashlib
import pandas as pd

from dao.Empresa_dao import listar_empresas, inserir_empresa
from model.Empresa import Empresa

SALT = os.getenv("SALT", "meu_salt_seguro").encode("utf-8")

def pseudonymize(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return value
    return hashlib.sha256(SALT + str(value).encode("utf-8")).hexdigest()

def anonimize_text(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return value
    return "Anonimizado"

def anonimizar_e_persistir_empresas():
    empresas = listar_empresas()  # lista de objetos Empresa
    df = pd.DataFrame([{
        "id_empresa": e.id_empresa,
        "id_tipo_empresa": e.id_tipo_empresa,
        "id_indice_classificacao": e.id_indice_classificacao,
        "id_status_aprovacao": e.id_status_aprovacao,
        "nome": e.nome,
        "cnpj": e.cnpj,
        "email": e.email,
        "telefone": e.telefone
    } for e in empresas])

    if not df.empty:
        if "cnpj" in df.columns:
            df["cnpj_pseudo"] = df["cnpj"].apply(pseudonymize)
        if "email" in df.columns:
            df["email_pseudo"] = df["email"].apply(pseudonymize)
        if "telefone" in df.columns:
            df["telefone_pseudo"] = df["telefone"].apply(pseudonymize)
        if "nome" in df.columns:
            df["nome_anon"] = df["nome"].apply(anonimize_text)

    
    for _, row in df.iterrows():
        empresa_anon = Empresa(
            row.get("id_empresa"),
            row.get("id_tipo_empresa"),
            row.get("id_indice_classificacao"),
            row.get("id_status_aprovacao"),
            row.get("nome_anon"),
            row.get("cnpj_pseudo"),
            row.get("email_pseudo"),
            row.get("telefone_pseudo")
        )
        inserir_empresa(empresa_anon)

    return df

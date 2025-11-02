# service/Administrador_service.py
import os
import hashlib
import pandas as pd

from dao.Administrador_dao import listar_administradores, inserir_administrador
from model.Administrador import Administrador

SALT = os.getenv("SALT", "meu_salt_seguro").encode("utf-8")

def pseudonymize(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return value
    return hashlib.sha256(SALT + str(value).encode("utf-8")).hexdigest()

def anonimize_email(_):
    return "anonimo@empresa.com"

def anonimizar_e_persistir_administradores():
    admins = listar_administradores()  
    
    df = pd.DataFrame([{
        "id_adm": a.id_adm,
        "email": a.email,
        "hash_senha": a.hash_senha
    } for a in admins])

    if not df.empty and "email" in df.columns:
        df["email_pseudo"] = df["email"].apply(pseudonymize)

    
    for _, row in df.iterrows():
        adm_anon = Administrador(
            None,                     
            row.get("email_pseudo"),   
            row.get("hash_senha")      
        )
        inserir_administrador(adm_anon)

    return df

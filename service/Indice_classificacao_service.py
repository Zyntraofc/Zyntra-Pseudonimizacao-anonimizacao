# service/Indice_classificacao_service.py
import pandas as pd

from dao.Indice_classificacao_dao import listar_indices_classificacao, inserir_indice_classificacao
from model.Indice_classificacao import Indice_classificacao

def anonimize_text(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return value
    return "Anonimizado"

def anonimizar_e_persistir_indices():
    indices = listar_indices_classificacao()  
    df = pd.DataFrame([{
        "id_indice_classificacao": i.id_indice_classificacao,
        "recomendacao": i.recomendacao,
        "preocupacao": i.preocupacao,
        "porcentagem_minima": i.porcentagem_minima,
        "porcentagem_maxima": i.porcentagem_maxima
    } for i in indices])

    if not df.empty:
        if "recomendacao" in df.columns:
            df["recomendacao_anon"] = df["recomendacao"].apply(anonimize_text)
        if "preocupacao" in df.columns:
            df["preocupacao_anon"] = df["preocupacao"].apply(anonimize_text)

    
    for _, row in df.iterrows():
        indice_anon = Indice_classificacao(
            None,
            row.get("recomendacao_anon"),
            row.get("preocupacao_anon"),
            row.get("porcentagem_minima"),
            row.get("porcentagem_maxima")
        )
        inserir_indice_classificacao(indice_anon)

    return df

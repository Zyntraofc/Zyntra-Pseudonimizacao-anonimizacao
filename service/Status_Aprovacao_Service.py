# service/Status_aprovacao_service.py
import pandas as pd

from dao.Status_aprovacao_dao import listar_status_aprovacao, inserir_status_aprovacao
from model.Status_aprovacao import Status_aprovacao

def anonimize_text(value):
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return value
    return "Anonimizado"

def anonimizar_e_persistir_status():
    statuses = listar_status_aprovacao()  
    df = pd.DataFrame([{
        "id_status_aprovacao": s.id_status_aprovacao,
        "motivo_rejeicao": s.motivo_rejeicao,
        "status": s.status,
        "data_solicitacao": s.data_solicitacao,
        "data_aprovacao": s.data_aprovacao
    } for s in statuses])

    if not df.empty:
        if "motivo_rejeicao" in df.columns:
            df["motivo_rejeicao_anon"] = df["motivo_rejeicao"].apply(anonimize_text)
        if "status" in df.columns:
            df["status_anon"] = df["status"].apply(anonimize_text)

    
    for _, row in df.iterrows():
        status_anon = Status_aprovacao(
            None,
            row.get("motivo_rejeicao_anon"),
            row.get("status_anon"),
            row.get("data_solicitacao"),
            row.get("data_aprovacao")
        )
        inserir_status_aprovacao(status_anon)

    return df

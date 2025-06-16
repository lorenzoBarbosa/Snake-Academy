from data.resposta_chamado.resposta_chamado_model import resposta_chamado
from data.resposta_chamado.resposta_chamado_sql import *
from data.util import get_connection


def criar_tabela_resposta_chamado():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_RESPOSTA_CHAMADO)
    conn.commit()
    conn.close()

def gerar_resposta_chamado(resposta_chamado: resposta_chamado):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(GERAR_RESPOSTA_CHAMADO, (
        resposta_chamado.feedback,
        resposta_chamado.dataEnvio,
        resposta_chamado.horaEnvio,
        resposta_chamado.visualizacao,
        resposta_chamado.idAdmin))
    conn.commit()
    conn.close()

def obter_todos_resposta_chamados() -> list[resposta_chamado]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_RESPOSTA_CHAMADOS)
    tuplas = cursor.fetchall()
    conn.close()
    resposta_chamados = [
        resposta_chamado(
            id=tupla[0],
            feedback=tupla[1],
            dataEnvio=tupla[2],
            horaEnvio=tupla[3],
            vizualizacao=tupla[4],
            iAdmin=tupla[5]    
            ) for tupla in tuplas ]
    conn.close()
    return resposta_chamados


def obter_resposta_chamado_por_idAdmin(idAdmin: int) -> resposta_chamado:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_RESPOSTA_CHAMADO_POR_ID_ADMIN, (idAdmin,))
    tupla = cursor.fetchone()
    conn.close()
    
    if tupla:
        return resposta_chamado(*tupla)
    return None

def excluir_resposta_chamado_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_RESPOSTA_CHAMADO_POR_ID, (id,))
    conn.commit()
    conn.close()

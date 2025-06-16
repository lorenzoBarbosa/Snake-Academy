from data.chamado.chamado_model import Chamado
from data.chamado.chamado_sql import *
from data.util import get_connection


def criar_tabela_chamado():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_CHAMADO)
    conn.commit()
    conn.close()

def gerar_chamado(chamado: Chamado):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(GERAR_CHAMADO, (
        chamado.descricao,
        chamado.dataEnvio,
        chamado.horaEnvio,
        chamado.visualizacao,
        chamado.idUsuario))
    conn.commit()
    conn.close()

def obter_todos_chamados() -> list[Chamado]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CHAMADOS)
    tuplas = cursor.fetchall()
    conn.close()
    chamados = [
        Chamado(
            id=tupla[0],
            descricao=tupla[1],
            dataEnvio=tupla[2],
            horaEnvio=tupla[3],
            visualizacao=tupla[4],
            idUsuario=tupla[5]    
            ) for tupla in tuplas ]
    conn.close()
    return chamados


def obter_chamado_por_id_usuario(id_usuario: int) -> Chamado:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CHAMADO_POR_ID_USUARIO, (id_usuario,))
    tupla = cursor.fetchone()
    conn.close()
    
    if tupla:
        return Chamado(*tupla)
    return None

def excluir_chamado_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_CHAMADO_POR_ID, (id,))
    conn.commit()
    conn.close()

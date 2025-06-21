from typing import Optional, List
from data.chamado.chamado_model import Chamado
from data.chamado.chamado_sql import *
from data.usuario.usuario_model import Usuario
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
        chamado["idUsuario"],
        chamado["descricao"],
        chamado["dataEnvio"],
        chamado["horaEnvio"],
        chamado["visualizacao"]))
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
            idUsuario=tupla[1],
            descricao=tupla[2],
            dataEnvio=tupla[3],
            horaEnvio=tupla[4],
            visualizacao=tupla[5]    
            ) for tupla in tuplas ]
    conn.close()
    return chamados

def obter_chamado_por_id(id: int) -> Chamado:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CHAMADO_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        return Chamado(
            id=tupla["id"],
            idUsuario=Usuario(id=tupla["idUsuario"], nome=tupla["nomeUsuario"]),
            descricao=tupla["descricao"],
            dataEnvio=tupla["dataEnvio"],
            horaEnvio=tupla["horaEnvio"],
            visualizacao=tupla["visualizacao"]
        )
    return None

def obter_chamado_paginado(pg_num: int, pg_size: int) -> list[Chamado]:
    limit = pg_size
    offset = (pg_num-1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CHAMADO_PAGINADO, (limit, offset))
    tuplas = cursor.fetchall()
    chamados = [
        Chamado(
            id=tupla["id"],
            idUsuario=Usuario(id=tupla["idUsuario"], nome=tupla["nomeUsuario"]),
            descricao=tupla["descricao"],
            dataEnvio=tupla["dataEnvio"],
            horaEnvio=tupla["horaEnvio"],
            visualizacao=tupla["visualizacao"]
        ) for tupla in tuplas
    ]
    conn.close()
    return chamados

def obter_chamado_por_termo_paginado(termo, pg_num, pg_size):
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    termo = f"%{termo}%"
    conn = get_connection
    cursor = conn.cursor()
    cursor.execute(OBTER_CHAMADO_POR_TERMO_PAGINADO(termo, termo, termo, limit, offset))
    tuplas = cursor.fetchall()
    chamados = [
        Chamado(
            id=tupla["id"],
            idUsuario=Usuario(id=tupla["idUsuario"], nome=tupla["nomeUsuario"]),
            descricao=tupla["descricao"],
            dataEnvio=tupla["dataEnvio"],
            horaEnvio=tupla["horaEnvio"],
            visualizacao=tupla["visualizacao"]
        )for tupla in tuplas
    ]
    return chamados

def obter_quantidade_chamados():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_CHAMADOS)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_chamados_por_nome_usuario(nome:str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_CHAMADOS_POR_NOME_USUARIO(nome))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_chamado_por_nome_usuario(nome: str) -> Optional[Chamado]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CHAMADO_POR_NOME_USUARIO, (nome,))
    tuplas = cursor.fetchall()
    conn.close()
    chamados = [Chamado(
            id=tupla["id"],
            idUsuario=Usuario(id=tupla["idUsuario"], nome=tupla["nomeUsuario"]),
            descricao=tupla["descricao"],
            dataEnvio=tupla["dataEnvio"],
            horaEnvio=tupla["horaEnvio"],
            visualizacao=tupla["visualizacao"]
        ) for tupla in tuplas
    ]
    return chamados

def excluir_chamado_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_CHAMADO_POR_ID, (id,))
    conn.commit()
    conn.close()

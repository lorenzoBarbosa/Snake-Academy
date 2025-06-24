from data.comunidade.comunidade_sql import *
from data.comunidade.comunidade_sql import *
from data.comunidade.comunidade_sql import *
from data.util import get_connection


def criar_tabela_comunidade():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_COMUNIDADE)
    conn.commit()
    conn.close()

def inserir_comunidade(comunidade: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        INSERIR_COMUNIDADE,
        (
            comunidade["idCurso"],
            comunidade["nome"],
            comunidade["quantidadeParticipantes"],
            comunidade["listaParticipantes"]
        )
    )
    conn.commit()
    conn.close()
    

def obter_todas_comunidades() -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_COMUNIDADE)
    tuplas = cursor.fetchall()
    conn.close()
    comunidades = [
        {
            "id": tupla[0],
            "idCurso": tupla[1],
            "nomeCurso": tupla[2],
            "nome": tupla[3],
            "quantidadeParticipantes": tupla[4],
            "listaParticipantes": tupla[5]
        } for tupla in tuplas ]
    return comunidades
        
def obter_comunidades_paginado(pg_num: int, pg_size: int) -> list[dict]:
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_COMUNIDADES_PAGINADO, (limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    comunidades = [
        {
            "id": tupla[0],
            "idCurso": tupla[1],
            "nomeCurso": tupla[2],
            "nome": tupla[3],
            "quantidadeParticipantes": tupla[4],
            "listaParticipantes": tupla[5]
        } for tupla in tuplas ]
    return comunidades

def obter_comunidade_por_id(id: int) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_COMUNIDADE_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        comunidade = {
            "id": tupla[0],
            "idCurso": tupla[1],
            "nomeCurso": tupla[2],
            "nome": tupla[3],
            "quantidadeParticipantes": tupla[4],
            "listaParticipantes": tupla[5]
        }
        return comunidade
    return None

def obter_comunidade_por_nome_curso(nome_curso: str) -> dict:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_COMUNIDADE_POR_NOME_CURSO, (nome_curso,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        comunidade = {
            "id": tupla[0],
            "idCurso": tupla[1],
            "nomeCurso": tupla[2],
            "nome": tupla[3],
            "quantidadeParticipantes": tupla[4],
            "listaParticipantes": tupla[5]
        }
        return comunidade
    return None

def obter_comunidade_por_termo_paginado(termo: str, pg_num: int, pg_size: int) -> list[dict]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_COMUNIDADE_POR_TERMO_PAGINADO, (termo, pg_size, (pg_num - 1) * pg_size))
    tuplas = cursor.fetchall()
    conn.close()
    comunidades = [
        {
            "id": tupla[0],
            "idCurso": tupla[1],
            "nomeCurso": tupla[2],
            "nome": tupla[3],
            "quantidadeParticipantes": tupla[4],
            "listaParticipantes": tupla[5]
        } for tupla in tuplas ]
    return comunidades

def obter_quantidade_comunidades() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_COMUNIDADES)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_comunidades_por_nome_curso(nome_curso: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_COMUNIDADES_POR_NOME_CURSO, (nome_curso,))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_comunidade(comunidade: dict):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        ATUALIZAR_COMUNIDADE,
        (
            comunidade["idCurso"],
            comunidade["quantidadeParticipantes"],
            comunidade["listaParticipantes"],
            comunidade["id"]
        )
    )
    conn.commit()
    conn.close()
    return None

def excluir_comunidade_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_COMUNIDADE_POR_ID, (id,))
    conn.commit()
    conn.close()
    return None
import json
from data.modulo.modulo_model import Modulo
from data.modulo.modulo_sql import *
from data.util import get_connection


def criar_tabela_modulo():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_MODULO)
    conn.commit()
    conn.close()

def inserir_modulo(modulo: Modulo):
    conn = get_connection()
    cursor = conn.cursor()
    listaAulas = json.dumps(modulo["listaAulas"])
    listaExercicios = json.dumps(modulo["listaExercicios"])
    cursor.execute(INSERIR_MODULO,
        (
            modulo["idCurso"],
            modulo["titulo"],
            modulo["descricaoModulo"],
            listaAulas,
            listaExercicios
        ))
    conn.commit()
    conn.close()

def obter_todos_modulos() -> list[Modulo]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MODULOS)
    tuplas = cursor.fetchall()
    modulos = [
        Modulo(
            id=tupla[0],
            idCurso=tupla[1],
            nomeCurso=tupla[2],
            titulo=tupla[3],
            descricaoModulo=tupla[4],
            listaAulas=tupla[5],
            listaExercicios=tupla[6]
        ) for tupla in tuplas
    ]
    conn.close()
    return modulos

def obter_modulos_paginado(pg_num: int, pg_size: int) -> list[Modulo]:
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MODULOS_PAGINADO, (limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    modulos = [
        Modulo(
            id=tupla[0],
            idCurso=tupla[1],
            nomeCurso=tupla[2],
            titulo=tupla[3],
            descricaoModulo=tupla[4],
            listaAulas=tupla[5],
            listaExercicios=tupla[6]
        ) for tupla in tuplas
    ]
    return modulos

def obter_modulo_por_id(id_modulo: int) -> Modulo:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MODULO_POR_ID, (id_modulo,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        return Modulo(
            id=tupla[0],
            idCurso=tupla[1],
            nomeCurso=tupla[2],
            titulo=tupla[3],
            descricaoModulo=tupla[4],
            listaAulas=tupla[5],
            listaExercicios=tupla[6]
        )
    return None

def obter_modulos_por_curso_paginado(id_curso: int, pg_num: int, pg_size: int) -> list[Modulo]:
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MODULO_POR_CURSO_PAGINADO, (id_curso, limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    modulos = [
        Modulo(
            id=tupla[0],
            idCurso=tupla[1],
            nomeCurso=tupla[2],
            titulo=tupla[3],
            descricaoModulo=tupla[4],
            listaAulas=tupla[5],
            listaExercicios=tupla[6]
        ) for tupla in tuplas
    ]
    return modulos
    
def obter_quantidade_modulos() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_MODULOS)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_modulos_por_curso(id_curso: int) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_MODULOS_POR_CURSO, (id_curso,))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_modulo_por_id(id_modulo: int, modulo: Modulo):
    conn = get_connection()
    cursor = conn.cursor()
    listaAulas = json.dumps(modulo["listaAulas"])
    listaExercicios = json.dumps(modulo["listaExercicios"])
    cursor.execute(ATUALIZAR_MODULO_POR_ID,
        (
            modulo["idCurso"],
            modulo["titulo"],
            modulo["descricaoModulo"],
            listaAulas,
            listaExercicios,
            id_modulo
        ))
    conn.commit()
    conn.close()

def excluir_modulo_por_id(id_modulo: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_MODULO_POR_ID, (id_modulo,))
    conn.commit()
    conn.close()
    
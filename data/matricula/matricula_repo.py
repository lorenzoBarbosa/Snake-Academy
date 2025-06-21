from data.matricula.matricula_sql import *
from data.util import get_connection
from data.matricula.matricula_model import Matricula


def criar_tabela_matricula():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_MATRICULA)
    conn.commit()
    conn.close()

def inserir_matricula(matricula: Matricula):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        INSERIR_MATRICULA,
        (
            matricula["idCliente"],
            matricula["idCurso"],
            matricula["statusMatricula"],
            matricula["desempenho"],
            matricula["frequencia"],
            matricula["dataMatricula"]
        )
    )
    conn.commit()
    conn.close()

def obter_todas_matriculas() -> list[Matricula]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MATRICULAS)
    tuplas = cursor.fetchall()
    conn.close()
    matriculas = [
        Matricula(
            idMatricula=tupla[0],
            idCliente=tupla[1],
            nome=tupla[2],
            email=tupla[3],
            senha=tupla[4],
            telefone=tupla[5],
            idCurso=tupla[6],
            nomeCurso=tupla[7],
            statusMatricula=tupla[8],
            desempenho=tupla[9],
            frequencia=tupla[10],
            dataMatricula=tupla[11]
        ) for tupla in tuplas ]
    return matriculas

def obter_matriculas_paginado(pg_num: int, pg_size: int) -> list[Matricula]:
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MATRICULAS_PAGINADO, (limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    matriculas = [
        Matricula(
            idMatricula=tupla[0],
            idCliente=tupla[1],
            nome=tupla[2],
            email=tupla[3],
            senha=tupla[4],
            telefone=tupla[5],
            idCurso=tupla[6],
            nomeCurso=tupla[7],
            statusMatricula=tupla[8],
            desempenho=tupla[9],
            frequencia=tupla[10],
            dataMatricula=tupla[11]
        ) for tupla in tuplas ]
    return matriculas

def obter_matricula_por_id(id: int) -> Matricula:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MATRICULA_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        matricula = Matricula(
            idMatricula=tupla[0],
            idCliente=tupla[1],
            nome=tupla[2],
            email=tupla[3],
            senha=tupla[4],
            telefone=tupla[5],
            idCurso=tupla[6],
            nomeCurso=tupla[7],
            statusMatricula=tupla[8],
            desempenho=tupla[9],
            frequencia=tupla[10],
            dataMatricula=tupla[11]
        )
        return matricula
    return None


def atualizar_matricula(id: int, matricula: Matricula):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        ATUALIZAR_MATRICULA_POR_ID,
        (
            matricula["idCliente"],
            matricula["idCurso"],
            matricula["statusMatricula"],
            matricula["desempenho"],
            matricula["frequencia"],
            matricula["dataMatricula"],
            id
        )
    )
    conn.commit()
    conn.close()

def excluir_matricula(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_MATRICULA_POR_ID, (id,))
    conn.commit()
    conn.close()
    
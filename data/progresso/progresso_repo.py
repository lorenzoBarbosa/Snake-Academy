from data.progresso.progresso_model import Progresso
from data.progresso.progresso_sql import *
from data.util import get_connection


def criar_tabela_progresso():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_PROGRESSO)
    conn.commit()
    conn.close()

def inserir_progresso(progresso: Progresso):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        INSERIR_PROGRESSO,
        (
            progresso["idAula"],
            progresso["idMatricula"],
            progresso["dataInicio"],
            progresso["dataFim"],
            progresso["statusAula"],
            progresso["porcentagemConclusao"]
        )
    )
    conn.commit()
    conn.close()

def obter_todos_progresso() -> list[Progresso]: 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_PROGRESSO)
    tuplas = cursor.fetchall()
    conn.close()
    progresso_list = [
        Progresso(
            id=tupla[0],
            idAula=tupla[1],
            tituloAula=tupla[2],
            idMatricula=tupla[3],
            nome=tupla[4],
            dataInicio=tupla[5],
            dataFim=tupla[6],
            statusAula=tupla[7],
            porcentagemConclusao=tupla[8]
        ) for tupla in tuplas ]
    return progresso_list

def obter_progresso_paginado(limite: int, offset: int) -> list[Progresso]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_PROGRESSO_PAGINADO, (limite, offset))
    tuplas = cursor.fetchall()
    conn.close()
    progresso_list = [
        Progresso(
            id=tupla[0],
            idAula=tupla[1],
            tituloAula=tupla[2],
            idMatricula=tupla[3],
            nome=tupla[4],
            dataInicio=tupla[5],
            dataFim=tupla[6],
            statusAula=tupla[7],
            porcentagemConclusao=tupla[8]
        ) for tupla in tuplas ]
    return progresso_list

def obter_progresso_por_id(id: int) -> Progresso: 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_PROGRESSO_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        return Progresso(
            id=tupla[0],
            idAula=tupla[1],
            tituloAula=tupla[2],
            idMatricula=tupla[3],
            nome=tupla[4],
            dataInicio=tupla[5],
            dataFim=tupla[6],
            statusAula=tupla[7],
            porcentagemConclusao=tupla[8]
        )
    return None

def obter_progresso_por_aula(id_aula: int, limite: int, offset: int) -> list[Progresso]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_PROGRESSO_POR_AULA, (id_aula, limite, offset))
    tuplas = cursor.fetchall()
    conn.close()
    progresso_list = [
        Progresso(
            id=tupla[0],
            idAula=tupla[1],
            tituloAula=tupla[2],
            idMatricula=tupla[3],
            nome=tupla[4],
            dataInicio=tupla[5],
            dataFim=tupla[6],
            statusAula=tupla[7],
            porcentagemConclusao=tupla[8]
        ) for tupla in tuplas ]
    return progresso_list

def obter_progresso_por_matricula(id_matricula: int, limite: int, offset: int) -> list[Progresso]: 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_PROGRESSO_POR_MATRICULA, (id_matricula, limite, offset))
    tuplas = cursor.fetchall()
    conn.close()
    progresso_list = [
        Progresso(
            id=tupla[0],
            idAula=tupla[1],
            tituloAula=tupla[2],
            idMatricula=tupla[3],
            nome=tupla[4],
            dataInicio=tupla[5],
            dataFim=tupla[6],
            statusAula=tupla[7],
            porcentagemConclusao=tupla[8]
        ) for tupla in tuplas ]
    return progresso_list

def obter_quantidade_progresso_por_aula(id_aula: int) -> int: 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_PROGRESSO_POR_AULA, (id_aula,))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_progresso_por_matricula(id_matricula: int) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_PROGRESSO_POR_MATRICULA, (id_matricula,))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_progresso() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_PROGRESSO)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_progresso_por_id(id: int, progresso: Progresso): 
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        ATUALIZAR_PROGRESSO_POR_ID,
        (
            progresso.idAula,
            progresso.idMatricula,
            progresso.dataInicio,
            progresso.dataFim,
            progresso.statusAula,
            progresso.porcentagemConclusao,
            id
        )
    )
    conn.commit()
    conn.close() 
    return cursor.rowcount > 0

def atualizar_progresso_por_matricula_e_aula(id_matricula: int, id_aula: int, progresso: Progresso):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        ATUALIZAR_PROGRESSO_POR_MATRICULA_E_AULA,
        (
            progresso["dataInicio"],
            progresso["dataFim"],
            progresso["statusAula"],
            progresso["porcentagemConclusao"],
            id_matricula,
            id_aula
        )
    )
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def excluir_progresso_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_PROGRESSO_POR_ID, (id,))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0

def excluir_progresso_por_matricula_e_aula(id_matricula: int, id_aula: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_PROGRESSO_POR_MATRICULA_E_AULA, (id_matricula, id_aula))
    conn.commit()
    conn.close()
    return cursor.rowcount > 0
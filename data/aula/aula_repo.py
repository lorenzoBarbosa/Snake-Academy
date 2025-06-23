from data.aula.aula_model import Aula
from data.aula.aula_sql import *
from data.util import get_connection


def criar_tabela_aula():
    conn= get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_AULA)
    conn.commit()
    conn.close()

def inserir_aula(aula):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        INSERIR_AULA,
        (
            aula["idModulo"],
            aula["titulo"],
            aula["descricaoAula"],
            aula["duracaoAula"],
            aula["tipo"],
            aula["ordem"],
            aula["dataDisponibilidade"]
        )
    )
    conn.commit()
    conn.close()   

def obter_todas_aulas() -> list[Aula]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_AULAS)
    tuplas = cursor.fetchall()
    conn.close()
    usuarios = [
        Aula(
            id=tupla[0],
            idModulo=tupla[1],
            nomeCurso=tupla[2],
            tituloModolo=tupla[3],
            titulo=tupla[4],
            descricaoAula=tupla[5],
            duracaoAula=tupla[6],
            tipo=tupla[7],
            ordem=tupla[8],
            dataDisponibilidade=tupla[9]    
            ) for tupla in tuplas ]
    conn.close()
    return usuarios
    
def obter_aula_por_id(id: int) -> Aula:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_AULA_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        return Aula(
            id=tupla[0],
            idModulo=tupla[1],
            nomeCurso=tupla[2],
            tituloModolo=tupla[3],
            titulo=tupla[4],
            descricaoAula=tupla[5],
            duracaoAula=tupla[6],
            tipo=tupla[7],
            ordem=tupla[8],
            dataDisponibilidade=tupla[9]
        )
    return None

def obter_aula_paginada_por_modulo(id_modulo: int, limite: int, offset: int) -> list[Aula]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_AULAS_PAGINADO_POR_MODULO, (id_modulo, limite, offset))
    tuplas = cursor.fetchall()
    conn.close()
    aulas = [
        Aula(
            id=tupla[0],
            idModulo=tupla[1],
            nomeCurso=tupla[2],
            tituloModolo=tupla[3],
            titulo=tupla[4],
            descricaoAula=tupla[5],
            duracaoAula=tupla[6],
            tipo=tupla[7],
            ordem=tupla[8],
            dataDisponibilidade=tupla[9]
        ) for tupla in tuplas ]
    return aulas

def obter_aula_por_titulo(titulo: str, limite: int, offset: int) -> list[Aula]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_AULA_POR_TITULO, (f"%{titulo}%", limite, offset))
    tuplas = cursor.fetchall()
    conn.close()
    aulas = [
        Aula(
            id=tupla[0],
            idModulo=tupla[1],
            nomeCurso=tupla[2],
            tituloModolo=tupla[3],
            titulo=tupla[4],
            descricaoAula=tupla[5],
            duracaoAula=tupla[6],
            tipo=tupla[7],
            ordem=tupla[8],
            dataDisponibilidade=tupla[9]
        ) for tupla in tuplas ]
    return aulas

def obter_quantidade_aulas() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_AULAS)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_aulas_por_modulo(id_modulo: int) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_AULAS_POR_MODULO, (id_modulo,))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_aula_por_id(aula: Aula):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        ATUALIZAR_AULA_POR_ID,
        (
            aula.idModulo,
            aula.titulo,
            aula.descricaoAula,
            aula.duracaoAula,
            aula.tipo,
            aula.ordem,
            aula.dataDisponibilidade,
            aula.id
        )
    )
    conn.commit()
    conn.close()

def excluir_aula_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_AULA_POR_ID, (id,))
    conn.commit()
    conn.close()

 
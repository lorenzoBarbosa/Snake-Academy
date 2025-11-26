from data.aula.aula_model import Aula
from data.aula.aula_sql import *
from data.modulo.modulo_repo import obter_modulo_por_id
from data.util import get_connection


def criar_tabela_aula():
    try:
        conn= get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_AULA)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

def inserir_aula(aula: Aula):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            INSERIR_AULA,
            (
                aula.idModulo,
                aula.titulo,
                aula.descricaoAula,
                aula.duracaoAula,
                aula.url,
                aula.videoId,
                aula.status,
                aula.dataDisponibilidade
            )
        )
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir aula: {e}")

def obter_todas_aulas() -> list[Aula]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_AULAS)
        tuplas = cursor.fetchall()
        conn.close()
        usuarios = [
            Aula(
                id=tupla[0],
                idModulo=tupla["idModulo"],
                titulo=tupla["titulo"],
                descricaoAula=tupla["descricaoAula"],
                duracaoAula=tupla["duracaoAula"],
                url=tupla["url"],
                videoId=tupla["videoId"],
                status=tupla["status"],
                dataDisponibilidade=tupla["dataDisponibilidade"]    
                ) for tupla in tuplas ]
        return usuarios
    except Exception as e:
        print(f"Erro ao obter todas as aulas: {e}")

def obter_aula_por_id(id: int) -> Aula:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_AULA_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Aula(
                id=tupla[0],
                idModulo= tupla["idModulo"],
                titulo=tupla["titulo"],
                descricaoAula=tupla["descricaoAula"],
                duracaoAula=tupla["duracaoAula"],
                url=tupla["url"],
                videoId=tupla["videoId"],
                status=tupla["status"],
                dataDisponibilidade=tupla["dataDisponibilidade"],
                modulo = obter_modulo_por_id(tupla["idModulo"]),
                nomeCurso = tupla["nomeCurso"]
            )
    except Exception as e:
        print(f"Erro ao obter aula por id: {e}")
        return None

def obter_aula_paginada_por_modulo(id_modulo: int, limite: int, offset: int) -> list[Aula]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_AULAS_PAGINADO_POR_MODULO, (id_modulo, limite, offset))
        tuplas = cursor.fetchall()
        conn.close()
        aulas = [
            Aula(
                id=tupla[0],
                idModulo=tupla["idModulo"],
                titulo=tupla["titulo"],
                descricaoAula=tupla["descricaoAula"],
                duracaoAula=tupla["duracaoAula"],
                url=tupla["url"],
                videoId=tupla["videoId"],
                status=tupla["status"],
                dataDisponibilidade=tupla["dataDisponibilidade"]
            ) for tupla in tuplas ]
        return aulas
    except Exception as e:
        print(f"Erro ao obter aulas paginadas por módulo: {e}")
        return []

def obter_aula_por_titulo(titulo: str, limite: int, offset: int) -> list[Aula]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_AULA_POR_TITULO, (f"%{titulo}%", limite, offset))
        tuplas = cursor.fetchall()
        conn.close()
        aulas = [
            Aula(
                id=tupla[0],
                idModulo=tupla["idModulo"],
                titulo=tupla["titulo"],
                descricaoAula=tupla["descricaoAula"],
                duracaoAula=tupla["duracaoAula"],
                url=tupla["url"],
                videoId=tupla["videoId"],
                status=tupla["status"],
                dataDisponibilidade=tupla["dataDisponibilidade"]
            ) for tupla in tuplas ]
        return aulas
    except Exception as e:
        print(f"Erro ao obter aula por título: {e}")
        return []

def obter_quantidade_aulas() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_AULAS)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de aulas: {e}")
        return 0

def obter_quantidade_aulas_por_modulo(id_modulo: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_AULAS_POR_MODULO, (id_modulo,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de aulas por módulo: {e}")
        return 0

def atualizar_aula_por_id(aula: Aula):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            ATUALIZAR_AULA_POR_ID,
            (
                aula.idModulo,
                aula.titulo,
                aula.descricaoAula,
                aula.duracaoAula,
                aula.url,
                aula.videoId,
                aula.status,
                aula.dataDisponibilidade,
                aula.id
            )
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao atualizar aula por id: {e}")

def excluir_aula_por_id(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_AULA_POR_ID, (id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao excluir aula por id: {e}")
import json
from data.comunidade.comunidade_model import Comunidade
from data.comunidade.comunidade_sql import *
from data.curso import curso_repo
from data.util import get_connection


def criar_tabela_comunidade():
    try:    
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_COMUNIDADE)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro a tabela não foi criada: {e}")

def inserir_comunidade(comunidade: Comunidade):
    try:    
        conn = get_connection()
        cursor = conn.cursor()
        listaParticipantes = json.dumps(comunidade.listaParticipantes)
        cursor.execute(
            INSERIR_COMUNIDADE,
            (
                comunidade.idCurso.id,
                comunidade.nome,
                comunidade.quantidadeParticipantes,
                listaParticipantes
            )
        )
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro os dados não foram inseridos: {e}")
        
def obter_comunidades_paginado(pg_num: int, pg_size: int) -> list[dict]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMUNIDADES_PAGINADO, (limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        comunidades = [
            Comunidade (
                id = tupla[0],
                idCurso = tupla[1],
                nome = tupla[3],
                quantidadeParticipantes = tupla[4],
                listaParticipantes = json.loads(tupla[5]),
                nomeCurso = curso_repo.obter_curso_por_id(tupla[2],)
                ) for tupla in tuplas ]
        
        return comunidades
    except Exception as e:
        print(f"Erro ao obter comunidades paginadas: {e}")
        return []

def obter_comunidade_por_id(id: int) -> dict:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMUNIDADE_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Comunidade (
                id = tupla[0],
                idCurso = tupla[1],
                nome = tupla[3],
                quantidadeParticipantes = tupla[4],
                listaParticipantes = json.loads(tupla[5]),
                nomeCurso = curso_repo.obter_curso_por_id(tupla[2],)
                )
    except Exception as e:
        print(f"Erro ao obter comunidade por id: {e}")
        return None

def obter_comunidade_por_nome_curso(nome_curso: str) -> dict:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMUNIDADE_POR_NOME_CURSO, (nome_curso,))
        tuplas = cursor.fetchall()
        conn.close()
        comunidade = [
            Comunidade (
                id = tupla[0],
                idCurso = tupla[1],
                nome = tupla[3],
                quantidadeParticipantes = tupla[4],
                listaParticipantes = json.loads(tupla[5]),
                nomeCurso = curso_repo.obter_curso_por_id(tupla[2],)
                ) for tupla in tuplas ]
        return comunidade
    except Exception as e:
        print(f"Erro ao obter comunidade por nome do curso: {e}")
        return []

def obter_todas_comunidades() -> list[dict]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMUNIDADE)
        tuplas = cursor.fetchall()
        conn.close()
        comunidade = [
            Comunidade (
                id = tupla[0],
                idCurso = tupla[1],
                nome = tupla[3],
                quantidadeParticipantes = tupla[4],
                listaParticipantes = json.loads(tupla[5]),
                nomeCurso = curso_repo.obter_curso_por_id(tupla[2],)
                ) for tupla in tuplas ]
        return comunidade
    except Exception as e:
        print(f"Erro ao obter todas as comunidades: {e}")
        return []

def obter_comunidade_por_termo_paginado(termo: str, pg_num: int, pg_size: int) -> list[dict]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMUNIDADE_POR_TERMO_PAGINADO, (f"%{termo}%", f"%{termo}%", pg_size, (pg_num - 1) * pg_size))
        tuplas = cursor.fetchall()
        conn.close()
        comunidade = [
            Comunidade (
                id = tupla[0],
                idCurso = tupla[1],
                nome = tupla[3],
                quantidadeParticipantes = tupla[4],
                listaParticipantes = json.loads(tupla[5]),
                nomeCurso = curso_repo.obter_curso_por_id(tupla[2],)
                ) for tupla in tuplas ]
        return comunidade
    except Exception as e:
        print(f"Erro ao obter comunidade por termo paginado: {e}")
        return []

def obter_quantidade_comunidades() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_COMUNIDADES)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de comunidades: {e}")
        return 0

def obter_quantidade_comunidades_por_nome_curso(nome_curso: str) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_COMUNIDADES_POR_NOME_CURSO, (nome_curso,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de comunidades por nome do curso: {e}")
        return 0

def atualizar_comunidade(id: int, comunidade: Comunidade):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        listaParticipantes = json.dumps(comunidade.listaParticipantes)
        cursor.execute(
            ATUALIZAR_COMUNIDADE,
            (
                comunidade.idCurso,
                comunidade.nome,
                comunidade.quantidadeParticipantes,
                listaParticipantes,
                id
            )
        )
        conn.commit()
        conn.close()
        return None
    except Exception as e:
        print(f"Erro ao atualizar comunidade: {e}")
        return None

def excluir_comunidade_por_id(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_COMUNIDADE_POR_ID, (id,))
        conn.commit()
        conn.close()
        return None
    except Exception as e:
        print(f"Erro ao excluir comunidade por id: {e}")
        return None

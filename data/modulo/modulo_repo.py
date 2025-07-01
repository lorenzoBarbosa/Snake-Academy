import json
from data.curso.curso_repo import obter_curso_por_id
from data.modulo.modulo_model import Modulo
from data.modulo.modulo_sql import *
from data.util import get_connection


def criar_tabela_modulo():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_MODULO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

def inserir_modulo(modulo: Modulo):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        listaAulas = json.dumps(modulo.listaAulas)
        listaExercicios = json.dumps(modulo.listaExercicios)
        cursor.execute(INSERIR_MODULO,
            (
                modulo.idCurso,
                modulo.titulo,
                modulo.descricaoModulo,
                listaAulas,
                listaExercicios
            ))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir modulo: {e}")

def obter_todos_modulos() -> list[Modulo]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MODULOS)
        tuplas = cursor.fetchall()
        modulos = [
            Modulo(
                id=tupla["id"],
                idCurso=tupla["idCurso"],
                titulo=tupla["titulo"],
                descricaoModulo=tupla["descricaoModulo"],
                listaAulas=tupla["listaAulas"],
                listaExercicios=tupla["listaExercicios"],
                curso = obter_curso_por_id(tupla["idCurso"])
            ) for tupla in tuplas
        ]
        conn.close()
        return modulos
    except Exception as e:
        print(f"Erro ao obter todos os módulos: {e}")

def obter_modulos_paginado(pg_num: int, pg_size: int) -> list[Modulo]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MODULOS_PAGINADO, (limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        modulos = [
            Modulo(
                id=tupla["id"],
                idCurso=tupla["idCurso"],
                titulo=tupla["titulo"],
                descricaoModulo=tupla["descricaoModulo"],
                listaAulas=tupla["listaAulas"],
                listaExercicios=tupla["listaExercicios"],
                curso = obter_curso_por_id(tupla["idCurso"])
            ) for tupla in tuplas
        ]
        return modulos
    except Exception as e:
        print(f"Erro ao obter módulos paginados: {e}")

def obter_modulo_por_id(id_modulo: int) -> Modulo:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MODULO_POR_ID, (id_modulo,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Modulo(
                id=tupla["id"],
                idCurso=tupla["idCurso"],
                titulo=tupla["titulo"],
                descricaoModulo=tupla["descricaoModulo"],
                listaAulas=tupla["listaAulas"],
                listaExercicios=tupla["listaExercicios"],
                curso = obter_curso_por_id(tupla["idCurso"])
            )
        return None
    except Exception as e:
        print(f"Erro ao obter módulo por id: {e}")

def obter_modulos_por_curso_paginado(id_curso: int, pg_num: int, pg_size: int) -> list[Modulo]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MODULO_POR_CURSO_PAGINADO, (id_curso, limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        modulos = [
            Modulo(
                id=tupla["id"],
                idCurso=tupla["idCurso"],
                titulo=tupla["titulo"],
                descricaoModulo=tupla["descricaoModulo"],
                listaAulas=tupla["listaAulas"],
                listaExercicios=tupla["listaExercicios"],
                curso = obter_curso_por_id(tupla["idCurso"])
            ) for tupla in tuplas
        ]
        return modulos
    except Exception as e:
        print(f"Erro ao obter módulos por curso paginado: {e}")

def obter_quantidade_modulos() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_MODULOS)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de módulos: {e}")

def obter_quantidade_modulos_por_curso(id_curso: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_MODULOS_POR_CURSO, (id_curso,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de módulos por curso: {e}")

def atualizar_modulo_por_id(id_modulo: int, modulo: Modulo):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        listaAulas = json.dumps(modulo.listaAulas)
        listaExercicios = json.dumps(modulo.listaExercicios)
        cursor.execute(ATUALIZAR_MODULO_POR_ID,
            (
                modulo.idCurso,
                modulo.titulo,
                modulo.descricaoModulo,
                listaAulas,
                listaExercicios,
                id_modulo
            ))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar módulo por id: {e}")

def excluir_modulo_por_id(id_modulo: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_MODULO_POR_ID, (id_modulo,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir módulo por id: {e}")

from data.curso.curso_sql import *
from data.util import get_connection
from data.curso.curso_model import Curso

def criar_tabela_curso():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_CURSO)
    conn.commit()
    conn.close()

def inserir_curso(curso: Curso):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        INSERIR_CURSO,
        (
            curso["nome"],
            curso["idProfessor"],
            curso["custo"],
            curso["descricaoCurso"],
            curso["duracaoCurso"],
            curso["avaliacao"],
            curso["dataCriacao"],
            curso["statusCurso"]
        )
    )
    conn.commit()
    conn.close()

def obter_todos_cursos() -> list[Curso]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CURSOS)
    tuplas = cursor.fetchall()
    conn.close()
    cursos = [
        Curso(
            id=tupla[0],
            nome=tupla[1],
            idProfessor=tupla[2],
            nomeProfessor=tupla[3],
            custo=tupla[4],
            descricaoCurso=tupla[5],
            duracaoCurso=tupla[6],
            avaliacao=tupla[7],
            dataCriacao=tupla[8],
            statusCurso=tupla[9]
        ) for tupla in tuplas ]
    return cursos

def obter_cursos_paginado(pg_num: int, pg_size: int) -> list[Curso]:
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CURSOS_PAGINADO, (limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    cursos = [
        Curso(
            id=tupla[0],
            nome=tupla[1],
            idProfessor=tupla[2],
            nomeProfessor=tupla[3],
            custo=tupla[4],
            descricaoCurso=tupla[5],
            duracaoCurso=tupla[6],
            avaliacao=tupla[7],
            dataCriacao=tupla[8],
            statusCurso=tupla[9]
        ) for tupla in tuplas ]
    return cursos

def obter_curso_por_id(id: int) -> Curso:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CURSO_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        return Curso(
            id=tupla[0],
            nome=tupla[1],
            idProfessor=tupla[2],
            nomeProfessor=tupla[3],
            custo=tupla[4],
            descricaoCurso=tupla[5],
            duracaoCurso=tupla[6],
            avaliacao=tupla[7],
            dataCriacao=tupla[8],
            statusCurso=tupla[9]
        )
    return None

def obter_curso_por_termo_paginado(termo: str, pg_num: int, pg_size: int) -> list[Curso]:
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CURSO_POR_TERMO_PAGINADO, ('%' + termo + '%', '%' + termo + '%', '%' + termo + '%', limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    cursos = [
        Curso(
            id=tupla[0],
            nome=tupla[1],
            idProfessor=tupla[2],
            nomeProfessor=tupla[3],
            custo=tupla[4],
            descricaoCurso=tupla[5],
            duracaoCurso=tupla[6],
            avaliacao=tupla[7],
            dataCriacao=tupla[8],
            statusCurso=tupla[9]
        ) for tupla in tuplas ]
    return cursos

def obter_quantidade_cursos() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_CURSOS)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_cursos_por_nome_professor(nome_professor: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_CURSOS_POR_NOME_PROFESSOR, (nome_professor,))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_curso_por_id(curso: Curso, id:int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        ATUALIZAR_CURSO_POR_ID,
        (
        curso["nome"],
        curso["idProfessor"],
        curso["custo"],
        curso["descricaoCurso"],
        curso["duracaoCurso"],
        curso["avaliacao"],
        curso["dataCriacao"],
        curso["statusCurso"],
        id
        ))
    conn.commit()
    conn.close()

def excluir_curso_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_CURSO_POR_ID, (id,))
    conn.commit()
    conn.close()

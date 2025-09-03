from data.curso.curso_sql import *
from data.professor import professor_repo
from data.util import get_connection
from data.curso.curso_model import *

def criar_tabela_curso():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CURSO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro a tabela não foi criada: {e}")

def inserir_curso(curso: Curso):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            INSERIR_CURSO,
            (
                curso.idTopico,
                curso.nome,
                curso.idProfessor,
                curso.custo,
                curso.descricaoCurso,
                curso.duracaoCurso,
                curso.avaliacao,
                curso.dataCriacao,
                curso.statusCurso
            )
        )
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro os dados não foram inseridos: {e}")
        raise

def obter_todos_cursos() -> list[Curso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CURSOS)
        tuplas = cursor.fetchall()
        conn.close()
        cursos = [
            Curso(
                id=tupla[0],
                idTopico=tupla[1],
                nome=tupla[2],
                idProfessor=tupla[3],
                custo=tupla[5],
                descricaoCurso=tupla[6],
                duracaoCurso=tupla[7],
                avaliacao=tupla[8],
                dataCriacao=tupla[9],
                statusCurso=tupla[10],
                professor = professor_repo.obter_professor_por_id(tupla[3])
            ) for tupla in tuplas ]
        return cursos
    except Exception as e:
        print(f"Erro os cursos não foram obtidos: {e}")


def obter_cursos_paginado(pg_num: int, pg_size: int) -> list[Curso]:
    try:
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
                idTopico=tupla[1],
                nome=tupla[2],
                idProfessor=tupla[3],
                custo=tupla[5],
                descricaoCurso=tupla[6],
                duracaoCurso=tupla[7],
                avaliacao=tupla[8],
                dataCriacao=tupla[9],
                statusCurso=tupla[10],
                professor = professor_repo.obter_professor_por_id(tupla[3])
            ) for tupla in tuplas ]
        return cursos
    except Exception as e:
        print(f"Erro os cursos não foram obtidos: {e}")

def obter_curso_por_id(id: int) -> Optional[Curso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CURSO_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        curso = Curso(
                id=tupla[0],
                idTopico=tupla[1],
                nome=tupla[2],
                idProfessor=tupla[3],
                custo=tupla[4],
                descricaoCurso=tupla[5],
                duracaoCurso=tupla[6],
                avaliacao=tupla[7],
                dataCriacao=tupla[8],
                statusCurso= bool(tupla[9]),
                professor = professor_repo.obter_professor_por_id(tupla[3])
            )
        return curso
    except Exception as e:
        print(f"Erro os cursos não foram obtidos: {e}")

def obter_curso_por_termo_paginado(termo: str, pg_num: int, pg_size: int) -> list[Curso]:
    try:
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
                idTopico=tupla[1],
                nome=tupla[2],
                idProfessor=tupla[3],
                custo=tupla[4],
                descricaoCurso=tupla[5],
                duracaoCurso=tupla[6],
                avaliacao=tupla[7],
                dataCriacao=tupla[8],
                statusCurso=tupla[9],
                professor = professor_repo.obter_professor_por_id(tupla[3])
            ) for tupla in tuplas ]
        return cursos
    except Exception as e:
        print(f"Erro os cursos não foram obtidos: {e}")

def obter_quantidade_cursos() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_CURSOS)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro a quantidade de cursos não foi obtida: {e}")

def obter_quantidade_cursos_por_id_professor(idProfessor: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_CURSOS_POR_ID_PROFESSOR, (idProfessor,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro a quantidade de cursos não foi obtida: {e}")

def atualizar_curso_por_id(curso: Curso, id:int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            ATUALIZAR_CURSO_POR_ID,
            (
            curso.idTopico,
            curso.nome,
            curso.idProfessor,
            curso.custo,
            curso.descricaoCurso,
            curso.duracaoCurso,
            curso.avaliacao,
            curso.dataCriacao,
            curso.statusCurso,
            id
            ))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro os dados não foram atualizados: {e}")

def excluir_curso_por_id(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CURSO_POR_ID, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro os dados não foram atualizados: {e}")

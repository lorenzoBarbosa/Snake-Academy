from data.curso.curso_repo import *
from data.matricula.matricula_sql import *
from data.usuario.usuario_repo import *
from data.util import get_connection
from data.matricula.matricula_model import Matricula


def criar_tabela_matricula() -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_MATRICULA)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Criação da tabela não concluida: {e}")
        return False

def inserir_matricula(matricula: Matricula) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            INSERIR_MATRICULA,
            (
            matricula.idCliente,
            matricula.idCurso,
            matricula.statusMatricula,
            matricula.desempenho,
            matricula.frequencia,
            matricula.dataMatricula
            )
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao inserir matrícula: {e}")
        return False
    
def obter_todas_matriculas() -> list[Matricula]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MATRICULAS)
        tuplas = cursor.fetchall()
        conn.close()
        matriculas = [
            Matricula(
                idMatricula=tupla[0],
                idCliente=tupla[1],
                idCurso=tupla[6],
                statusMatricula=tupla[8],
                desempenho=tupla[9],
                frequencia=tupla[10],
                dataMatricula=tupla[11],
                curso = obter_curso_por_id(tupla[6]),
                usuario = obter_usuario_por_id(tupla[1])
            ) for tupla in tuplas
        ]
        return matriculas
    except Exception as e:
        print(f"Erro ao obter matrículas: {e}")
        return None

def obter_matriculas_paginadas(pg_num: int, pg_size: int) -> list[Matricula]:
    try:
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
                idCurso=tupla[6],
                statusMatricula=tupla[8],
                desempenho=tupla[9],
                frequencia=tupla[10],
                dataMatricula=tupla[11],
                curso = obter_curso_por_id(tupla[6]),
                usuario = obter_usuario_por_id(tupla[1])
            ) for tupla in tuplas
        ]
        return matriculas
    except Exception as e:
        print(f"Erro ao obter matrículas paginadas: {e}")
        return None

def obter_matricula_por_id(id: int) -> Matricula:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MATRICULA_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            matricula = Matricula(
                idMatricula=tupla[0],
                idCliente=tupla[1],
                idCurso=tupla[6],
                statusMatricula=tupla[8],
                desempenho=tupla[9],
                frequencia=tupla[10],
                dataMatricula=tupla[11],
                curso = obter_curso_por_id(tupla[6]),
                usuario = obter_usuario_por_id(tupla[1])
            ) 
            return matricula
        return None
    except Exception as e:
        print(f"Erro ao obter matrícula por ID: {e}")
        return None
    
def obter_matriculas_por_nome(nome: str) -> list[Matricula]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MATRICULA_POR_NOME, ('%' + nome + '%',))
        tuplas = cursor.fetchall()
        conn.close()
        matriculas = [
            Matricula(
                idMatricula=tupla[0],
                idCliente=tupla[1],
                idCurso=tupla[6],
                statusMatricula=tupla[8],
                desempenho=tupla[9],
                frequencia=tupla[10],
                dataMatricula=tupla[11],
                curso = obter_curso_por_id(tupla[6]),
                usuario = obter_usuario_por_id(tupla[1])
            ) for tupla in tuplas
        ]
        return matriculas
    except Exception as e:
        print(f"Erro ao obter matrículas por nome: {e}")
        return None
    
def obter_matriculas_por_curso(nome: str) -> list[Matricula]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MATRICULA_POR_CURSO, ('%' + nome + '%',))
        tuplas = cursor.fetchall()
        conn.close()
        matriculas = [
            Matricula(
                idMatricula=tupla[0],
                idCliente=tupla[1],
                idCurso=tupla[6],
                statusMatricula=tupla[8],
                desempenho=tupla[9],
                frequencia=tupla[10],
                dataMatricula=tupla[11],
                curso = obter_curso_por_id(tupla[6]),
                usuario = obter_usuario_por_id(tupla[1])
            ) for tupla in tuplas
        ]
        return matriculas
    except Exception as e:
        print(f"Erro ao obter matrículas por curso: {e}")
        return None

def obter_matriculas_por_cliente(id_cliente: int) -> list[Matricula]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MATRICULA_POR_CLIENTE, (id_cliente,))
        tuplas = cursor.fetchall()
        conn.close()
        matriculas = [
            Matricula(
                idMatricula=tupla[0],
                idCliente=tupla[1],
                idCurso=tupla[6],
                statusMatricula=tupla[8],
                desempenho=tupla[9],
                frequencia=tupla[10],
                dataMatricula=tupla[11],
                curso = obter_curso_por_id(tupla[6]),
                usuario = obter_usuario_por_id(tupla[1])
            ) for tupla in tuplas
        ]
        return matriculas
    except Exception as e:
        print(f"Erro ao obter matrículas por cliente: {e}")
        return None

def obter_quantidade_matriculas_por_curso(nome: str) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_MATRICULA_POR_CURSO, ('%' + nome + '%',))
        quantidade = cursor.fetchone()[0]
        conn.close()

        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de matrículas por curso: {e}")
        return 0
    
def obter_quantidade_matriculas_por_cliente(id_cliente: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_MATRICULA_POR_CLIENTE, (id_cliente,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de matrículas por cliente: {e}")
        return 0

def obter_quantidade_matriculas() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_MATRICULAS)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de matrículas: {e}")
        return 0

def atualizar_matricula(id: int, matricula: Matricula) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            ATUALIZAR_MATRICULA_POR_ID,
            (
                matricula.idCliente,
                matricula.idCurso,
                matricula.statusMatricula,
                matricula.desempenho,
                matricula.frequencia,
                matricula.dataMatricula,
                id
            )
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao atualizar matrícula: {e}")
        return False

def excluir_matricula(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_MATRICULA_POR_ID, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir matrícula: {e}")
        return False

    
#função extra porque eu preciso do id de matrícula que aqui retorna bool:

def inserir_matricula_pegar_id(matricula: Matricula) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            INSERIR_MATRICULA,
            (
            matricula.idCliente,
            matricula.idCurso,
            matricula.statusMatricula,
            matricula.desempenho,
            matricula.frequencia,
            matricula.dataMatricula
            )
        )
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir matrícula: {e}")
        return False
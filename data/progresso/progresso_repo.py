from data.aula.aula_repo import obter_aula_por_id
from data.matricula.matricula_repo import obter_matricula_por_id
from data.progresso.progresso_model import Progresso
from data.progresso.progresso_sql import *
from data.util import get_connection


def criar_tabela_progresso():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_PROGRESSO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar a tabela progresso: {e}")

from typing import Optional
from data.aula.aula_repo import obter_aula_por_id
from data.matricula.matricula_repo import obter_matricula_por_id
from data.progresso.progresso_model import Progresso
from data.progresso.progresso_sql import *
from data.util import get_connection


def criar_tabela_progresso() -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_PROGRESSO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar a tabela progresso: {e}")
        return False


def inserir_progresso(progresso: Progresso) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            INSERIR_PROGRESSO,
            (
                progresso.idAula,
                progresso.idMatricula,
                progresso.dataInicio,
                progresso.dataFim,
                progresso.statusAula,
                progresso.porcentagemConclusao
            )
        )
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir progresso: {e}")
        return None


def obter_todos_progresso() -> list[Progresso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROGRESSO)
        tuplas = cursor.fetchall()
        conn.close()
        progresso_list = [
            Progresso(
                id=tupla[0],
                idAula=tupla['idAula'],
                idMatricula=tupla['idMatricula'],
                dataInicio=tupla['dataInicio'],
                dataFim=tupla['dataFim'],
                statusAula=tupla['statusAula'],
                porcentagemConclusao=tupla['porcentagemConclusao'],
                aula=obter_aula_por_id(tupla['idAula']),
                matricula=obter_matricula_por_id(tupla['idMatricula'])
            ) for tupla in tuplas
        ]
        return progresso_list
    except Exception as e:
        print(f"Erro ao obter todos os progressos: {e}")


def obter_progresso_paginado(limite: int, offset: int) -> list[Progresso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROGRESSO_PAGINADO, (limite, offset))
        tuplas = cursor.fetchall()
        conn.close()
        progresso_list = [
            Progresso(
                id=tupla[0],
                idAula=tupla['idAula'],
                idMatricula=tupla['idMatricula'],
                dataInicio=tupla['dataInicio'],
                dataFim=tupla['dataFim'],
                statusAula=tupla['statusAula'],
                porcentagemConclusao=tupla['porcentagemConclusao'],
                aula=obter_aula_por_id(tupla['idAula']),
                matricula=obter_matricula_por_id(tupla['idMatricula'])
            ) for tupla in tuplas
        ]
        return progresso_list
    except Exception as e:
        print(f"Erro ao obter progresso paginado: {e}")


def obter_progresso_por_id(id: int) -> Optional[Progresso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROGRESSO_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Progresso(
                id=tupla[0],
                idAula=tupla['idAula'],
                idMatricula=tupla['idMatricula'],
                dataInicio=tupla['dataInicio'],
                dataFim=tupla['dataFim'],
                statusAula=tupla['statusAula'],
                porcentagemConclusao=tupla['porcentagemConclusao'],
                aula=obter_aula_por_id(tupla['idAula']),
                matricula=obter_matricula_por_id(tupla['idMatricula'])
            )
        return None
    except Exception as e:
        print(f"Erro ao obter progresso por id: {e}")
        return None


def obter_progresso_por_aula(id_aula: int, limite: int, offset: int) -> list[Progresso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROGRESSO_POR_AULA, (id_aula, limite, offset))
        tuplas = cursor.fetchall()
        conn.close()
        progresso_list = [
            Progresso(
                id=tupla[0],
                idAula=tupla['idAula'],
                idMatricula=tupla['idMatricula'],
                dataInicio=tupla['dataInicio'],
                dataFim=tupla['dataFim'],
                statusAula=tupla['statusAula'],
                porcentagemConclusao=tupla['porcentagemConclusao'],
                aula=obter_aula_por_id(tupla['idAula']),
                matricula=obter_matricula_por_id(tupla['idMatricula'])
            ) for tupla in tuplas
        ]
        return progresso_list
    except Exception as e:
        print(f"Erro ao obter progresso por aula: {e}")


def obter_progresso_por_matricula(id_matricula: int, limite: int, offset: int) -> list[Progresso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROGRESSO_POR_MATRICULA, (id_matricula, limite, offset))
        tuplas = cursor.fetchall()
        conn.close()
        progresso_list = [
            Progresso(
                id=tupla[0],
                idAula=tupla['idAula'],
                idMatricula=tupla['idMatricula'],
                dataInicio=tupla['dataInicio'],
                dataFim=tupla['dataFim'],
                statusAula=tupla['statusAula'],
                porcentagemConclusao=tupla['porcentagemConclusao'],
                aula=obter_aula_por_id(tupla['idAula']),
                matricula=obter_matricula_por_id(tupla['idMatricula'])
            ) for tupla in tuplas
        ]
        return progresso_list
    except Exception as e:
        print(f"Erro ao obter progresso por matrícula: {e}")


def obter_quantidade_progresso_por_aula(id_aula: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_PROGRESSO_POR_AULA, (id_aula,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de progresso por aula: {e}")
        return 0


def obter_quantidade_progresso_por_matricula(id_matricula: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_PROGRESSO_POR_MATRICULA, (id_matricula,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de progresso por matrícula: {e}")
        return 0


def obter_quantidade_progresso() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_PROGRESSO)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade total de progresso: {e}")
        return 0


def atualizar_progresso_por_id(id: int, progresso: Progresso) -> bool:
    try:
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
    except Exception as e:
        print(f"Erro ao atualizar progresso por id: {e}")
        return False


def atualizar_progresso_por_matricula_e_aula(id_matricula: int, id_aula: int, progresso: dict) -> bool:
    try:
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
    except Exception as e:
        print(f"Erro ao atualizar progresso por matrícula e aula: {e}")
        return False


def excluir_progresso_por_id(id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_PROGRESSO_POR_ID, (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao excluir progresso por id: {e}")
        return False


def excluir_progresso_por_matricula_e_aula(id_matricula: int, id_aula: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_PROGRESSO_POR_MATRICULA_E_AULA, (id_matricula, id_aula))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao excluir progresso por matrícula e aula: {e}")
        return False

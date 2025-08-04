import json
from typing import Optional
from data.professor.professor_model import Professor
from data.professor.professor_sql import *
from data.util import get_connection


def criar_tabela_professor() -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_PROFESSOR)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela professor: {e}")
        return False

def inserir_professor(professor: Professor, id: int) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursosPostados = json.dumps(professor.cursosPostados)
        cursor.execute(INSERIR_PROFESSOR, (
        cursosPostados,
        professor.quantidadeAlunos,
        professor.dataCriacaoProfessor,
        id))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir professor: {e}")
        return None

def obter_todos_professors() -> list[Professor]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROFESSOR)
        tuplas = cursor.fetchall()
        conn.close()
        professores = [
                Professor(
                id=tupla[0],
                nome=tupla[1],
                email=tupla[2],
                senha=tupla[3],
                telefone=tupla[4],
                dataCriacao=tupla[5],
                dataUltimoAcesso=tupla[6],
                statusConta=tupla[7],
                historicoCursos=tupla[8],
                indentificacaoProfessor=tupla[9], 
                cursosPostados=tupla[10],
                quantidadeAlunos=tupla[11],
                dataCriacaoProfessor=tupla[12]   
            ) for tupla in tuplas 
        ]
        conn.close()
        return professores
    except Exception as e:
        print(f"Erro ao obter todos os professores: {e}")
        return []


def obter_professor_por_email(email: str) -> Optional[Professor]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROFESSOR_POR_EMAIL, (email,))
        tupla = cursor.fetchone()
        conn.close()

        if tupla:
            historicoCursos = json.loads(tupla[8])
            cursosPostados = json.loads(tupla[10])

            return Professor(
                id=tupla[0],
                nome=tupla[1],
                email=tupla[2],
                senha=tupla[3],
                telefone=tupla[4],
                dataCriacao=tupla[5],
                dataUltimoAcesso=tupla[6],
                statusConta=tupla[7],
                historicoCursos=historicoCursos,
                indentificacaoProfessor=tupla[9],
                cursosPostados=cursosPostados,
                quantidadeAlunos=tupla[11],
                dataCriacaoProfessor=tupla[12]
            )
    except Exception as e:
        print(f"Erro ao obter professor por email: {e}")
        return None


def obter_professor_por_id(id: int) -> Optional[Professor]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROFESSOR_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla is None:
            return None

        historicoCursos = json.loads(tupla[8])
        cursosPostados = json.loads(tupla[10])

        return Professor(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5],
            dataUltimoAcesso=tupla[6],
            statusConta=tupla[7],
            historicoCursos=historicoCursos,
            indentificacaoProfessor=tupla[9],
            cursosPostados=cursosPostados,
            quantidadeAlunos=tupla[11],
            dataCriacaoProfessor=tupla[12]
        )
    except Exception as e:
        print(f"Erro ao obter professor por id: {e}")
        return None


def atualizar_professor_por_id(professor: Professor, id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Atualiza os dados do professor na tabela usuario
        cursor.execute("""
            UPDATE usuario
            SET nome = ?, email = ?, senha = ?, telefone = ?
            WHERE id = ?
        """, (
            professor.nome,
            professor.email,
            professor.senha,
            professor.telefone,
            id
        ))

        # Atualiza a tabela cliente
        cursor.execute("""
            UPDATE cliente
            SET dataUltimoAcesso = ?, statusConta = ?, historicoCursos = ?, indentificacaoProfessor = ?
            WHERE id = ?
        """, (
            professor.dataUltimoAcesso,
            professor.statusConta,
            professor.historicoCursos,
            professor.indentificacaoProfessor,
            id
        ))

        # Atualiza a tabela professor
        cursor.execute("""
            UPDATE professor
            SET cursosPostados = ?, quantidadeAlunos = ?, dataCriacaoProfessor = ?
            WHERE id = ?
        """, (
            professor.cursosPostados,
            professor.quantidadeAlunos,
            professor.dataCriacaoProfessor,
            id
        ))

        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao atualizar professor por id: {e}")


def atualizar_professor_por_email(professor: Professor, email: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM usuario WHERE email = ?", (email,))
        resultado = cursor.fetchone()
        if not resultado:
            return False
        id_usuario = resultado[0]

        cursor.execute("""
            UPDATE usuario
            SET nome = ?, email = ?, senha = ?, telefone = ?
            WHERE id = ?
        """, (
            professor.nome,
            professor.email,
            professor.senha,
            professor.telefone,
            id_usuario
        ))

        cursor.execute("""
            UPDATE cliente
            SET dataUltimoAcesso = ?, statusConta = ?, historicoCursos = ?, indentificacaoProfessor = ?
            WHERE id = ?
        """, (
            professor.dataUltimoAcesso,
            professor.statusConta,
            professor.historicoCursos,
            professor.indentificacaoProfessor,
            id_usuario
        ))

        cursor.execute("""
            UPDATE professor
            SET cursosPostados = ?, quantidadeAlunos = ?, dataCriacaoProfessor = ?
            WHERE id = ?
        """, (
            professor.cursosPostados,
            professor.quantidadeAlunos,
            professor.dataCriacaoProfessor,
            id_usuario
        ))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao atualizar professor por email: {e}")
        return False



def excluir_professor_por_id(id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_PROFESSOR_POR_ID, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir professor por id: {e}")
        return False

def excluir_professor_por_email(email: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_PROFESSOR_POR_EMAIL, (email,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir professor por email: {e}")
        return False

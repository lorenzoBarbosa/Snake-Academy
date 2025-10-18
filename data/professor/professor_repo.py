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
        professor.descricaoProfessor,
        id))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir professor: {e}")
        return None

def obter_todos_professores() -> list[Professor]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROFESSOR)
        tuplas = cursor.fetchall()
        conn.close()
        professores = []
        for tupla in tuplas:
            historicoCursos = json.loads(tupla["historicoCursos"])
            cursosPostados = json.loads(tupla["cursosPostados"])
            professor = Professor(
                id=tupla["id"],
                nome=tupla["nome"],
                email=tupla["email"],
                senha=tupla["senha"],
                telefone=tupla["telefone"],
                dataNascimento=tupla["dataNascimento"],
                perfil=tupla["perfil"],
                token_redefinicao=tupla["token_redefinicao"],
                data_token=tupla["data_token"],
                data_cadastro=tupla["data_cadastro"],
                foto=tupla["foto"],
                dataUltimoAcesso=tupla["dataUltimoAcesso"],
                statusConta=tupla["statusConta"],
                historicoCursos=historicoCursos,
                indentificacaoProfessor=tupla["indentificacaoProfessor"],
                cursosPostados=cursosPostados,
                quantidadeAlunos=tupla["quantidadeAlunos"],
                dataCriacaoProfessor=tupla["dataCriacaoProfessor"],
                descricaoProfessor=tupla["descricaoProfessor"]
            )
            professores.append(professor)
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
            historicoCursos = json.loads(tupla["historicoCursos"])
            cursosPostados = json.loads(tupla["cursosPostados"])

            return Professor(
                id=tupla["id"],
                nome=tupla["nome"],
                email=tupla["email"],
                senha=tupla["senha"],
                telefone=tupla["telefone"],
                dataNascimento=tupla["dataNascimento"],
                perfil=tupla["perfil"],
                token_redefinicao=tupla["token_redefinicao"],
                data_token=tupla["data_token"],
                data_cadastro=tupla["data_cadastro"],
                foto=tupla["foto"],
                dataUltimoAcesso=tupla["dataUltimoAcesso"],
                statusConta=tupla["statusConta"],
                historicoCursos=historicoCursos,
                indentificacaoProfessor=tupla["indentificacaoProfessor"],
                cursosPostados=cursosPostados,
                quantidadeAlunos=tupla["quantidadeAlunos"],
                dataCriacaoProfessor=tupla["dataCriacaoProfessor"],
                descricaoProfessor=tupla["descricaoProfessor"]
            )
    except Exception as e:
        print(f"Erro ao obter professor por email: {e}")
        return None
    
def obter_professor_por_termo_paginado(termo: str, pagina: int, tamanho_pagina: int) -> list[Professor]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        offset = (pagina - 1) * tamanho_pagina
        termo_like = f"%{termo}%"
        cursor.execute(OBTER_PROFESSOR_POR_TERMO_PAGINADO, (termo_like, tamanho_pagina, offset))
        tuplas = cursor.fetchall()
        professores = []
        for tupla in tuplas:
            historicoCursos = json.loads(tupla["historicoCursos"])
            cursosPostados = json.loads(tupla["cursosPostados"])
            professor = Professor(
                id=tupla["id"],
                nome=tupla["nome"],
                email=tupla["email"],
                senha=tupla["senha"],
                telefone=tupla["telefone"],
                dataNascimento=tupla["dataNascimento"],
                perfil=tupla["perfil"],
                token_redefinicao=tupla["token_redefinicao"],
                data_token=tupla["data_token"],
                data_cadastro=tupla["data_cadastro"],
                foto=tupla["foto"],
                dataUltimoAcesso=tupla["dataUltimoAcesso"],
                statusConta=tupla["statusConta"],
                historicoCursos=historicoCursos,
                indentificacaoProfessor=tupla["indentificacaoProfessor"],
                cursosPostados=cursosPostados,
                quantidadeAlunos=tupla["quantidadeAlunos"],
                dataCriacaoProfessor=tupla["dataCriacaoProfessor"],
                descricaoProfessor=tupla["descricaoProfessor"]
            )
            professores.append(professor)
        conn.close()
        return professores
    except Exception as e:
        print(f"Erro ao obter professores por termo paginado: {e}")
        return []


def obter_professor_por_id(id: int) -> Optional[Professor]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_PROFESSOR_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            historicoCursos = json.loads(tupla["historicoCursos"])
            cursosPostados = json.loads(tupla["cursosPostados"])

            return Professor(
                id=tupla["id"],
                nome=tupla["nome"],
                email=tupla["email"],
                senha=tupla["senha"],
                telefone=tupla["telefone"],
                dataNascimento=tupla["dataNascimento"],
                perfil=tupla["perfil"],
                token_redefinicao=tupla["token_redefinicao"],
                data_token=tupla["data_token"],
                data_cadastro=tupla["data_cadastro"],
                foto=tupla["foto"],
                dataUltimoAcesso=tupla["dataUltimoAcesso"],
                statusConta=tupla["statusConta"],
                historicoCursos=historicoCursos,
                indentificacaoProfessor=tupla["indentificacaoProfessor"],
                cursosPostados=cursosPostados,
                quantidadeAlunos=tupla["quantidadeAlunos"],
                dataCriacaoProfessor=tupla["dataCriacaoProfessor"],
                descricaoProfessor=tupla["descricaoProfessor"]
            )
    except Exception as e:
        print(f"Erro ao obter professor por email: {e}")
        return None


def atualizar_professor_por_id(professor: Professor, id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute( ATUALIZAR_PROFESSOR_POR_ID,(
            professor.cursosPostados,
            professor.quantidadeAlunos,
            professor.dataCriacaoProfessor,
            professor.descricaoProfessor,
            id
        ))
        conn.commit()
        conn.close()
        return (cursor.rowcount > 0)
    except Exception as e:
        print(f"Erro ao atualizar professor por id: {e}")


def atualizar_professor_por_email(professor: Professor, email: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute( ATUALIZAR_PROFESSOR_POR_ID,(
            professor.cursosPostados,
            professor.quantidadeAlunos,
            professor.dataCriacaoProfessor,
            professor.descricaoProfessor,
            email
        ))
        conn.commit()
        conn.close()
        return (cursor.rowcount > 0)
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

import json
from data.professor.professor_model import Professor
from data.professor.professor_sql import *
from data.util import get_connection


def criar_tabela_professor():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_PROFESSOR)
    conn.commit()
    conn.close()

def inserir_professor(professor: Professor, id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursosPostados = json.dumps(professor["cursosPostados"])
    cursor.execute(INSERIR_PROFESSOR, (
        cursosPostados,
        professor["quantidadeAlunos"],
        professor["dataCriacaoProfessor"],
        id))
    conn.commit()
    conn.close()

def obter_todos_professors() -> list[Professor]:
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
            ) for tupla in tuplas ]
    conn.close()
    return professores


def obter_professor_por_email(email: str) -> Professor:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_PROFESSOR_POR_EMAIL, (email,))
    tupla = cursor.fetchone()
    conn.close()
    
    if tupla:
        return Professor(*tupla)
    return None

def atualizar_professor_por_email(professor: Professor):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_PROFESSOR_POR_EMAIL, (
        professor.nome,
        professor.email,
        professor.senha,
        professor.telefone,
        professor.dataCriacao,
        professor.dataUltimoAcesso,
        professor.statusConta,
        professor.historicoCursos,
        professor.indentificacaoProfessor,
        professor.email))
    conn.commit()
    conn.close()

def excluir_professor_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_PROFESSOR_POR_EMAIL, (email,))
    conn.commit()
    conn.close()

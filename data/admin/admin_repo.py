from data.admin.admin_model import Admin
from data.admin.admin_sql import *
from data.util import get_connection


def criar_tabela_admin():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_ADMIN)
    conn.commit()
    conn.close()

def inserir_admin(admin: Admin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR_ADMIN, (
        admin.nome,
        admin.email,
        admin.senha,
        admin.telefone,
        admin.dataCriacao,
        admin.nivelAcesso))
    conn.commit()
    conn.close()

def obter_todos_admins() -> list[Admin]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_ADMINS)
    tuplas = cursor.fetchall()
    conn.close()
    usuarios = [
        Admin(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5],
            nivelAcesso=tupla[6]    
            ) for tupla in tuplas ]
    conn.close()
    return usuarios


def obter_admin_por_email(email: str) -> Admin:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_ADMIN_POR_EMAIL, (email,))
    tupla = cursor.fetchone()
    conn.close()
    
    if tupla:
        return Admin(*tupla)
    return None

def atualizar_admin_por_email(admin: Admin):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_ADMIN_POR_EMAIL, (
        admin.nome,
        admin.email,
        admin.senha,
        admin.telefone,
        admin.dataCriacao,
        admin.email))
    conn.commit()
    conn.close()

def excluir_admin_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_ADMIN_POR_EMAIL, (email,))
    conn.commit()
    conn.close()

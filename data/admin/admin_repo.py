import sqlite3
from typing import List, Optional
from data.admin.admin_model import Admin
from data.admin.admin_sql import *
from data.util import get_connection


def criar_tabela_admin():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_ADMIN)
    conn.commit()
    conn.close()

def inserir_admin(admin: Admin, id:int) -> Optional[int]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR_ADMIN, (
        admin["nivelAcesso"],
        id))
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

def atualizar_admin_por_email(admin: Admin, email:str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_ADMIN_POR_EMAIL, (
        admin["nivelAcesso"],
        email))
    conn.commit()
    conn.close()

def excluir_admin_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_ADMIN_POR_EMAIL, (email,))
    conn.commit()
    conn.close()

def obter_admin_paginado(pg_num: int, pg_size: int) -> List[Admin]:
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_ADMIN_PAGINADO, (limit, offset))
    tuplas = cursor.fetchall()
    admins = [
        Admin(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5],
            nivelAcesso=tupla[6]
        ) for tupla in tuplas]
    conn.close()
    return admins

def obter_admin_por_termo_paginado(termo: str, pg_num: int, pg_size: int) -> List[Admin]:
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    termo = f"%{termo}%"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_ADMIN_POR_TERMO_PAGINADO, (termo, termo, termo, limit, offset))
    tuplas = cursor.fetchall()
    admins = [
        Admin(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5],
            nivelAcesso=tupla[6]
        ) for tupla in tuplas]
    conn.close()
    return admins

def obter_quantidade_admins() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_ADMINS)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_admin_por_id(admin: Admin, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_ADMIN_POR_ID, (
        admin["nivelAcesso"],
        id))
    conn.commit()
    conn.close()

def excluir_admin_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_ADMIN_POR_ID, (id,))
    conn.commit()
    conn.close()

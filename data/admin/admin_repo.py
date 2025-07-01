import sqlite3
from typing import List, Optional
from data.admin.admin_model import Admin
from data.admin.admin_sql import *
from data.util import get_connection


def criar_tabela_admin() ->bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_ADMIN)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela admin: {e}")
        return False

def inserir_admin(admin: Admin, id:int) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(INSERIR_ADMIN, (
            admin.nivelAcesso,
            id))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir admin: {e}")
        
def obter_todos_admins() -> list[Admin]:
    try:
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
            ) for tupla in tuplas
        ]
        conn.close()
        return usuarios
    except Exception as e:
        print(f"Erro ao obter todos os admins: {e}")

def obter_admin_por_email(email: str) -> Admin:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_ADMIN_POR_EMAIL, (email,))
        tupla = cursor.fetchone()
        conn.close()
    
        if tupla:
            return Admin(*tupla)
        return None
    except Exception as e:
        print(f"Erro ao obter admim por email: {e}")
    
def obter_admin_por_id(id: int) -> Admin:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_ADMIN_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()

        if tupla:
            return Admin(*tupla)
        return None
    except Exception as e:
        print(f"Erro ao obter admin por id: {e}")

def atualizar_admin_por_email(admin: Admin, email:str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_ADMIN_POR_EMAIL, (
        admin.nivelAcesso,
        email))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao atualizar admin por email: {e}")

def excluir_admin_por_email(email: str) ->bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_ADMIN_POR_EMAIL, (email,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir admin por email: {e}")

def obter_admin_paginado(pg_num: int, pg_size: int) -> List[Admin]:
    try:
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
        ) for tupla in tuplas
        ]
        conn.close()
        return admins
    except Exception as e:
        print(f"Erro ao obter admins paginados: {e}")
        return []

def obter_admin_por_termo_paginado(termo: str, pg_num: int, pg_size: int) -> List[Admin]:
    try:
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
            ) for tupla in tuplas
            ]
        conn.close()
        return admins
    except Exception as e:
        print(f"Erro ao obter admins por termo paginados: {e}")

def obter_quantidade_admins() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_ADMINS)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de admins: {e}")

def atualizar_admin_por_id(admin: Admin, id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_ADMIN_POR_ID, (
        admin["nivelAcesso"],
        id))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao atualizar admin por id: {e}")

def excluir_admin_por_id(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_ADMIN_POR_ID, (id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao excluir admin por id: {e}")
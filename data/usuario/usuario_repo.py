from typing import Optional
from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import *
from data.util import get_connection


def criar_tabela_usuario() -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_USUARIO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")

def inserir_usuario(usuario: Usuario) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor() 
        cursor.execute(
            INSERIR_USUARIO,
            (
                usuario.nome,
                usuario.email,
                usuario.senha,
                usuario.telefone,
                usuario.dataNascimento,
                usuario.perfil
            )
        )
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def obter_todos_usuarios() -> list[Usuario]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIOS)
        tuplas = cursor.fetchall()
        usuarios = [
            Usuario(
                id=tupla[0],
                nome=tupla[1],
                email=tupla[2],
                senha=tupla[3],
                telefone=tupla[4],
                dataNascimento=tupla[5],
                perfil=tupla[6]
            ) for tupla in tuplas
        ]
        conn.close()
        return usuarios
    except Exception as e:
        print(f"Erro ao obter todos os usuários: {e}")

def obter_usuario_por_perfil(perfil: str) -> list[Usuario]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_PERFIL, (perfil,))
        tuplas = cursor.fetchall()
        usuarios = [
            Usuario(
                id=tupla[0],
                nome=tupla[1],
                email=tupla[2],
                senha=tupla[3],
                telefone=tupla[4],
                dataNascimento=tupla[5],
                perfil=tupla[6]
            ) for tupla in tuplas
        ]
        conn.close()
        return usuarios
    except Exception as e:
        print(f"Erro ao obter usuários por perfil: {e}")
        return []

def obter_usuario_por_email(email: str) -> Usuario:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_EMAIL, (email,))
        tupla = cursor.fetchone()
        conn.close()
        return Usuario(*tupla)
    except Exception as e:
        print(f"Erro ao obter usuário por email: {e}")

def obter_usuario_por_id(id: int) -> Usuario:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        return Usuario(*tupla)
    except Exception as e:
        print(f"Erro ao obter usuário por id: {e}")

def obter_usuario_paginado(pg_num: int, pg_size: int) -> list[Usuario]:
    try:
        limite = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_USUARIO_PAGINADO, (limite, offset))
        tuplas = cursor.fetchall()
        usuarios = [
            Usuario(
                id=tupla[0],
                nome=tupla[1],
                email=tupla[2],
                senha=tupla[3],
                telefone=tupla[4],
                dataNascimento=tupla[5],
                perfil=tupla[6]
            ) for tupla in tuplas
        ]
        conn.close()
        return usuarios
    except Exception as e:
        print(f"Erro ao obter usuários paginados: {e}")
        return []

def obter_quantidade_usuario() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_USUARIO)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de usuários: {e}")
    
def atualizar_usuario_por_id(usuario:Usuario) -> bool:
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(ATUALIZAR_USUARIO_POR_ID, (
                usuario.nome,
                usuario.email,
                usuario.senha,
                usuario.telefone,
                usuario.dataNascimento,
                usuario.perfil,
                usuario.id))
            conn.commit()
            conn.close()
            return (cursor.rowcount > 0)
        except Exception as e:
            print(f"Erro ao atualizar usuário por email: {e}")
            return False

def atualizar_usuario_por_email(usuario: Usuario) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_USUARIO_POR_EMAIL, (
            usuario.nome,
            usuario.email,
            usuario.senha,
            usuario.telefone,
            usuario.dataNascimento,
            usuario.perfil,
            usuario.email))
        conn.commit()
        conn.close()
        return (cursor.rowcount > 0)
    except Exception as e:
        print(f"Erro ao atualizar usuário por email: {e}")
        return False

def atualizar_senha(id: int, senha: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_SENHA, (senha, id))
        conn.commit()
        conn.close()
        return (cursor.rowcount > 0)
    except Exception as e:
        print(f"Erro ao atualizar senha: {e}")
        return False

def excluir_usuario_por_email(email: str) ->bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_USUARIO_POR_EMAIL, (email,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir usuário por email: {e}")

def excluir_usuario_por_id(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_USUARIO_POR_ID, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir usuário por id: {e}")


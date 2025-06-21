from data.usuario.usuario_model import Usuario
from data.usuario.usuario_sql import *
from data.util import get_connection


def criar_tabela_usuario():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_USUARIO)
    conn.commit()
    conn.close()

def inserir_usuario(usuario: Usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        INSERIR_USUARIO,
        (
            usuario["nome"],
            usuario["email"],
            usuario["senha"],
            usuario["telefone"],
            usuario["dataCriacao"]
        )
    )
    conn.commit()
    conn.close()

def obter_todos_usuarios() -> list[Usuario]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_USUARIOS)
    tuplas = cursor.fetchall()
    conn.close()
    usuarios = [
        Usuario(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5]    
            ) for tupla in tuplas ]
    conn.close()
    return usuarios


def obter_usuario_por_email(email: str) -> Usuario:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_USUARIO_POR_EMAIL, (email,))
    tupla = cursor.fetchone()
    conn.close()
    
    if tupla:
        return Usuario(*tupla)
    return None

def obter_usuario_por_id(id: int) -> Usuario:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_USUARIO_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    
    if tupla:
        return Usuario(*tupla)
    return None

def obter_usuario_paginado(pg_num: int, pg_size: int) -> list[Usuario]:
    limite = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_USUARIO_PAGINADO, (limite, offset))
    tuplas = cursor.fetchall()
    conn.close()
    usuarios = [
        Usuario(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5]    
            ) for tupla in tuplas ]
    return usuarios

def obter_quantidade_usuario() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_USUARIO)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_usuario_por_email(usuario: Usuario):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_USUARIO_POR_EMAIL, (
        usuario.nome,
        usuario.email,
        usuario.senha,
        usuario.telefone,
        usuario.dataCriacao,
        usuario.email))
    conn.commit()
    conn.close()

def excluir_usuario_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_USUARIO_POR_EMAIL, (email,))
    conn.commit()
    conn.close()

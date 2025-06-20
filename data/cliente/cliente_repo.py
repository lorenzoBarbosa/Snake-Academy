import json
import sqlite3
from typing import List, Optional
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from data.util import get_connection


def criar_tabela_cliente():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_CLIENTE)
    conn.commit()
    conn.close()

def inserir_cliente(cliente: Cliente, id:int):
    conn = get_connection()
    cursor = conn.cursor()
    historicoCursos = json.dumps(cliente["historicoCursos"])
    cursor.execute(INSERIR_CLIENTE, (
        cliente["dataUltimoAcesso"],
        cliente["statusConta"],
        historicoCursos,
        cliente["indentificacaoProfessor"],
        id))
    conn.commit()
    conn.close()

def obter_todos_clientes() -> list[Cliente]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CLIENTES)
    tuplas = cursor.fetchall()
    conn.close()
    clientes = [
        Cliente(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5],
            dataUltimoAcesso=tupla[6],
            statusConta=tupla[7],
            historicoCursos=tupla[8],
            indentificacaoProfessor=tupla[9]    
            ) for tupla in tuplas ]
    conn.close()
    return clientes


def obter_cliente_por_email(email: str) -> Cliente:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CLIENTE_POR_EMAIL, (email,))
    tupla = cursor.fetchone()
    conn.close()
    
    if tupla:
        return Cliente(*tupla)
    return None

def obter_cliente_paginado(pg_num: int, pg_size: int) -> List[Cliente]:
    limit = pg_size
    offset = (pg_num-1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CLIENTE_PAGINADO, (limit, offset))
    tuplas = cursor.fetchall()
    clientes= [
        Cliente(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5],
            dataUltimoAcesso=tupla[6],
            statusConta=tupla[7],
            historicoCursos=tupla[8],
            indentificacaoProfessor=tupla[9]
        ) for tupla in tuplas
    ]  
    conn.close()
    return clientes

def obter_cliente_por_id(id: int) -> Optional[Cliente]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CLIENTE_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    
    if tupla:
        return Cliente(*tupla)
    return None

def obter_cliente_por_termo_paginado(termo: str, pg_num: int, pg_size: int) -> List[Cliente]:
    limit = pg_size
    offset = (pg_num-1) * pg_size
    termo = f"%{termo}%"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_CLIENTE_POR_TERMO_PAGINADO, (termo, termo, termo, limit, offset))
    tuplas = cursor.fetchall()
    clientes= [
        Cliente(
            id=tupla[0],
            nome=tupla[1],
            email=tupla[2],
            senha=tupla[3],
            telefone=tupla[4],
            dataCriacao=tupla[5],
            dataUltimoAcesso=tupla[6],
            statusConta=tupla[7],
            historicoCursos=tupla[8],
            indentificacaoProfessor=tupla[9]
        ) for tupla in tuplas
    ]  
    conn.close()
    return clientes

def atualizar_cliente_por_email(email:str, cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_CLIENTE_POR_EMAIL, (
        cliente.dataUltimoAcesso,
        cliente.statusConta,
        cliente.historicoCursos,
        cliente.indentificacaoProfessor,
        email))
    conn.commit()
    conn.close()

def excluir_cliente_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_CLIENTE_POR_EMAIL, (email,))
    conn.commit()
    conn.close()

def obter_quantidade_clientes() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_CLIENTES)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_cliente_por_id(id: int, cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_CLIENTE_POR_ID, (
        cliente.dataUltimoAcesso,
        cliente.statusConta,
        cliente.historicoCursos,
        cliente.indentificacaoProfessor,
        id))
    conn.commit()
    conn.close()

def excluir_cliente_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_CLIENTE_POR_ID, (id,))
    conn.commit()
    conn.close()
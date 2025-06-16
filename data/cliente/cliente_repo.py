from data.cliente.cliente_model import Cliente
from data.cliente.cliente_sql import *
from data.util import get_connection


def criar_tabela_cliente():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_CLIENTE)
    conn.commit()
    conn.close()

def inserir_cliente(cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR_CLIENTE, (
        cliente.nome,
        cliente.email,
        cliente.senha,
        cliente.telefone,
        cliente.dataCriacao,
        cliente.dataUltimoAcesso,
        cliente.statusConta,
        cliente.historicoCursos,
        cliente.indentificacaoProfessor))
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

def atualizar_cliente_por_email(cliente: Cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_CLIENTE_POR_EMAIL, (
        cliente.nome,
        cliente.email,
        cliente.senha,
        cliente.telefone,
        cliente.dataCriacao,
        cliente.dataUltimoAcesso,
        cliente.statusConta,
        cliente.historicoCursos,
        cliente.indentificacaoProfessor,
        cliente.email))
    conn.commit()
    conn.close()

def excluir_cliente_por_email(email: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_CLIENTE_POR_EMAIL, (email,))
    conn.commit()
    conn.close()

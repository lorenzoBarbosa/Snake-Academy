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

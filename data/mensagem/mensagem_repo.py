from data.mensagem.mensagem_model import Mensagem
from data.mensagem.mensagem_sql import *
from data.util import get_connection


def criar_tabela_mensagem():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_MENSAGEM)
    conn.commit()
    conn.close()

def inserir_mensagem(mensagem: Mensagem):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(GERAR_MENSAGEM, (
        mensagem["idRemetente"],
        mensagem["idDestinatario"],
        mensagem["conteudo"],
        mensagem["dataEnvio"],
        mensagem["horaEnvio"],
        mensagem["visualizacao"]
    ))
    conn.commit()
    conn.close()

def obter_mensagens():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MENSAGENS)
    tuplas = cursor.fetchall()
    conn.close()
    mensagens = [ 
        Mensagem(
            id=tupla[0],
            idRmetente=tupla[1],
            nomeRemetente=tupla[2],
            idDestinatario=tupla[3],
            nomeDestinatario=tupla[4],
            conteudo=tupla[5],
            dataEnvio=tupla[6],
            horaEnvio=tupla[7],
            visualizacao=tupla[8]
        ) for tupla in tuplas
    ]
    return mensagens

def obter_mensagem_paginado(pg_num: int, pg_size: int):
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MENSAGEM_PAGINADO, (limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    mensagens = [
        Mensagem(
            id=tupla[0],
            idRmetente=tupla[1],
            nomeRemetente=tupla[2],
            idDestinatario=tupla[3],
            nomeDestinatario=tupla[4],
            conteudo=tupla[5],
            dataEnvio=tupla[6],
            horaEnvio=tupla[7],
            visualizacao=tupla[8]
        ) for tupla in tuplas
    ]
    return mensagens

def obter_mensagem_por_termo_paginado(termo: str, pg_num: int, pg_size: int):
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MENSAGEM_POR_TERMO_PAGINADO, (f"%{termo}%", f"%{termo}%", f"%{termo}%", limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    mensagens = [
        Mensagem(
            id=tupla[0],
            idRmetente=tupla[1],
            nomeRemetente=tupla[2],
            idDestinatario=tupla[3],
            nomeDestinatario=tupla[4],
            conteudo=tupla[5],
            dataEnvio=tupla[6],
            horaEnvio=tupla[7],
            visualizacao=tupla[8]
        ) for tupla in tuplas
    ]
    return mensagens

def obter_mensagem_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MENSAGEM_POR_ID, (id,))
    tupla = cursor.fetchone()
    conn.close()
    if tupla:
        mensagem = Mensagem(
            id=tupla[0],
            idRmetente=tupla[1],
            nomeRemetente=tupla[2],
            idDestinatario=tupla[3],
            nomeDestinatario=tupla[4],
            conteudo=tupla[5],
            dataEnvio=tupla[6],
            horaEnvio=tupla[7],
            visualizacao=tupla[8]
        )
        return mensagem
    return None

def obter_mensagem_por_nome_remetente(nome: str, pg_num: int, pg_size: int):
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MENSAGEM_POR_NOME_REMETENTE, (nome, limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    mensagens = [
        Mensagem(
            id=tupla[0],
            idRmetente=tupla[1],
            nomeRemetente=tupla[2],
            idDestinatario=tupla[3],
            nomeDestinatario=tupla[4],
            conteudo=tupla[5],
            dataEnvio=tupla[6],
            horaEnvio=tupla[7],
            visualizacao=tupla[8]
        ) for tupla in tuplas
    ]
    return mensagens

def obter_mensagem_por_nome_destinatario(nome: str, pg_num: int, pg_size: int):
    limit = pg_size
    offset = (pg_num - 1) * pg_size
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_MENSAGEM_POR_NOME_DESTINATARIO, (nome, limit, offset))
    tuplas = cursor.fetchall()
    conn.close()
    mensagens = [
        Mensagem(
            id=tupla[0],
            idRmetente=tupla[1],
            nomeRemetente=tupla[2],
            idDestinatario=tupla[3],
            nomeDestinatario=tupla[4],
            conteudo=tupla[5],
            dataEnvio=tupla[6],
            horaEnvio=tupla[7],
            visualizacao=tupla[8]
        ) for tupla in tuplas
    ]
    return mensagens

def obter_quantidade_mensagem():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_MENSAGEM)
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_mensagem_por_nome_remetente(nome: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_MENSAGEM_POR_NOME_REMETENTE, (nome,))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def obter_quantidade_mensagem_por_nome_destinatario(nome: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_QUANTIDADE_MENSAGEM_POR_NOME_DESTINATARIO, (nome,))
    quantidade = cursor.fetchone()[0]
    conn.close()
    return quantidade

def atualizar_mensagem(mensagem: Mensagem, id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_MENSAGEM, (
        mensagem["idRmetente"],
        mensagem["idDestinatario"],
        mensagem["conteudo"],
        mensagem["dataEnvio"],
        mensagem["horaEnvio"],
        mensagem["visualizacao"],
        id
    ))
    conn.commit()
    conn.close()

def atualizar_visualizacao_mensagem(visualizacao: bool, id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(ATUALIZAR_VISUALIZACAO_MENSAGEM, (visualizacao, id))
    conn.commit()
    conn.close()

def excluir_mensagem(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_MENSAGEM_POR_ID, (id))
    conn.commit()
    conn.close()

def excluir_mensagem_por_nome_remetente(nome: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_MENSAGEM_POR_NOME_REMETENTE, (nome,))
    conn.commit()
    conn.close()

def excluir_mensagem_por_nome_destinatario(nome: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_MENSAGEM_POR_NOME_DESTINATARIO, (nome,))
    conn.commit()
    conn.close()









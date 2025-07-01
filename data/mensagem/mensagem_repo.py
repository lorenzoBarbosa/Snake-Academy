from typing import Optional
from data.mensagem.mensagem_model import Mensagem
from data.mensagem.mensagem_sql import *
from data.usuario.usuario_repo import obter_usuario_por_id
from data.util import get_connection


def criar_tabela_mensagem() -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_MENSAGEM)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de mensagens: {e}")
        return False


def inserir_mensagem(mensagem: Mensagem) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(GERAR_MENSAGEM, (
            mensagem.idRmetente,
            mensagem.idDestinatario,
            mensagem.conteudo,
            mensagem.dataEnvio,
            mensagem.horaEnvio,
            mensagem.visualizacao
        ))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir mensagem: {e}")
        return None

def obter_mensagens() -> list[Mensagem]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGENS)
        tuplas = cursor.fetchall()
        conn.close()
        mensagens = [ 
            Mensagem(
                id=tupla["id"],
                idRmetente=tupla["idRemetente"],
                idDestinatario=tupla["idDestinatario"],
                conteudo=tupla["conteudo"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"],
                remetente=obter_usuario_por_id(tupla["idRemetente"]),
                destinatario=obter_usuario_por_id(tupla["idDestinatario"])
            ) for tupla in tuplas
        ]
        return mensagens
    except Exception as e:
        print(f"Erro ao obter mensagens: {e}")
        return None

def obter_mensagem_paginado(pg_num: int, pg_size: int) -> list[Mensagem]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_PAGINADO, (limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        mensagens = [
            Mensagem(
                id=tupla["id"],
                idRmetente=tupla["idRemetente"],
                idDestinatario=tupla["idDestinatario"],
                conteudo=tupla["conteudo"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"],
                remetente=obter_usuario_por_id(tupla["idRemetente"]),
                destinatario=obter_usuario_por_id(tupla["idDestinatario"])
            ) for tupla in tuplas
        ]
        return mensagens
    except Exception as e:
        print(f"Erro ao obter mensagens paginadas: {e}")
        return None

def obter_mensagem_por_termo_paginado(termo: str, pg_num: int, pg_size: int) -> list[Mensagem]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_POR_TERMO_PAGINADO, (f"%{termo}%", f"%{termo}%", f"%{termo}%", limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        mensagens = [
            Mensagem(
                id=tupla["id"],
                idRmetente=tupla["idRemetente"],
                idDestinatario=tupla["idDestinatario"],
                conteudo=tupla["conteudo"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"],
                remetente=obter_usuario_por_id(tupla["idRemetente"]),
                destinatario=obter_usuario_por_id(tupla["idDestinatario"])
            ) for tupla in tuplas
        ]
        return mensagens
    except Exception as e:
        print(f"Erro ao obter mensagens por termo paginadas: {e}")
        return None


def obter_mensagem_por_id(id: int) -> Optional[Mensagem]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            mensagem = Mensagem(
            id=tupla["id"],
            idRmetente=tupla["idRemetente"],
            idDestinatario=tupla["idDestinatario"],
            conteudo=tupla["conteudo"],
            dataEnvio=tupla["dataEnvio"],
            horaEnvio=tupla["horaEnvio"],
            visualizacao=tupla["visualizacao"],
            remetente= obter_usuario_por_id(tupla["idRemetente"]),
            destinatario= obter_usuario_por_id(tupla["idDestinatario"])
        )
        return mensagem
    except Exception as e:
        print(f"Erro ao obter mensagem por id: {e}")

def obter_mensagem_por_nome_remetente(nome: str, pg_num: int, pg_size: int) -> list[Mensagem]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_POR_NOME_REMETENTE, (nome, limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        mensagens = [
            Mensagem(
                id=tupla["id"],
                idRmetente=tupla["idRemetente"],
                idDestinatario=tupla["idDestinatario"],
                conteudo=tupla["conteudo"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"],
                remetente=obter_usuario_por_id(tupla["idRemetente"]),
                destinatario=obter_usuario_por_id(tupla["idDestinatario"])
            ) for tupla in tuplas
        ]
        return mensagens
    except Exception as e:
        print(f"Erro ao obter mensagens por nome do remetente: {e}")
        return None

def obter_mensagem_por_nome_destinatario(nome: str, pg_num: int, pg_size: int) -> list[Mensagem]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_POR_NOME_DESTINATARIO, (nome, limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        mensagens = [
            Mensagem(
                id=tupla["id"],
                idRmetente=tupla["idRemetente"],
                idDestinatario=tupla["idDestinatario"],
                conteudo=tupla["conteudo"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"],
                remetente=obter_usuario_por_id(tupla["idRemetente"]),
                destinatario=obter_usuario_por_id(tupla["idDestinatario"])
            ) for tupla in tuplas
        ]
        return mensagens
    except Exception as e:
        print(f"Erro ao obter mensagens por nome do destinatário: {e}")
        return None


def obter_quantidade_mensagem() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_MENSAGEM)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de mensagens: {e}")
        return 0

def obter_quantidade_mensagem_por_nome_remetente(nome: str) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_MENSAGEM_POR_NOME_REMETENTE, (nome,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de mensagens por nome do remetente: {e}")
        return 0

def obter_quantidade_mensagem_por_nome_destinatario(nome: str) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_MENSAGEM_POR_NOME_DESTINATARIO, (nome,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de mensagens por nome do destinatário: {e}")
        return 0

def atualizar_mensagem(mensagem: Mensagem, id) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_MENSAGEM, (
        mensagem.idRmetente,
        mensagem.idDestinatario,
        mensagem.conteudo,
        mensagem.dataEnvio,
        mensagem.horaEnvio,
        mensagem.visualizacao,
        id
    ))
        conn.commit()
        conn.close()
        return(cursor.rowcount > 0)
    except Exception as e:
        print(f"Erro ao atualizar mensagem: {e}")
        return False

def atualizar_visualizacao_mensagem(visualizacao: bool, id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_VISUALIZACAO_MENSAGEM, (visualizacao, id))
        conn.commit()
        conn.close()
        return(cursor.rowcount > 0)
    except Exception as e:
        print(f"Erro ao atualizar visualização da mensagem: {e}")
        return False

def excluir_mensagem(id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_MENSAGEM_POR_ID, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir mensagem: {e}")
        return False
    

def excluir_mensagem_por_nome_remetente(nome: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_MENSAGEM_POR_NOME_REMETENTE, (nome,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir mensagem por nome do remetente: {e}")
        return False

def excluir_mensagem_por_nome_destinatario(nome: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_MENSAGEM_POR_NOME_DESTINATARIO, (nome,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir mensagem por nome do destinatário: {e}")
        return False






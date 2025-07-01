from typing import List, Optional
from data.mensagem_comunidade.mensagem_comunidade_model import *
from data.mensagem_comunidade.mensagem_comunidade_sql import *
from data.util import get_connection


def criar_tabela_mensagem_comunidade() ->bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_MENSAGEM_COMUNIDADE)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"A tabela mensagem comunidade não foi criada {e}")
        return False

def inserir_mensagem_comunidade(mensagem_comunidade: MensagemComunidade) ->Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(GERAR_MENSAGEM_COMUNIDADE, (
            mensagem_comunidade.idMatricula,
            mensagem_comunidade.idComunidade,
            mensagem_comunidade.conteudo,
            mensagem_comunidade.dataEnvio,
            mensagem_comunidade.horaEnvio
        ))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Falhou a inserção de mensagem {e}")
        return None

def obter_mensagens_comunidade() -> list[MensagemComunidade]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGENS_COMUNIDADE)
        tuplas = cursor.fetchall()
        conn.close()
        mensagens_comunidade = [
            MensagemComunidade(
                id=tupla[0],
                idMatricula=tupla[1],
                nomeMatricula=tupla[2],
                idComunidade=tupla[3],
                nomeComunidade=tupla[4],
                conteudo=tupla[5],
                dataEnvio=tupla[6],
                horaEnvio=tupla[7]
            ) for tupla in tuplas
        ]
        return mensagens_comunidade
    except Exception as e:
        print(f"Erro em obter mensagem comunidade")
        return []

def obter_mensagem_comunidade_paginado(pg_num: int, pg_size: int) ->List[MensagemComunidade]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_COMUNIDADE_PAGINADO, (limit, offset))
        tuplas = cursor.fetchall()
        mensagens_comunidade = [
            MensagemComunidade(
                id=tupla[0],
                idMatricula=tupla[1],
                nomeMatricula=tupla[2],
                idComunidade=tupla[3],
                nomeComunidade=tupla[4],
                conteudo=tupla[5],
                dataEnvio=tupla[6],
                horaEnvio=tupla[7]
            ) for tupla in tuplas
        ]
        conn.close()
        return mensagens_comunidade
    except Exception as e:
        print(f"Erro ao obter mensagem comunidade por erro paginado {e}")
        return []

def obter_mensagem_comunidade_por_termo_paginado(termo: str, pg_num: int, pg_size: int) ->List[MensagemComunidade]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_COMUNIDADE_POR_TERMO_PAGINADO, (f"%{termo}%", f"%{termo}%", limit, offset))
        tuplas = cursor.fetchall()
        mensagens_comunidade = [
            MensagemComunidade(
                id=tupla[0],
                idMatricula=tupla[1],
                nomeMatricula=tupla[2],
                idComunidade=tupla[3],
                nomeComunidade=tupla[4],
                conteudo=tupla[5],
                dataEnvio=tupla[6],
                horaEnvio=tupla[7]
            ) for tupla in tuplas
        ]
        conn.close()
        return mensagens_comunidade
    except Exception as e:
        print(f"Erro ao obter mensagem por termo paginado {e}")

def obter_mensagem_comunidade_por_id(id: int) ->MensagemComunidade:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_COMUNIDADE_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            mensagem_comunidade = MensagemComunidade(
                id=tupla[0],
                idMatricula=tupla[1],
                nomeMatricula=tupla[2],
                idComunidade=tupla[3],
                nomeComunidade=tupla[4],
                conteudo=tupla[5],
                dataEnvio=tupla[6],
                horaEnvio=tupla[7]
            )
            return mensagem_comunidade
        return None
    except Exception as e:
        print(f"Erro ao obter mensagem comunidade por id {e}")

def obter_mensagem_comunidade_por_matricula(nome_matricula: str, pg_num: int, pg_size: int) ->MensagemComunidade:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_COMUNIDADE_POR_MATRICULA, (f"%{nome_matricula}%", limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        mensagens_comunidade = [
            MensagemComunidade(
                id=tupla[0],
                idMatricula=tupla[1],
                nomeMatricula=tupla[2],
                idComunidade=tupla[3],
                nomeComunidade=tupla[4],
                conteudo=tupla[5],
                dataEnvio=tupla[6],
                horaEnvio=tupla[7]
            ) for tupla in tuplas
        ]
        return mensagens_comunidade
    except Exception as e:
        print(f"Erro ao obter mensagem comunidade por matrícula {e}")


def obter_mensagem_comunidade_por_comunidade(nome_comunidade: str, pg_num: int, pg_size: int) ->MensagemComunidade:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_MENSAGEM_COMUNIDADE_POR_COMUNIDADE, (f"%{nome_comunidade}%", limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        mensagens_comunidade = [
            MensagemComunidade(
                id=tupla[0],
                idMatricula=tupla[1],
                nomeMatricula=tupla[2],
                idComunidade=tupla[3],
                nomeComunidade=tupla[4],
                conteudo=tupla[5],
                dataEnvio=tupla[6],
                horaEnvio=tupla[7]
            ) for tupla in tuplas
        ]
        return mensagens_comunidade
    except Exception as e:
        print(f"Erro ao obter mensagem comunidade por comunidade {e}")

def atualizar_mensagem_comunidade(mensagem_comunidade: MensagemComunidade, id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_MENSAGEM_COMUNIDADE, (
            mensagem_comunidade["conteudo"],
            mensagem_comunidade["dataEnvio"],
            mensagem_comunidade["horaEnvio"],
            id
        ))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao atualizar mensagem comunidade {e}")

def excluir_mensagem_comunidade(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_MENSAGEM_COMUNIDADE, (id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao excluir mensagem comunidade {e}")
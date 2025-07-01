from typing import Optional, List
from data.admin.admin_model import Admin
from data.chamado.chamado_model import Chamado
from data.resposta_chamado.resposta_chamado_model import respostaChamado
from data.resposta_chamado.resposta_chamado_sql import *
from data.util import get_connection


def criar_tabela_rchamado():
    try:     
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_RCHAMADO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar a tabela {e}")

def gerar_rchamado(rchamado: respostaChamado):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(GERAR_RCHAMADO, (
            rchamado.idAdmin,
            rchamado.idChamado,
            rchamado.descricao,
            rchamado.dataEnvio,
            rchamado.horaEnvio,
            rchamado.visualizacao))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao gerar resposta ao chamado: {e}")

def obter_todos_rchamados() -> list[respostaChamado]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_RCHAMADOS)
        tuplas = cursor.fetchall()
        conn.close()
        rchamados = [
            respostaChamado(
                id=tupla[0],
                idAdmin=tupla[1],
                idChamado=tupla[2],
                descricao=tupla[2],
                dataEnvio=tupla[3],
                horaEnvio=tupla[4],
                visualizacao=tupla[5]    
            ) for tupla in tuplas ]
        return rchamados
    except Exception as e:
        print(f"Erro ao obter todos os rchamados: {e}")
        return None

def obter_rchamado_por_id(id: int) -> Optional[respostaChamado]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_RCHAMADO_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return respostaChamado(
                id=tupla["id"],
                idAdmin=tupla["idAdmin"],
                idChamado=tupla["idChamado"],
                descricao=tupla["descricao"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"]
            )
    except Exception as e:
        print(f"Erro ao obter rchamado por ID: {e}")
    return None

def obter_rchamado_paginado(pg_num: int, pg_size: int) -> list[respostaChamado]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_RCHAMADO_PAGINADO, (limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        rchamados = [
            respostaChamado(
                id=tupla["id"],
                idAdmin=tupla["idAdmin"],
                idChamado=tupla["idChamado"],
                descricao=tupla["descricao"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"]
            ) for tupla in tuplas
        ]
        return rchamados
    except Exception as e:
        print(f"Erro ao obter rchamado paginado: {e}")
        return None

def obter_rchamado_por_termo_paginado(termo, pg_num, pg_size) -> List[respostaChamado]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        termo = f"%{termo}%"
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_RCHAMADO_POR_TERMO_PAGINADO,(termo, termo, termo, limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        rchamados = [
            respostaChamado(
                id=tupla["id"],
                idAdmin=tupla["idAdmin"],
                idChamado=tupla["idChamado"],
                descricao=tupla["descricao"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"]
            ) for tupla in tuplas
        ]
        return rchamados
    except Exception as e:
        print(f"Erro ao obter rchamado por termo paginado: {e}")
        return None

def obter_quantidade_rchamados() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_RCHAMADOS)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de rchamados: {e}")
        return None

def obter_quantidade_rchamados_por_nome_admin(nome: str) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_RCHAMADOS_POR_NOME_ADMIN,(nome,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade por nome do admin: {e}")
        return None

def obter_rchamado_por_nome_admin(nome: str, pg_num: int, pg_size:int) -> List[respostaChamado]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_RCHAMADO_POR_NOME_ADMIN, (nome, limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        rchamados = [
            respostaChamado(
                id=tupla["id"],
                idAdmin=tupla["idAdmin"],
                idChamado= tupla["idChamado"],
                descricao=tupla["descricao"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"]
            ) for tupla in tuplas
        ]
        return rchamados
    except Exception as e:
        print(f"Erro ao obter rchamado por nome do admin: {e}")
        return None

def obter_rchamado_por_id_chamado(id: int) -> List[respostaChamado]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_RCHAMADO_POR_ID_CHAMADO, (id,))
        tuplas = cursor.fetchall()
        conn.close()
        rchamados = [
            respostaChamado(
                id=tupla["id"],
                idAdmin=tupla["idAdmin"],
                idChamado = tupla["idChamado"],
                descricao=tupla["descricao"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"]
            ) for tupla in tuplas
        ]
        return rchamados
    except Exception as e:
        print(f"Erro ao obter rchamado por ID do chamado: {e}")
        return None

def excluir_rchamado_por_id(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_RCHAMADO_POR_ID, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir rchamado por id: {e}")
        return None
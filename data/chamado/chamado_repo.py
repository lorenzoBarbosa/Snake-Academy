from datetime import datetime
from typing import Optional
from data.chamado.chamado_model import Chamado
from data.chamado.chamado_sql import *
from data.usuario.usuario_model import Usuario
from data.util import get_connection


def criar_tabela_chamado()  ->bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CHAMADO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de chamados: {e}")
        return False

def gerar_chamado(chamado: Chamado) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = datetime.now().date()
        chamado.dataEnvio = data.strftime("%d-%m-%Y")
        hora = datetime.now().time()
        chamado.horaEnvio = hora.strftime("%H:%M:%S")
        cursor.execute(GERAR_CHAMADO, (
            chamado.idUsuario,
            chamado.descricao,
            chamado.dataEnvio,
            chamado.horaEnvio,
            chamado.visualizacao,
            chamado.tipo))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao gerar chamado: {e}")
        return None

def obter_todos_chamados() -> list[Chamado]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CHAMADOS)
        tuplas = cursor.fetchall()
        conn.close()
        chamados = [
            Chamado(
                id=tupla[0],
                idUsuario=tupla[1],
                descricao=tupla[2],
                dataEnvio=tupla[3],
                horaEnvio=tupla[4],
                visualizacao=tupla[5],
                tipo=tupla[6]
            ) for tupla in tuplas
        ]
        conn.close()
        return chamados
    except Exception as e:
        print(f"Erro ao obter todos os chamados: {e}")
        return []

def obter_chamado_por_id(id: int) -> Chamado:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CHAMADO_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Chamado(
                id=tupla["id"],
                idUsuario=tupla["idUsuario"],
                descricao=tupla["descricao"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=bool(tupla["visualizacao"]),
                tipo=tupla["tipo"]
            )
    except Exception as e:
        print(f"Erro ao obter chamado por id: {e}")

    return None

def obter_chamado_por_nome_usuario(nome: str) -> Optional[Chamado]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CHAMADO_POR_NOME_USUARIO, (nome,))
        tuplas = cursor.fetchall()
        conn.close()
        chamados = [Chamado(
                id=tupla["id"],
                idUsuario=Usuario.somente_id(id=tupla["idUsuario"]),
                descricao=tupla["descricao"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"],
                tipo=tupla["tipo"]
            ) for tupla in tuplas
        ]
        return chamados
    except Exception as e:
        print(f"Erro ao obter chamado por nome de usuário: {e}")
        return []

def obter_chamado_paginado(pg_num: int, pg_size: int) -> list[Chamado]:
    try:
        limit = pg_size
        offset = (pg_num-1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CHAMADO_PAGINADO, (limit, offset))
        tuplas = cursor.fetchall()
        chamados = [
            Chamado(
                id=tupla["id"],
                idUsuario=Usuario.somente_id(tupla["idUsuario"]),
                descricao=tupla["descricao"],
                dataEnvio=tupla["dataEnvio"],
                horaEnvio=tupla["horaEnvio"],
                visualizacao=tupla["visualizacao"],
                tipo=tupla["tipo"]
            ) for tupla in tuplas
    ]
        conn.close()
        return chamados
    except Exception as e:
        print(f"Erro ao obter chamados paginados: {e}")
        return []  

def obter_chamado_por_termo_paginado(termo, pg_num, pg_size):
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        termo = f"%{termo}%"
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CHAMADO_POR_TERMO_PAGINADO(termo, termo, termo, limit, offset))
        tuplas = cursor.fetchall()
        chamados = [
            Chamado(
                id=tupla["id"],
            idUsuario=Usuario.somente_id(id=tupla["idUsuario"]),
            descricao=tupla["descricao"],
            dataEnvio=tupla["dataEnvio"],
            horaEnvio=tupla["horaEnvio"],
            visualizacao=tupla["visualizacao"],
            tipo=tupla["tipo"]
        ) for tupla in tuplas
    ]
        conn.close()
        return chamados
    except Exception as e:
        print(f"Erro ao obter chamado por termo paginado: {e}")

def obter_quantidade_chamados() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_CHAMADOS)
        quantidade = int(cursor.fetchone()[0])
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de chamados: {e}")
        return 0

def obter_quantidade_chamados_por_nome_usuario(nome:str) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_CHAMADOS_POR_NOME_USUARIO(nome))
        quantidade = int(cursor.fetchone()[0])
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de chamados por nome de usuário: {e}")
        return 0

def excluir_chamado_por_id(id: int) ->bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CHAMADO_POR_ID, (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao excluir chamado por id: {e}")
        return False

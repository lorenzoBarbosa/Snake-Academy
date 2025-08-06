import sqlite3
from typing import List, Optional
from data.topico.topico_model import Topico
from data.categoria.categoria_model import Categoria
from data.topico.topico_sql import *
from data.util import get_connection

def criar_tabela_topico() -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_TOPICO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de tópicos: {e}")
        return False

def inserir_topico(topico: Topico) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(INSERIR_TOPICO, (topico.nome, topico.idCategoria))
        conn.commit()
        cursor.lastrowid
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir tópico: {e}")
        return None

def obter_topicos() -> List[Topico]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_TOPICOS)
        tuplas = cursor.fetchall()
        conn.close()
        topicos = [
            Topico(
                id=tupla[0],
                nome=tupla[1],
                idCategoria=tupla[2],
                categoria=Categoria(id=tupla[2], nome=tupla[3])
            ) for tupla in tuplas
        ]
        return topicos
    except Exception as e:
        print(f"Erro ao obter tópicos: {e}")
        return []

def obter_topicos_paginado(pg_num: int, pg_size: int) -> List[Topico]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_TOPICOS_PAGINADO, (limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        topicos = [
            Topico(
                id=tupla[0],
                nome=tupla[1],
                idCategoria=tupla[2],
                categoria=Categoria(id=tupla[2], nome=tupla[3])
            ) for tupla in tuplas
        ]
        return topicos
    except Exception as e:
        print(f"Erro ao obter tópicos paginados: {e}")
        return []

def obter_topico_por_id(id: int) -> Optional[Topico]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_TOPICO_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Topico(
                id=tupla[0],
                nome=tupla[1],
                idCategoria=tupla[2],
                categoria=Categoria(id=tupla[2], nome=tupla[3])
            )
    except Exception as e:
        print(f"Erro ao obter tópico por id: {e}")
        return None

def obter_topico_por_categoria_paginado(idCategoria: int, pg_num: int, pg_size: int) -> List[Topico]:
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_TOPICO_POR_CATEGORIA_PAGINADO, (idCategoria, limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        topicos = [
            Topico(
                id=tupla[0],
                nome=tupla[1],
                idCategoria=tupla[2],
                categoria=Categoria(id=tupla[2], nome=tupla[3])
            ) for tupla in tuplas
        ]
        return topicos
    except Exception as e:
        print(f"Erro ao obter tópicos por categoria paginado: {e}")
        return []

def obter_topico_por_nome(nome: str) -> Optional[Topico]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_TOPICO_POR_NOME, (nome,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Topico(
                id=tupla[0],
                nome=tupla[1],
                idCategoria=tupla[2],
                categoria=Categoria(id=tupla[2], nome=tupla[3])
            )
    except Exception as e:
        print(f"Erro ao obter tópico por nome: {e}")
        return None

def obter_quantidade_topicos() -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_TOPICOS)
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de tópicos: {e}")
        return 0

def obter_quantidade_topicos_por_categoria(idCategoria: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_TOPICOS_POR_CATEGORIA, (idCategoria,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de tópicos por categoria: {e}")
        return 0

def obter_quantidade_topicos_por_nome(nome: str) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_TOPICOS_POR_NOME, (nome,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de tópicos por nome: {e}")
        return 0

def obter_quantidade_topicos_por_id(id: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_TOPICOS_POR_ID, (id,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de tópicos por id: {e}")
        return 0

def atualizar_topico_por_id(id: int, nome: str, idCategoria: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_TOPICO_POR_ID, (nome, idCategoria, id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar tópico por id: {e}")
        return False

def excluir_topico_por_id(id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_TOPICO_POR_ID, (id,))
        conn.commit()
        sucesso = cursor.rowcount > 0
        conn.close()
        return sucesso
    except Exception as e:
        print(f"Erro ao excluir tópico por id: {e}")
        return False
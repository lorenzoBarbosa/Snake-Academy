import sqlite3
from typing import List, Optional
from data.categoria.categoria_model import Categoria
from data.categoria.categoria_sql import *
from data.util import get_connection

def criar_tabela_categoria() -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_CATEGORIA)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de categorias: {e}")
        return False

def inserir_categoria(categoria: Categoria) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(INSERIR_CATEGORIA, (categoria.nome,))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir categoria: {e}")
        return None

def obter_categorias() -> List[Categoria]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CATEGORIA)
        tuplas = cursor.fetchall()
        conn.close()
        categorias = [Categoria(id=tupla[0], nome=tupla[1]) for tupla in tuplas]
        return categorias
    except Exception as e:
        print(f"Erro ao obter categorias: {e}")
        return []

def obter_categoria_por_id(id: int) -> Optional[Categoria]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CATEGORIA_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Categoria(id=tupla[0], nome=tupla[1])
    except Exception as e:
        print(f"Erro ao obter categoria por id: {e}")
        return None

def obter_categorias_paginado(pg_num: int, pg_size: int) -> List[Categoria]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        offset = (pg_num - 1) * pg_size
        limit = pg_size
        cursor.execute(OBTER_CATEGORIAS_PAGINADO, (limit, offset))
        tuplas = cursor.fetchall()
        conn.close()
        categorias = [Categoria(id=tupla[0], nome=tupla[1]) for tupla in tuplas]
        return categorias
    except Exception as e:
        print(f"Erro ao obter categorias paginado: {e}")
        return None

def obter_categoria_por_nome(nome: str) -> Optional[Categoria]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_CATEGORIA_POR_NOME, (nome,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return Categoria(id=tupla[0], nome=tupla[1])
    except Exception as e:
        print(f"Erro ao obter categoria por nome: {e}")
        return None

def obter_quantidade_categoria_por_id(id: int) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_CATEGORIA_POR_ID, (id,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de categoria por id: {e}")
        return 0

def obter_quantidade_categoria_por_nome(nome: str) -> int:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_QUANTIDADE_CATEGORIA_POR_NOME, (nome,))
        quantidade = cursor.fetchone()[0]
        conn.close()
        return quantidade
    except Exception as e:
        print(f"Erro ao obter quantidade de categoria por nome: {e}")
        return 0

def atualizar_categoria_por_id(id: int, nome: str) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_CATEGORIA_POR_ID, (nome, id))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao atualizar categoria por id: {e}")
        return False

def excluir_categoria_por_id(id: int) -> bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_CATEGORIA_POR_ID, (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao excluir categoria por id: {e}")
        return False
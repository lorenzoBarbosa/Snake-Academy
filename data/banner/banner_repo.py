from data.banner.banner_model import Banner
from data.banner.banner_sql import *
from data.util import get_connection


def criar_tabela_banner():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_BANNER)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

def inserir_banner(banner: Banner):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(INSERIR_BANNER, (banner.idAdmin, banner.status))
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao inserir banner: {e}")

def obter_todos_banners():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_TODOS_BANNERS)
        banners = cursor.fetchall()
        conn.close()
        return [Banner(*row) for row in banners]
    except Exception as e:
        print(f"Erro ao obter todos os banners: {e}")
        return None

def obter_banner_por_id(id: int) -> Banner:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_BANNER_POR_ID, (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Banner(*row)
        return None
    except Exception as e:
        print(f"Erro ao obter banner por ID: {e}")
        return None

def obter_banner_paginado(pg_num: int, pg_size: int):
    try:
        limit = pg_size
        offset = (pg_num - 1) * pg_size
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OOBTER_BANNER_PAGINADO, (limit, offset))
        banners = cursor.fetchall()
        conn.close()
        return [Banner(*row) for row in banners]
    except Exception as e:
        print(f"Erro ao obter banners paginados: {e}")
        return None

def atualizar_banner(banner: Banner):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(ATUALIZAR_BANNER, (banner.idAdmin, banner.status, banner.id))
        conn.commit()
        conn.close()
        return obter_banner_por_id(banner.id)
    except Exception as e:
        print(f"Erro ao atualizar banner: {e}")
        return None

def deletar_banner(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(DELETAR_BANNER, (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Erro ao deletar banner: {e}")
        return None


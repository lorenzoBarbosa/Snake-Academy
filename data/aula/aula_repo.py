from data.aula.aula_sql import *
from data.util import get_connection


def criar_tabela_aula():
    conn= get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_AULA)
    conn.commit()
    conn.close()

def inserir_aula(aula):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        INSERIR_AULA,
        (
            aula["idModulo"],
            aula["titulo"],
            aula["descricaoAula"],
            aula["duracaoAula"],
            aula["tipo"],
            aula["ordem"],
            aula["dataDisponibilidade"]
        )
    )
    conn.commit()
    conn.close()    

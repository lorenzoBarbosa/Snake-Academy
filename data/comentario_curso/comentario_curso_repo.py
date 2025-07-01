from typing import Optional
from data.comentario_curso.comentario_curso_model import comentarioCurso
from data.comentario_curso.comentario_curso_sql import *
from data.util import get_connection


def criar_tabela_comentario_curso() ->bool:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(CRIAR_TABELA_COMENTARIO_CURSO)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao criar tabela de comentários de curso: {e}")
        return False

def gerar_comentario_curso(comentario: comentarioCurso) -> Optional[int]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(GERAR_COMENTARIO_CURSO, (
            comentario.idAdmin,
            comentario.idMatricula,
            comentario.conteudo,
            comentario.dataEnvio,
            comentario.dataSupervisaoAdmin)
        )
        conn.commit()
        conn.close()
        return cursor.lastrowid
    except Exception as e:
        print(f"Erro ao gerar comentário de curso: {e}")

def obter_comentario_curso() -> list[comentarioCurso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMENTARIO_CURSO)
        tuplas = cursor.fetchall()
        conn.close()
        comentarios = [
        comentarioCurso(
            id=tupla[0],
            idAdmin=tupla[1],
            nomeAdmin=tupla[2],
            idMatricula=tupla[3],
            nomeMatricula=tupla[4],
            conteudo=tupla[5],
            dataEnvio=tupla[6],
            dataSupervisaoAdmin=tupla[7]
        ) for tupla in tuplas]
        return comentarios
    except Exception as e:
        print(f"Erro ao obter comentário de curso: {e}")
        return []

def obter_comentario_curso_por_id(id: int) -> comentarioCurso:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMENTARIO_CURSO_POR_ID, (id,))
        tupla = cursor.fetchone()
        conn.close()
        if tupla:
            return comentarioCurso(
            id=tupla[0],
            idAdmin=tupla[1],
            nomeAdmin=tupla[2],
            idMatricula=tupla[3],
            nomeMatricula=tupla[4],
            conteudo=tupla[5],
            dataEnvio=tupla[6],
            dataSupervisaoAdmin=tupla[7]
        )
    except Exception as e:
        print(f"Erro ao obter comentário de curso por id: {e}")

def obter_comentario_curso_por_nome_admin(nome: str, limite: int, offset: int) -> list[comentarioCurso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMENTARIO_CURSO_POR_NOME_ADMIN, (nome, limite, offset))
        tuplas = cursor.fetchall()
        conn.close()
        comentarios = [
            comentarioCurso(
                id=tupla[0],
                idAdmin=tupla[1],
                nomeAdmin=tupla[2],
                idMatricula=tupla[3],
                nomeMatricula=tupla[4],
                conteudo=tupla[5],
                dataEnvio=tupla[6],
                dataSupervisaoAdmin=tupla[7]
            ) for tupla in tuplas
        ]
        return comentarios
    except Exception as e:
        print(f"Erro ao obter comentário de curso por nome admin: {e}")
        return []

def excluir_comentario_curso_por_id(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(EXCLUIR_COMENTARIO_CURSO_POR_ID, (id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao excluir comentário de curso por id{e}")

def obter_comentario_curso_por_id_chamado(id_chamado: int, limite: int, offset: int) -> list[comentarioCurso]:
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMENTARIO_CURSO_POR_ID_CHAMADO, (id_chamado, limite, offset))
        tuplas = cursor.fetchall()
        conn.close()
        comentarios = [
            comentarioCurso(
                id=tupla[0],
                idAdmin=tupla[1],
                idMatricula=tupla[2],
                conteudo=tupla[3],
                dataEnvio=tupla[4],
                dataSupervisaoAdmin=tupla[5],
                nomeAdmin=tupla[6]
            ) for tupla in tuplas
            ]
        return comentarios
    except Exception as e:
        print(f"Erro ao obter comentário de curso por id chamado: {e}")

def obter_comentario_curso_paginado(limite: int, offset: int) -> list[comentarioCurso]:
    try:    
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(OBTER_COMENTARIO_CURSO_PAGINADO, (limite, offset))
        tuplas = cursor.fetchall()
        conn.close()
        comentarios = [
            comentarioCurso(
                id=tupla[0],
                idAdmin=tupla[1],
                idMatricula=tupla[2],
                conteudo=tupla[3],
                dataEnvio=tupla[4],
                dataSupervisaoAdmin=tupla[5],
                nomeAdmin=tupla[6]
            ) for tupla in tuplas
            ]
        return comentarios
    except Exception as e:
        print(f"Erro ao obter comentário de curso paginado: {e}")
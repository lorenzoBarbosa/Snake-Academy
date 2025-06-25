from data.comentario_curso.comentario_curso_model import comentarioCurso
from data.comentario_curso.comentario_curso_sql import *
from data.util import get_connection


def criar_tabela_comentario_curso():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA_COMENTARIO_CURSO)
    conn.commit()
    conn.close()

def gerar_comentario_curso(comentario: comentarioCurso):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(GERAR_COMENTARIO_CURSO, (
        comentario["idAdmin"],
        comentario["idMatricula"],
        comentario["conteudo"],
        comentario["dataEnvio"],
        comentario["dataSupervisaoAdmin"]))
    conn.commit()
    conn.close()

def obter_comentario_curso() -> list[comentarioCurso]:
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

def obter_comentario_curso_por_id(id: int) -> comentarioCurso:
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
    return None

def obter_comentario_curso_por_nome_admin(nome: str, limite: int, offset: int) -> list[comentarioCurso]:
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
        ) for tupla in tuplas]
    return comentarios

def excluir_comentario_curso_por_id(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(EXCLUIR_COMENTARIO_CURSO_POR_ID, (id,))
    conn.commit()
    conn.close()

def obter_comentario_curso_por_id_chamado(id_chamado: int, limite: int, offset: int) -> list[comentarioCurso]:
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
        ) for tupla in tuplas]
    return comentarios

def obter_comentario_curso_paginado(limite: int, offset: int) -> list[comentarioCurso]:
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
        ) for tupla in tuplas]
    return comentarios
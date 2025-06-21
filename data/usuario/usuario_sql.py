CRIAR_TABELA_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL,
    dataCriacao TEXT NOT NULL
)
"""
INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, telefone, dataCriacao)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_USUARIOS = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao
FROM usuario
ORDER BY id 
"""

OBTER_USUARIO_POR_EMAIL = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao
FROM usuario
WHERE email = ?
"""

OBTER_USUARIO_POR_ID = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao
FROM usuario
WHERE id = ?
"""

OBTER_USUARIO_PAGINADO = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao
    FROM usuario
    ORDER BY id
    LIMIT ? OFFSET ?"""

OBTER_QUANTIDADE_USUARIO= """
SELECT COUNT(*) FROM usuario
"""

ATUALIZAR_USUARIO_POR_EMAIL= """
UPDATE usuario
SET 
    nome = ?, 
    email = ?, 
    senha = ?, 
    telefone = ?, 
    dataCriacao = ?
WHERE email = ?
"""

EXCLUIR_USUARIO_POR_EMAIL = """
DELETE FROM usuario
WHERE email = ?
"""

EXCLUIR_USUARIO_POR_ID = """
DELETE FROM usuario
WHERE id = ?
"""



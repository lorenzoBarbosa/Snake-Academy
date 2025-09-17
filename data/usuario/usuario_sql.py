CRIAR_TABELA_USUARIO = """
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL,
    dataNascimento TEXT NOT NULL,
    perfil TEXT NOT NULL DEFAULT 'usuario',
    token_redefinicao TEXT,
    data_token TIMESTAMP,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    foto TEXT
)
"""
INSERIR_USUARIO = """
INSERT INTO usuario (nome, email, senha, telefone, dataNascimento, perfil)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_USUARIOS = """
SELECT 
    id, nome, email, senha, telefone, dataNascimento, perfil, token_redefinicao, data_token, data_cadastro, foto
FROM usuario
ORDER BY id 
"""

OBTER_USUARIO_POR_PERFIL= """
SELECT 
    id, nome, email, senha, telefone, dataNascimento, perfil, token_redefinicao, data_token, data_cadastro, foto
FROM usuario
WHERE perfil LIKE ?
"""

OBTER_USUARIO_POR_EMAIL = """
SELECT 
    id, nome, email, senha, telefone, dataNascimento, perfil, token_redefinicao, data_token, data_cadastro, foto
FROM usuario
WHERE email = ?
"""

OBTER_USUARIO_POR_ID = """
SELECT 
    id, nome, email, senha, telefone, dataNascimento, perfil, token_redefinicao, data_token, data_cadastro, foto
FROM usuario
WHERE id = ?
"""

OBTER_USUARIO_PAGINADO = """
SELECT 
    id, nome, email, senha, telefone, dataNascimento, perfil, token_redefinicao, data_token, data_cadastro, foto
    FROM usuario
    ORDER BY id
    LIMIT ? OFFSET ?"""

OBTER_QUANTIDADE_USUARIO= """
SELECT COUNT(*) FROM usuario
"""

ATUALIZAR_USUARIO_POR_ID ="""
UPDATE usuario
SET 
    nome = ?, 
    email = ?,  
    telefone = ?, 
    dataNascimento = ?, 
    perfil = ?
WHERE id = ?
"""

ATUALIZAR_USUARIO_POR_EMAIL= """
UPDATE usuario
SET 
    nome = ?, 
    email = ?,  
    telefone = ?, 
    dataNascimento = ?, 
    perfil = ?
WHERE email = ?
"""

ATUALIZAR_SENHA= """ 
UPDATE usuario
SET 
    senha = ?
WHERE id = ?
"""

ATUALIZAR_PERFIL= """
UPDATE usuario
SET 
    perfil = ?
WHERE id = ?
"""

EXCLUIR_USUARIO_POR_EMAIL = """
DELETE FROM usuario
WHERE email = ?
"""

EXCLUIR_USUARIO_POR_ID = """
DELETE FROM usuario
WHERE id = ?
"""

ADICIONAR_COLUNA_FOTO = """
ALTER TABLE usuario
ADD COLUMN foto TEXT
"""


ATUALIZAR_FOTO = """
UPDATE usuario SET foto = ? WHERE id = ?
"""

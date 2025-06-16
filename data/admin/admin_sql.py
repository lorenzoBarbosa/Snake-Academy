CRIAR_TABELA_ADMIN = """
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL,
    dataCriacao TEXT NOT NULL,
    nivelAcesso INTEGER NOT NULL
)
"""
INSERIR_ADMIN = """
INSERT INTO admin (nome, email, senha, telefone, dataCriacao, nivelAcesso)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_ADMINS = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, nivelAcesso
FROM admin
ORDER BY id 
"""

OBTER_ADMIN_POR_EMAIL = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor
FROM admin
WHERE email = ?
"""

ATUALIZAR_ADMIN_POR_EMAIL= """
UPDATE admin
SET 
    nome = ?, 
    email = ?, 
    senha = ?, 
    telefone = ?, 
    dataCriacao = ?,
    nivelAcesso = ?
WHERE email = ?
"""

EXCLUIR_ADMIN_POR_EMAIL = """
DELETE FROM admin
WHERE email = ?
"""



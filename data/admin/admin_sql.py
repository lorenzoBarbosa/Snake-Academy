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

OBTER_QUANTIDADE_ADMINS = """
SELECT COUNT(*) AS quantidade
FROM admin
""" 

OBTER_ADMIN_PAGINADO = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, nivelAcesso
FROM admin
ORDER BY id
LIMIT ? OFFSET ?
""" #LIMIT determina quantos registros serão retornados, OFFSET determina a partir de qual registro começar a retornar
    #Caso o LIMIT seja 10 e o OFFSET seja 0, os primeiros 10 registros serão retornados.
    # Caso o LIMIT seja 10 e o OFFSET seja 10, os próximos 10 registros serão retornados. 

OBTER_ADMIN_POR_ID = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, nivelAcesso
FROM admin
WHERE id = ?
"""

ATUALIZAR_ADMIN_POR_ID = """
UPDATE admin
SET 
    nome = ?, 
    email = ?, 
    senha = ?, 
    telefone = ?, 
    dataCriacao = ?,
    nivelAcesso = ?
WHERE id = ?
"""

EXCLUIR_ADMIN_POR_ID = """
DELETE FROM admin
WHERE id = ?
"""

OBTER_ADMIN_POR_TERMO_PAGINADO = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, nivelAcesso
FROM admin
WHERE (nome LIKE ? OR email LIKE ? OR nivelAcesso LIKE ? OR id LIKE ?)
ORDER BY id
LIMIT ? OFFSET ?
"""







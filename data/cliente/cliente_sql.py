CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL,
    dataCriacao TEXT NOT NULL,
    dataUltimoAcesso TEXT NOT NULL,
    statusConta BOOLEAN NOT NULL,
    historicoCursos TEXT NOT NULL,
    indentificacaoProfessor BOOLEAN NOT NULL
)
"""
INSERIR_CLIENTE = """
INSERT INTO cliente (nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_CLIENTES = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor
FROM cliente
ORDER BY id 
"""

OBTER_CLIENTE_POR_EMAIL = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor
FROM cliente
WHERE email = ?
"""

ATUALIZAR_CLIENTE_POR_EMAIL= """
UPDATE cliente
SET 
    nome = ?, 
    email = ?, 
    senha = ?, 
    telefone = ?, 
    dataCriacao = ?,
    dataUltimoAcesso = ?, 
    statusConta = ?, 
    historicoCursos = ?, 
    indentificacaoProfessor = ?
WHERE email = ?
"""

EXCLUIR_CLIENTE_POR_EMAIL = """
DELETE FROM cliente
WHERE email = ?
"""

OBTER_QUANTIDADE_CLIENTES = """
SELECT COUNT(*) AS quantidade
FROM cliente
"""

OBTER_CLIENTE_PAGINADO = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor
FROM cliente
ORDER BY id
LIMIT ? OFFSET ?
"""  # LIMIT determina quantos registros serão retornados, OFFSET determina a partir de qual registro começar a retornar
# Caso o LIMIT seja 10 e o OFFSET seja 0, os primeiros 10 registros serão retornados.
# Caso o LIMIT seja 10 e o OFFSET seja 10, os próximos 10 registros serão retornados.

OBTER_CLIENTE_POR_ID = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor
FROM cliente
WHERE id = ?
"""

ATUALIZAR_CLIENTE_POR_ID = """
UPDATE cliente
SET 
    nome = ?, 
    email = ?, 
    senha = ?, 
    telefone = ?, 
    dataCriacao = ?,
    dataUltimoAcesso = ?, 
    statusConta = ?, 
    historicoCursos = ?, 
    indentificacaoProfessor = ?
WHERE id = ?
"""

EXCLUIR_CLIENTE_POR_ID = """
DELETE FROM cliente
WHERE id = ?
"""

OBTER_CLIENTE_POR_TERMO_PAGINADO = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor
FROM cliente
WHERE (nome LIKE ? OR email LIKE ? OR statusConta LIKE ?)
ORDER BY id
LIMIT ? OFFSET ?
"""
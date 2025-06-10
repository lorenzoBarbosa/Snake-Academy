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



CRIAR_TABELA_CLIENTE = """
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY,
    dataUltimoAcesso TEXT,
    statusConta BOOLEAN NOT NULL,
    historicoCursos TEXT NOT NULL,
    indentificacaoProfessor BOOLEAN NOT NULL,
    FOREIGN KEY (id) REFERENCES usuario(id)
)
"""
INSERIR_CLIENTE = """
INSERT INTO cliente (id, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor)
SELECT u.id, ?, ?, ?, ?
FROM usuario u
WHERE u.id = ?
"""

OBTER_CLIENTES = """
SELECT 
    u.id as id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.perfil as perfil, c.dataUltimoAcesso, c.statusConta, c.historicoCursos, c.indentificacaoProfessor
FROM cliente c
JOIN usuario u ON c.id = u.id
ORDER BY id 
"""
 
OBTER_CLIENTE_POR_EMAIL = """
SELECT 
    c.id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.perfil as perfil, c.dataUltimoAcesso, c.statusConta, c.historicoCursos, c.indentificacaoProfessor
FROM cliente c
JOIN usuario u ON c.id = u.id
WHERE u.email = ?
"""

OBTER_CLIENTE_PAGINADO = """
SELECT 
    c.id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.perfil as perfil, c.dataUltimoAcesso, c.statusConta, c.historicoCursos, c.indentificacaoProfessor
FROM cliente c
JOIN usuario u ON c.id = u.id
ORDER BY c.id
LIMIT ? OFFSET ?
"""
# LIMIT determina quantos registros serão retornados, OFFSET determina a partir de qual registro começar a retornar
# Caso o LIMIT seja 10 e o OFFSET seja 0, os primeiros 10 registros serão retornados.
# Caso o LIMIT seja 10 e o OFFSET seja 10, os próximos 10 registros serão retornados.

OBTER_CLIENTE_POR_ID = """
SELECT 
    c.id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.dataNascimento as dataNascimento, u.perfil as perfil, u.token_redefinicao as token_redefinicao, u.data_token as data_token, u.data_cadastro as data_cadastro, c.dataUltimoAcesso, c.statusConta, c.historicoCursos, c.indentificacaoProfessor
FROM cliente c
JOIN usuario u ON c.id = u.id
WHERE c.id = ?
"""

OBTER_CLIENTE_POR_TERMO_PAGINADO = """
SELECT 
    c.id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.dataNascimento as dataNascimento, u.perfil as perfil, c.dataUltimoAcesso, c.statusConta, c.historicoCursos, c.indentificacaoProfessor
FROM cliente c
JOIN usuario u ON c.id = u.id
WHERE (u.nome LIKE ? OR u.email LIKE ? OR c.statusConta LIKE ?)
ORDER BY c.id
LIMIT ? OFFSET ?
"""

ATUALIZAR_CLIENTE_POR_EMAIL = """
UPDATE cliente
SET 
    dataUltimoAcesso = ?, 
    statusConta = ?, 
    historicoCursos = ?, 
    indentificacaoProfessor = ?
WHERE id = (SELECT id FROM usuario WHERE email = ?)
"""

EXCLUIR_CLIENTE_POR_EMAIL = """
DELETE FROM cliente
WHERE id = (SELECT id FROM usuario WHERE email = ?)
"""

OBTER_QUANTIDADE_CLIENTES = """
SELECT COUNT(*) AS quantidade
FROM cliente
""" 


ATUALIZAR_CLIENTE_POR_ID = """
UPDATE cliente
SET 
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
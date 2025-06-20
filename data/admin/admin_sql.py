CRIAR_TABELA_ADMIN = """
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY,
    nivelAcesso INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES usuario(id)
)
"""

INSERIR_ADMIN = """
INSERT INTO admin (id, nivelAcesso)
SELECT u.id, ?
FROM usuario u
WHERE u.id = ?
"""

OBTER_ADMINS = """
SELECT 
    u.id as id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.dataCriacao as dataCriacao, a.nivelAcesso
FROM admin a
JOIN usuario u ON a.id = u.id
ORDER BY id 
"""

OBTER_ADMIN_POR_EMAIL = """
SELECT 
    u.id as id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.dataCriacao as dataCriacao, a.nivelAcesso
FROM admin a
JOIN usuario u ON a.id = u.id
WHERE u.email = ?
"""

ATUALIZAR_ADMIN_POR_EMAIL = """
UPDATE admin
SET 
    nivelAcesso = ?
WHERE id = (SELECT id FROM usuario WHERE email = ?)
"""

EXCLUIR_ADMIN_POR_EMAIL = """
DELETE FROM admin
WHERE id = (SELECT id FROM usuario WHERE email = ?)
"""

OBTER_ADMIN_PAGINADO = """
SELECT 
    u.id as id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.dataCriacao as dataCriacao, a.nivelAcesso
FROM admin a
JOIN usuario u ON a.id = u.id
ORDER BY u.id
LIMIT ? OFFSET ?
"""

OBTER_ADMIN_POR_ID = """
SELECT 
    u.id as id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.dataCriacao as dataCriacao, a.nivelAcesso
FROM admin a
JOIN usuario u ON a.id = u.id
WHERE u.id = ?
"""

ATUALIZAR_ADMIN_POR_ID = """
UPDATE admin
SET 
    nivelAcesso = ?
WHERE id = ?
"""

EXCLUIR_ADMIN_POR_ID = """
DELETE FROM admin
WHERE id = ?
"""

OBTER_ADMIN_POR_TERMO_PAGINADO = """
SELECT 
    u.id as id, u.nome as nome, u.email as email, u.senha as senha, u.telefone as telefone, u.dataCriacao as dataCriacao, a.nivelAcesso
FROM admin a
JOIN usuario u ON a.id = u.id
WHERE (u.nome LIKE ? OR u.email LIKE ? OR a.nivelAcesso LIKE ?)
ORDER BY u.id
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_ADMINS = """
SELECT COUNT(*) FROM admin
"""
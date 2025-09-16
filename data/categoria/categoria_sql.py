CRIAR_TABELA_CATEGORIA = """
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);
"""

INSERIR_CATEGORIA = """
INSERT INTO categoria (nome)
VALUES (?);
"""

OBTER_CATEGORIA = """
SELECT c.id, c.nome 
FROM categoria c
ORDER BY c.id;
"""

OBTER_CATEGORIA_POR_ID = """
SELECT c.id, c.nome 
FROM categoria c
WHERE c.id = ?;
"""

OBTER_CATEGORIA_POR_NOME = """
SELECT c.id, c.nome
FROM categoria c
WHERE c.nome = ?;
"""

OBTER_QUANTIDADE_CATEGORIA_POR_ID = """
SELECT COUNT(*)
FROM categoria c
WHERE c.id = ?;
"""

OBTER_CATEGORIAS_PAGINADO = """
SELECT c.id, c.nome
FROM categoria c
LIMIT ? OFFSET ?;
"""

OBTER_QUANTIDADE_CATEGORIA_POR_NOME = """
SELECT COUNT(*)
FROM categoria c
WHERE c.nome = ?;
"""

ATUALIZAR_CATEGORIA_POR_ID = """
UPDATE categoria
SET nome = ?
WHERE id = ?;
"""

EXCLUIR_CATEGORIA_POR_ID = """
DELETE FROM categoria
WHERE id = ?;
"""

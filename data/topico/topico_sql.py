CRIAR_TABELA_TOPICO = """
CREATE TABLE IF NOT EXISTS topico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idCategoria INTEGER NOT NULL,
    FOREIGN KEY (idCategoria) REFERENCES categoria(id)
)
"""

INSERIR_TOPICO = """
INSERT INTO topico (nome, idCategoria)
VALUES (?, ?)
"""

OBTER_TOPICOS = """
SELECT 
    t.id, t.nome, t.idCategoria, c.nome as nomeCategoria
FROM topico t
JOIN categoria c ON t.idCategoria = c.id
ORDER BY t.id
"""

OBTER_TOPICOS_PAGINADO = """
SELECT 
    t.id, t.nome, t.idCategoria, c.nome as nomeCategoria
FROM topico t
JOIN categoria c ON t.idCategoria = c.id
ORDER BY t.id
LIMIT ? OFFSET ?
"""

OBTER_TOPICO_POR_ID = """
SELECT 
    t.id, t.nome, t.idCategoria, c.nome as nomeCategoria
FROM topico t
JOIN categoria c ON t.idCategoria = c.id
WHERE t.id = ?
"""

OBTER_TOPICO_POR_CATEGORIA_PAGINADO = """
SELECT 
    t.id, t.nome, t.idCategoria, c.nome as nomeCategoria
FROM topico t
JOIN categoria c ON t.idCategoria = c.id
WHERE t.idCategoria = ?
ORDER BY t.id
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_TOPICOS = """
SELECT COUNT(*) FROM topico
"""

OBTER_QUANTIDADE_TOPICOS_POR_CATEGORIA = """
SELECT COUNT(*) FROM topico t
JOIN categoria c ON t.idCategoria = c.id
WHERE t.idCategoria = ?
"""

OBTER_TOPICO_POR_NOME = """
SELECT 
    t.id, t.nome, t.idCategoria, c.nome as nomeCategoria
FROM topico t
JOIN categoria c ON t.idCategoria = c.id
WHERE t.nome = ?
"""


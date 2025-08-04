CRIAR_TABELA_MATRICULA = """    
CREATE TABLE IF NOT EXISTS matricula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idCliente INTEGER NOT NULL,
    idCurso INTEGER NOT NULL,
    statusMatricula BOOLEAN NOT NULL,
    desempenho TEXT NOT NULL,
    frequencia TEXT NOT NULL,
    dataMatricula TEXT NOT NULL,
    FOREIGN KEY (idCliente) REFERENCES cliente(id),
    FOREIGN KEY (idCurso) REFERENCES curso(id)
)
"""

INSERIR_MATRICULA = """
INSERT INTO matricula (idCliente, idCurso, statusMatricula, desempenho, frequencia, dataMatricula)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_MATRICULAS = """
SELECT 
    m.id,
    m.idCliente, 
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone, 
    m.idCurso, 
    c.nome AS nomeCurso, 
    m.statusMatricula, 
    m.desempenho, 
    m.frequencia, 
    m.dataMatricula
FROM matricula m
JOIN cliente cl ON m.idCliente = cl.id
JOIN usuario u ON cl.id = u.id
JOIN curso c ON m.idCurso = c.id
ORDER BY m.id
"""

OBTER_MATRICULAS_PAGINADO = """
SELECT 
    m.id,
    m.idCliente, 
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone, 
    m.idCurso, 
    c.nome AS nomeCurso, 
    m.statusMatricula, 
    m.desempenho, 
    m.frequencia, 
    m.dataMatricula
FROM matricula m
JOIN cliente cl ON m.idCliente = cl.id 
JOIN usuario u ON cl.id = u.id
JOIN curso c ON m.idCurso = c.id
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_MATRICULA_POR_ID = """
SELECT 
    m.id,
    m.idCliente, 
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone, 
    m.idCurso, 
    c.nome AS nomeCurso, 
    m.statusMatricula, 
    m.desempenho, 
    m.frequencia, 
    m.dataMatricula
FROM matricula m
JOIN cliente cl ON m.idCliente = cl.id
JOIN usuario u ON cl.id = u.id
JOIN curso c ON m.idCurso = c.id
WHERE m.id = ?
"""

OBTER_MATRICULA_POR_NOME= """
SELECT 
    m.id,
    m.idCliente, 
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone, 
    m.idCurso, 
    c.nome AS nomeCurso, 
    m.statusMatricula, 
    m.desempenho, 
    m.frequencia, 
    m.dataMatricula
FROM matricula m
JOIN cliente cl ON m.idCliente = cl.id
JOIN usuario u ON cl.id = u.id  
JOIN curso c ON m.idCurso = c.id
WHERE u.nome LIKE ?
ORDER BY m.id
"""

OBTER_MATRICULA_POR_CURSO = """
SELECT 
    m.id,
    m.idCliente, 
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone, 
    m.idCurso, 
    c.nome AS nomeCurso, 
    m.statusMatricula, 
    m.desempenho, 
    m.frequencia, 
    m.dataMatricula
FROM matricula m
JOIN cliente cl ON m.idCliente = cl.id
JOIN usuario u ON cl.id = u.id
JOIN curso c ON m.idCurso = c.id
WHERE c.nome LIKE ?
ORDER BY m.id
"""

OBTER_MATRICULA_POR_CLIENTE = """
SELECT 
    m.id,
    m.idCliente, 
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone, 
    m.idCurso, 
    c.nome AS nomeCurso, 
    m.statusMatricula, 
    m.desempenho, 
    m.frequencia, 
    m.dataMatricula
FROM matricula m
JOIN cliente cl ON m.idCliente = cl.id
JOIN usuario u ON cl.id = u.id
JOIN curso c ON m.idCurso = c.id
WHERE cl.id = ?
ORDER BY m.id
"""

OBTER_QUANTIDADE_MATRICULA_POR_CURSO = """
SELECT COUNT(*)
FROM matricula m
JOIN curso c ON m.idCurso = c.id
WHERE c.nome LIKE ?
"""


OBTER_QUANTIDADE_MATRICULA_POR_CLIENTE = """
SELECT COUNT(*)
FROM matricula m
JOIN cliente cl ON m.idCliente = cl.id
JOIN usuario u ON cl.id = u.id
WHERE cl.id LIKE ?
"""

OBTER_QUANTIDADE_MATRICULAS = """
SELECT COUNT(*) FROM matricula
"""

ATUALIZAR_MATRICULA_POR_ID = """
UPDATE matricula
SET 
    idCliente = ?, 
    idCurso = ?, 
    statusMatricula = ?, 
    desempenho = ?, 
    frequencia = ?, 
    dataMatricula = ?
WHERE id = ?
"""

EXCLUIR_MATRICULA_POR_ID = """
DELETE FROM matricula WHERE id = ?
"""

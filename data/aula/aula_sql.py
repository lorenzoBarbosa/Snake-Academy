CRIAR_TABELA_AULA = """
CREATE TABLE IF NOT EXISTS aula (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idModulo INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricaoAula TEXT NOT NULL,
    duracaoAula TEXT NOT NULL,
    tipo TEXT NOT NULL,
    ordem INTEGER NOT NULL,
    dataDisponibilidade TEXT NOT NULL,
    FOREIGN KEY (idModulo) REFERENCES modulo(id)
)
"""

INSERIR_AULA = """
INSERT INTO aula (idModulo, titulo, descricaoAula,  duracaoAula, tipo, ordem, dataDisponibilidade)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

OBTER_AULAS = """
SELECT 
    a.id, a.idModulo, c.nome as nomeCurso, m.titulo as tituloModulo, a.titulo, a.descricaoAula, a.duracaoAula, a.tipo, a.ordem, a.dataDisponibilidade
FROM aula a
JOIN modulo m ON a.idModulo = m.id
JOIN curso c ON m.idCurso = c.id
ORDER BY a.id
"""

OBTER_AULAS_PAGINADO_POR_MODULO = """
SELECT 
    a.id, a.idModulo, c.nome as nomeCurso, m.titulo as tituloModulo, a.titulo, a.descricaoAula, a.duracaoAula, a.tipo, a.ordem, a.dataDisponibilidade
FROM aula a
JOIN modulo m ON a.idModulo = m.id
JOIN curso c ON m.idCurso = c.id
WHERE a.idModulo = ?
ORDER BY a.id
LIMIT ? OFFSET ?
"""

OBTER_AULA_POR_ID = """
SELECT 
    a.id, a.idModulo, c.nome as nomeCurso, m.titulo as tituloModulo, a.titulo, a.descricaoAula, a.duracaoAula, a.tipo, a.ordem, a.dataDisponibilidade
FROM aula a
JOIN modulo m ON a.idModulo = m.id
JOIN curso c ON m.idCurso = c.id
WHERE a.id = ?
"""

OBTER_AULA_POR_TITULO= """
SELECT 
    a.id, a.idModulo, c.nome as nomeCurso, m.titulo as tituloModulo, a.titulo, a.descricaoAula, a.duracaoAula, a.tipo, a.ordem, a.dataDisponibilidade       
FROM aula a
JOIN modulo m ON a.idModulo = m.id
JOIN curso c ON m.idCurso = c.id
WHERE a.titulo LIKE ?
ORDER BY a.id
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_AULAS = """
SELECT COUNT(*) FROM aula
"""

OBTER_QUANTIDADE_AULAS_POR_MODULO = """
SELECT COUNT(*) FROM aula a
JOIN modulo m ON a.idModulo = m.id
WHERE a.idModulo = ?
"""

ATUALIZAR_AULA_POR_ID = """
UPDATE aula
SET 
    idModulo = ?, 
    titulo = ?, 
    descricaoAula = ?, 
    duracaoAula = ?, 
    tipo = ?, 
    ordem = ?, 
    dataDisponibilidade = ?
WHERE id = ?
"""

EXCLUIR_AULA_POR_ID = """
DELETE FROM aula WHERE id = ?
"""



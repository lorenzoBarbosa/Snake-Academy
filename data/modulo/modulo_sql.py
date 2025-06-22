CRIAR_TABELA_MODULO= """
CREATE TABLE IF NOT EXISTS modulo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idCurso INTEGER NOT NULL,
    titulo TEXT NOT NULL,
    descricaoModulo TEXT NOT NULL,
    listaAulas TEXT NOT NULL,
    listaExercicios TEXT NOT NULL,
    FOREIGN KEY (idCurso) REFERENCES curso(id)
)
"""
INSERIR_MODULO = """
INSERT INTO modulo (idCurso, titulo, descricaoModulo, listaAulas, listaExercicios)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_MODULOS = """
SELECT 
    m.id, m.idCurso, c.nome as nomeCurso, m.titulo, m.descricaoModulo, m.listaAulas, m.listaExercicios
FROM modulo m
JOIN curso c ON m.idCurso = c.id
ORDER BY m.id
"""

OBTER_MODULOS_PAGINADO = """
SELECT 
    m.id, m.idCurso, c.nome as nomeCurso, m.titulo, m.descricaoModulo, m.listaAulas, m.listaExercicios
FROM modulo m
JOIN curso c ON m.idCurso = c.id
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_MODULO_POR_ID = """
SELECT 
    m.id, m.idCurso, c.nome as nomeCurso, m.titulo, m.descricaoModulo, m.listaAulas, m.listaExercicios
FROM modulo m
JOIN curso c ON m.idCurso = c.id
WHERE m.id = ?
"""

OBTER_MODULO_POR_CURSO_PAGINADO = """
SELECT 
    m.id, m.idCurso, c.nome as nomeCurso, m.titulo, m.descricaoModulo, m.listaAulas, m.listaExercicios
FROM modulo m
JOIN curso c ON m.idCurso = c.id
WHERE m.idCurso = ?
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_MODULOS="""
SELECT COUNT(*) FROM modulo
"""

OBTER_QUANTIDADE_MODULOS_POR_CURSO = """
SELECT COUNT(*) FROM modulo m
JOIN curso c ON m.idCurso = c.id
WHERE m.idCurso = ?
"""

ATUALIZAR_MODULO_POR_ID = """
UPDATE modulo
SET 
    idCurso = ?, 
    titulo = ?, 
    descricaoModulo = ?, 
    listaAulas = ?, 
    listaExercicios = ?
WHERE id = ?
"""

EXCLUIR_MODULO_POR_ID = """
DELETE FROM modulo WHERE id = ?
"""


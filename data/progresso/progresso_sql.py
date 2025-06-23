CRIAR_TABELA_PROGRESSO = """
CREATE TABLE IF NOT EXISTS progresso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idAula INTEGER NOT NULL,
    idMatricula INTEGER NOT NULL,
    dataInicio TEXT NOT NULL,
    dataFim TEXT NOT NULL,
    statusAula TEXT NOT NULL,
    porcentagemConclusao REAL NOT NULL,
    FOREIGN KEY (idAula) REFERENCES aula(id),
    FOREIGN KEY (idMatricula) REFERENCES matricula(id)
)
"""

INSERIR_PROGRESSO = """
INSERT INTO progresso (idAula, idMatricula, dataInicio, dataFim, statusAula, porcentagemConclusao)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_PROGRESSO = """
SELECT 
    p.id, p.idAula, a.titulo as tituloAula, p.idMatricula, m.nome as nome, p.dataInicio, p.dataFim, p.statusAula, p.porcentagemConclusao
FROM progresso p
JOIN aula a ON p.idAula = a.id
JOIN matricula m ON p.idMatricula = m.id
ORDER BY p.id ASC
"""

OBTER_PROGRESSO_PAGINADO = """
SELECT 
    p.id, p.idAula, a.titulo as tituloAula, p.idMatricula, m.nome as nome, p.dataInicio, p.dataFim, p.statusAula, p.porcentagemConclusao
FROM progresso p
JOIN aula a ON p.idAula = a.id
JOIN matricula m ON p.idMatricula = m.id
ORDER BY p.id
LIMIT ? OFFSET ?
"""

OBTER_PROGRESSO_POR_ID = """
SELECT
    p.id, p.idAula, a.titulo as tituloAula, p.idMatricula, m.nome as nome, p.dataInicio, p.dataFim, p.statusAula, p.porcentagemConclusao
FROM progresso p
JOIN aula a ON p.idAula = a.id
JOIN matricula m ON p.idMatricula = m.id
WHERE p.id = ?
ORDER BY p.id ASC
"""

OBTER_PROGRESSO_POR_AULA = """
SELECT
    p.id, p.idAula, a.titulo as tituloAula, p.idMatricula, m.nome as nome, p.dataInicio, p.dataFim, p.statusAula, p.porcentagemConclusao
FROM progresso p
JOIN aula a ON p.idAula = a.id
JOIN matricula m ON p.idMatricula = m.id
WHERE p.idAula = ?
ORDER BY p.id ASC
LIMIT ? OFFSET ?
"""

OBTER_PROGRESSO_POR_MATRICULA = """
SELECT
    p.id, p.idAula, a.titulo as tituloAula, p.idMatricula, m.nome as nome, p.dataInicio, p.dataFim, p.statusAula, p.porcentagemConclusao
FROM progresso p
JOIN aula a ON p.idAula = a.id
JOIN matricula m ON p.idMatricula = m.id
WHERE p.idMatricula = ?
ORDER BY p.id ASC
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_PROGRESSO_POR_AULA = """
SELECT COUNT(*) FROM progresso
WHERE idAula = ?
"""

OBTER_QUANTIDADE_PROGRESSO_POR_MATRICULA = """
SELECT COUNT(*) FROM progresso
WHERE idMatricula = ?
"""

OBTER_QUANTIDADE_PROGRESSO = """
SELECT COUNT(*) FROM progresso
"""

ATUALIZAR_PROGRESSO_POR_ID = """
UPDATE progresso
SET 
    idAula = ?, 
    idMatricula = ?, 
    dataInicio = ?, 
    dataFim = ?, 
    statusAula = ?, 
    porcentagemConclusao = ?
WHERE id = ?
"""

ATUALIZAR_PROGRESSO_POR_MATRICULA_E_AULA = """
UPDATE progresso
SET 
    dataInicio = ?, 
    dataFim = ?, 
    statusAula = ?, 
    porcentagemConclusao = ?
WHERE idMatricula = ? AND idAula = ?
"""

EXCLUIR_PROGRESSO_POR_ID = """
DELETE FROM progresso
WHERE id = ?
"""

EXCLUIR_PROGRESSO_POR_MATRICULA_E_AULA = """
DELETE FROM progresso
WHERE idMatricula = ? AND idAula = ?
"""
CRIAR_TABELA_CURSO="""
CREATE TABLE IF NOT EXISTS curso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idProfessor INTEGER NOT NULL,
    custo REAL NOT NULL,
    descricaoCurso TEXT NOT NULL UNIQUE,
    duracaoCurso TEXT NOT NULL,
    avaliacao TEXT NOT NULL,
    dataCriacao TEXT NOT NULL,
    statusCurso BOOLEAN NOT NULL,
    FOREIGN KEY (idProfessor) REFERENCES professor(id)
)
"""

INSERIR_CURSO = """
INSERT INTO curso (nome, idProfessor, custo, descricaoCurso, duracaoCurso, avaliacao, dataCriacao, statusCurso)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_CURSOS = """
SELECT 
    c.id, c.nome, c.idProfessor, p.nome as nomeProfessor c.custo, c.descricaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM cliente c
JOIN professor p ON c.idProfessor = p.id
ORDER BY id 
"""
OBTER_CURSOS_PAGINADO = """
SELECT 
    c.id, c.nome, c.idProfessor, p.nome as nomeProfessor, c.custo, c.descricaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN professor p ON c.idProfessor = p.id
ORDER BY c.id
LIMIT ? OFFSET ?
"""

OBTER_CURSO_POR_ID = """
SELECT 
    c.id, c.nome, c.idProfessor, p.nome as nomeProfessor, c.custo, c.descricaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN professor p ON c.idProfessor = p.id
WHERE c.id = ?
"""

OBTER_CURSO_POR_TERMO_PAGINADO = """
SELECT 
    c.id, c.nome, c.idProfessor, p.nome as nomeProfessor, c.custo, c.descricaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN professor p ON c.idProfessor = p.id
WHERE (c.nome LIKE ? OR c.descricaoCurso LIKE ? OR p.nome LIKE ?)
ORDER BY c.id
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_CURSOS = """
SELECT COUNT(*) FROM curso
"""

OBTER_QUANTIDADE_CURSOS_POR_NOME_PROFESSOR = """
SELECT COUNT(*) FROM curso c
JOIN professor p ON c.idProfessor = p.id
WHERE p.nome = ?
"""

ATUALIZAR_CURSO_POR_ID = """
UPDATE curso
SET 
    nome = ?, 
    idProfessor = ?, 
    custo = ?, 
    descricaoCurso = ?, 
    duracaoCurso = ?, 
    avaliacao = ?, 
    dataCriacao = ?, 
    statusCurso = ?
WHERE id = ?
"""

EXCLUIR_CURSO_POR_ID = """
DELETE FROM curso
WHERE id = ?
"""


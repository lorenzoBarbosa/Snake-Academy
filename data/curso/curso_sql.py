CRIAR_TABELA_CURSO="""
CREATE TABLE IF NOT EXISTS curso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idTopico INTEGER NOT NULL,
    nome TEXT NOT NULL,
    idProfessor INTEGER NOT NULL,
    custo REAL NOT NULL,
    descricaoCurso TEXT NOT NULL,
    duracaoCurso TEXT NOT NULL,
    avaliacao TEXT NOT NULL,
    dataCriacao TEXT NOT NULL,
    statusCurso BOOLEAN NOT NULL,
    FOREIGN KEY (idProfessor) REFERENCES professor(id),
    FOREING KEY (idTopico) REFERENCES topico(id)
)
"""

INSERIR_CURSO = """
INSERT INTO curso (idTopico, nome, idProfessor, custo, descricaoCurso, duracaoCurso, avaliacao, dataCriacao, statusCurso)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_CURSOS = """
SELECT 
    c.id, i.idTopico, c.nome, c.idProfessor, u.nome as nomeProfessor, c.custo, c.descricaoCurso, c.duracaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN topico i ON c.idTopico = i.id
JOIN professor p ON c.idProfessor = p.id
JOIN cliente cli ON p.id = cli.id
JOIN usuario u ON cli.id = u.id
ORDER BY c.id 
"""
OBTER_CURSOS_POR_PROFESSOR = """
SELECT 
    c.id, i.idTopico, c.nome, c.idProfessor, u.nome as nomeProfessor, c.custo, c.descricaoCurso, c.duracaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN topico i ON c.idTopico = i.id
JOIN professor p ON c.idProfessor = p.id
JOIN cliente cli ON p.id = cli.id
JOIN usuario u ON cli.id = u.id
WHERE c.idProfessor = ?
ORDER BY c.id
"""

OBTER_CURSOS_PAGINADO = """
SELECT 
    c.id, i.idTopico, c.nome, c.idProfessor, u.nome as nomeProfessor, c.custo, c.descricaoCurso, c.duracaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN topico i ON c.idTopico = i.id
JOIN professor p ON c.idProfessor = p.id
JOIN cliente cli ON p.id = cli.id
JOIN usuario u ON cli.id = u.id
ORDER BY c.id
LIMIT ? OFFSET ?
"""

OBTER_CURSO_POR_ID = """
SELECT 
    c.id, i.idTopico, c.nome, c.idProfessor, u.nome as nomeProfessor, c.custo, c.descricaoCurso, c.duracaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN topico i ON c.idTopico = i.id
JOIN professor p ON c.idProfessor = p.id
JOIN cliente cli ON p.id = cli.id
JOIN usuario u ON cli.id = u.id
WHERE c.id = ?
"""

OBTER_CURSO_POR_TERMO_PAGINADO = """
SELECT 
    c.id, i.idTopico, c.nome, c.idProfessor, u.nome as nomeProfessor, c.custo, c.descricaoCurso, c.duracaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN topico i ON c.idTopico = i.id
JOIN professor p ON c.idProfessor = p.id
JOIN cliente cli ON p.id = cli.id
JOIN usuario u ON cli.id = u.id
WHERE (c.nome LIKE ? OR c.descricaoCurso LIKE ? OR u.nome LIKE ?)
ORDER BY c.id
LIMIT ? OFFSET ?
"""
OBTER_QUANTIDADE_CURSOS = """
SELECT COUNT(*) FROM curso
"""

OBTER_QUANTIDADE_CURSOS_POR_NOME_PROFESSOR = """
SELECT COUNT(*) FROM curso c
JOIN professor p ON c.idProfessor = p.id
JOIN usuario u ON p.id = u.id
WHERE u.nome = ?
"""

OBTER_CURSOS_POR_TOPICO = """
SELECT
    c.id, i.idTopico, i.nome as nomeTopico, c.nome, c.idProfessor, u.nome as nomeProfessor, c.custo, c.descricaoCurso, c.duracaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN topico i ON c.idTopico = i.id
JOIN professor p ON c.idProfessor = p.id
JOIN cliente cli ON p.id = cli.id
JOIN usuario u ON cli.id = u.id
WHERE i.nome = ?
ORDER BY c.id
"""

OBTER_CURSOS_POR_ID_TOPICO = """
SELECT
    c.id, i.idTopico, i.nome as nomeTopico, c.nome, c.idProfessor, u.nome as nomeProfessor, c.custo, c.descricaoCurso, c.duracaoCurso, c.avaliacao, c.dataCriacao, c.statusCurso
FROM curso c
JOIN topico i ON c.idTopico = i.id
JOIN professor p ON c.idProfessor = p.id
JOIN cliente cli ON p.id = cli.id
JOIN usuario u ON cli.id = u.id
WHERE i.id = ?
ORDER BY c.id
"""

ATUALIZAR_CURSO_POR_ID = """
UPDATE curso
SET 
    idTopico = ?,
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


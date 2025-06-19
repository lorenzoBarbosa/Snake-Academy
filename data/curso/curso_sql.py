CRIAR_TABELA_CURSO="""
CREATE TABLE IF NOT EXISTS curso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idProfessor INTEGER NOT NULL,
    custo REAL NOT NULL,
    descricaoCurso TEXT NOT NULL UNIQUE,
    duracaoCurso TEXT NOT NULL,
    avaliacao TEXT NOT NULL,
    dataCriacao TEXT NOT NULL,
    satatusCurso BOOLEAN NOT NULL,
    FOREIGN KEY (idProfessor) REFERENCES professor(id)
)
"""

INSERIR_CURSO = """
INSERT INTO curso (idProfessor, custo, descricaoCurso, duracaoCurso, avaliacao, dataCriacao, statusCurso)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

OBTER_CURSOS = """
SELECT 
    id, idProfessor, custo, descricaoCurso, avaliacao, dataCriacao, statusCurso
FROM cliente
ORDER BY id 
"""

OBTER_CLIENTE_POR_EMAIL = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusCurso, historicoCursos, indentificacaoProfessor
FROM cliente
WHERE email = ?
"""

ATUALIZAR_CLIENTE_POR_EMAIL= """
UPDATE cliente
SET 
    nome = ?, 
    email = ?, 
    senha = ?, 
    telefone = ?, 
    dataCriacao = ?,
    dataUltimoAcesso = ?, 
    statusCurso = ?, 
    historicoCursos = ?, 
    indentificacaoProfessor = ?
WHERE email = ?
"""

EXCLUIR_CLIENTE_POR_EMAIL = """
DELETE FROM cliente
WHERE email = ?
"""

OBTER_QUANTIDADE_CLIENTES = """
SELECT COUNT(*) AS quantidade
FROM cliente
"""

OBTER_CLIENTE_PAGINADO = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusCurso, historicoCursos, indentificacaoProfessor
FROM cliente
ORDER BY id
LIMIT ? OFFSET ?
"""  # LIMIT determina quantos registros serão retornados, OFFSET determina a partir de qual registro começar a retornar
# Caso o LIMIT seja 10 e o OFFSET seja 0, os primeiros 10 registros serão retornados.
# Caso o LIMIT seja 10 e o OFFSET seja 10, os próximos 10 registros serão retornados.

OBTER_CLIENTE_POR_ID = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusCurso, historicoCursos, indentificacaoProfessor
FROM cliente
WHERE id = ?
"""

ATUALIZAR_CLIENTE_POR_ID = """
UPDATE cliente
SET 
    nome = ?, 
    email = ?, 
    senha = ?, 
    telefone = ?, 
    dataCriacao = ?,
    dataUltimoAcesso = ?, 
    statusCurso = ?, 
    historicoCursos = ?, 
    indentificacaoProfessor = ?
WHERE id = ?
"""

EXCLUIR_CLIENTE_POR_ID = """
DELETE FROM cliente
WHERE id = ?
"""

OBTER_CLIENTE_POR_TERMO_PAGINADO = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusCurso, historicoCursos, indentificacaoProfessor
FROM cliente
WHERE (nome LIKE ? OR email LIKE ? OR statusCurso LIKE ?)
ORDER BY id
LIMIT ? OFFSET ?
"""
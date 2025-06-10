CRIAR_TABELA_PROFESSOR = """
CREATE TABLE IF NOT EXISTS professor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL,
    dataCriacao TEXT NOT NULL,
    dataUltimoAcesso TEXT NOT NULL,
    statusConta BOOLEAN NOT NULL,
    historicoCursos TEXT NOT NULL,
    indentificacaoProfessor BOOLEAN NOT NULL,
    cursosPostados TEXT NOT NULL DEFAULT '[]',
    quantidadeAlunos INTEGER NOT NULL,
    dataCriacaoProfessor TEXT NOT NULL
)
"""
INSERIR_PROFESSOR = """
INSERT INTO professor (nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor, cursosPostados, quantidadeAlunos, dataCriacaoProfessor)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

OBTER_PROFESSORS = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor, cursosPostados, quantidadeAlunos, dataCriacaoProfessor
FROM professor
ORDER BY id 
"""

OBTER_PROFESSOR_POR_EMAIL = """
SELECT 
    id, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso, statusConta, historicoCursos, indentificacaoProfessor, cursosPostados, quantidadeAlunos, dataCriacaoProfessor
FROM professor
WHERE email = ?
"""

ATUALIZAR_PROFESSOR_POR_EMAIL= """
UPDATE professor
SET 
    nome = ?, 
    email = ?, 
    senha = ?, 
    telefone = ?, 
    dataCriacao = ?,
    dataUltimoAcesso = ?, 
    statusConta = ?, 
    historicoCursos = ?, 
    indentificacaoProfessor = ?,
    cursosPostados= ?,
    quantidadeAlunos= ?,
    dataCriacaoProfessor = ?
WHERE email = ?
"""

EXCLUIR_PROFESSOR_POR_EMAIL = """
DELETE FROM professor
WHERE email = ?
"""



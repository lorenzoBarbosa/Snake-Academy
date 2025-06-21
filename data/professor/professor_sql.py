CRIAR_TABELA_PROFESSOR = """
CREATE TABLE IF NOT EXISTS professor (
    id INTEGER PRIMARY KEY,
    cursosPostados TEXT NOT NULL DEFAULT '[]',
    quantidadeAlunos INTEGER NOT NULL,
    dataCriacaoProfessor TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES cliente(id)
)
"""

INSERIR_PROFESSOR = """
INSERT INTO professor (id, cursosPostados, quantidadeAlunos, dataCriacaoProfessor)
SELECT c.id, ?, ?, ?
FROM cliente c
WHERE c.id = ?
"""
OBTER_PROFESSOR_POR_EMAIL = """
SELECT 
    c.id as id,
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone,
    u.dataCriacao as dataCriacao,
    c.dataUltimoAcesso as dataUltimoAcesso,
    c.statusConta as statusConta,
    c.historicoCursos as historicoCursos,
    c.indentificacaoProfessor as indentificacaoProfessor,
    p.cursosPostados,
    p.quantidadeAlunos,
    p.dataCriacaoProfessor
FROM professor p
JOIN cliente c ON p.id = c.id
JOIN usuario u ON c.id = u.id
WHERE u.email = ?
"""

OBTER_PROFESSOR_POR_ID = """
SELECT 
    c.id as id,
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone,
    u.dataCriacao as dataCriacao,
    c.dataUltimoAcesso as dataUltimoAcesso,
    c.statusConta as statusConta,
    c.historicoCursos as historicoCursos,
    c.indentificacaoProfessor as indentificacaoProfessor,
    p.cursosPostados,
    p.quantidadeAlunos,
    p.dataCriacaoProfessor
FROM professor p
JOIN cliente c ON p.id = c.id
JOIN usuario u ON c.id = u.id
WHERE c.id = ?
"""

OBTER_PROFESSOR = """
SELECT 
    c.id as id,
    u.nome as nome,
    u.email as email,
    u.senha as senha,
    u.telefone as telefone,
    u.dataCriacao as dataCriacao,
    c.dataUltimoAcesso as dataUltimoAcesso,
    c.statusConta as statusConta,
    c.historicoCursos as historicoCursos,
    c.indentificacaoProfessor as indentificacaoProfessor,
    p.cursosPostados,
    p.quantidadeAlunos,
    p.dataCriacaoProfessor
FROM professor p
JOIN cliente c ON p.id = c.id
JOIN usuario u ON c.id = u.id
ORDER BY id 
"""

ATUALIZAR_PROFESSOR_POR_EMAIL= """
UPDATE professor
SET 
    cursosPostados= ?,
    quantidadeAlunos= ?,
    dataCriacaoProfessor = ?
WHERE email = ?
"""

EXCLUIR_PROFESSOR_POR_EMAIL = """
DELETE FROM professor
WHERE email = ?
"""



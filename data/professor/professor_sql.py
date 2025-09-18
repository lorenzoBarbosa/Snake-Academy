CRIAR_TABELA_PROFESSOR = """
CREATE TABLE IF NOT EXISTS professor (
    id INTEGER PRIMARY KEY,
    cursosPostados TEXT NOT NULL DEFAULT '[]',
    quantidadeAlunos INTEGER NOT NULL,
    dataCriacaoProfessor TEXT NOT NULL,
    descricaoProfessor TEXT,
    FOREIGN KEY (id) REFERENCES cliente(id)
)
"""

INSERIR_PROFESSOR = """
INSERT INTO professor (id, cursosPostados, quantidadeAlunos, dataCriacaoProfessor, descricaoProfessor)
SELECT c.id, ?, ?, ?, ?
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
    u.dataNascimento as dataNascimento,
    c.dataUltimoAcesso as dataUltimoAcesso,
    c.statusConta as statusConta,
    c.historicoCursos as historicoCursos,
    c.indentificacaoProfessor as indentificacaoProfessor,
    p.cursosPostados,
    p.quantidadeAlunos,
    p.dataCriacaoProfessor,
    p.descricaoProfessor
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
    u.dataNascimento as dataNascimento,
    u.perfil as perfil,
    u.token_redefinicao as token_redefinicao,
    u.data_token as data_token,
    u.data_cadastro as data_cadastro,
    u.foto as foto,
    c.dataUltimoAcesso as dataUltimoAcesso,
    c.statusConta as statusConta,
    c.historicoCursos as historicoCursos,
    c.indentificacaoProfessor as indentificacaoProfessor,
    p.cursosPostados,
    p.quantidadeAlunos,
    p.dataCriacaoProfessor,
    p.descricaoProfessor
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
    u.dataNascimento as dataNascimento,
    c.dataUltimoAcesso as dataUltimoAcesso,
    c.statusConta as statusConta,
    c.historicoCursos as historicoCursos,
    c.indentificacaoProfessor as indentificacaoProfessor,
    p.cursosPostados,
    p.quantidadeAlunos,
    p.dataCriacaoProfessor,
    p.descricaoProfessor
FROM professor p
JOIN cliente c ON p.id = c.id
JOIN usuario u ON c.id = u.id
ORDER BY id 
"""

ATUALIZAR_PROFESSOR_POR_ID= """
UPDATE professor
SET 
    cursosPostados= ?,
    quantidadeAlunos= ?,
    dataCriacaoProfessor = ?,
    descricaoProfessor = ?
WHERE id = ?
"""

ATUALIZAR_PROFESSOR_POR_EMAIL= """
UPDATE professor
SET 
    cursosPostados= ?,
    quantidadeAlunos= ?,
    dataCriacaoProfessor = ?,
    descricaoProfessor = ?
WHERE id = (SELECT id FROM usuario WHERE email = ?)
"""

EXCLUIR_PROFESSOR_POR_EMAIL = """
DELETE FROM professor
WHERE id = (SELECT id FROM usuario WHERE email = ?)
"""

EXCLUIR_PROFESSOR_POR_ID = """
DELETE FROM professor
WHERE id = ?
"""



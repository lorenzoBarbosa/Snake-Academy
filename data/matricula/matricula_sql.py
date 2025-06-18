CRIAR_TABELA_MATRICULA = """
CREATE TABLE IF NOT EXISTS matricula (
    idMatricula INTEGER PRIMARY KEY AUTOINCREMENT,
    id INTEGER NOT NULL,
    idCurso INTEGER NOT NULL,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL,
    dataCriacao TEXT NOT NULL,
    dataUltimoAcesso TEXT NOT NULL,
    statusConta BOOLEAN NOT NULL,
    historicoCursos TEXT NOT NULL,
    indentificacaoProfessor BOOLEAN NOT NULL,
    status_matricula TEXT NOT NULL,
    desempenho TEXT NOT NULL,
    frequencia TEXT NOT NULL,
    data_matricula TEXT NOT NULL,
    FOREIGN KEY (id) REFERENCES cliente(id),
    FOREIGN KEY (idCurso) REFERENCES curso(id)
    )"""

INSERIR_MATRICULA = """
INSERT INTO matricula (
    id, idCurso, nome, email, senha, telefone, dataCriacao, dataUltimoAcesso,
    statusConta, historicoCursos, indentificacaoProfessor,
    status_matricula, desempenho, frequencia, data_matricula) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

OBTER_MATRICULAS = """
SELECT 
    idMatricula, id, idCurso, nome, email, senha, telefone, dataCriacao, 
    dataUltimoAcesso, statusConta, historicoCursos, 
    indentificacaoProfessor, status_matricula, desempenho, 
    frequencia, data_matricula
FROM matricula
ORDER BY idMatricula ASC
"""

OBTER_MATRICULA_POR_ID = """
SELECT 
    m.idMatricula, m.id, m.idCurso, m.nome, m.email, m.senha, m.telefone, m.dataCriacao, 
    m.dataUltimoAcesso, m.statusConta, m.historicoCursos, 
    m.indentificacaoProfessor, m.status_matricula, m.desempenho, 
    m.frequencia, m.data_matricula, c.nome as nomeCurso
FROM matricula m
JOIN curso c ON m.idCurso = c.id
WHERE idMatricula = ?
ORDER BY idMatricula ASC
"""

ATUALIZAR_MATRICULA_POR_EMAIL= """
UPDATE matricula
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
    status_matricula = ?,
    desempenho = ?,
    frequencia = ?,
    data_matricula = ?
WHERE email = ?
"""

EXCLUIR_MATRICULA_POR_ID = """
DELETE FROM matricula
WHERE idMatricula = ?
"""


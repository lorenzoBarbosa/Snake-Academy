CRIAR_TABELA_MATRICULA = """
CREATE TABLE IF NOT EXISTS matricula (
    id_matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    FOREING KEY (id) REFERENCES cliente(id),
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
    data_matricula TEXT NOT NULL
    )"""

INSERIR_MATRICULA = """
INSERT INTO matricula (
    nome, email, senha, telefone, dataCriacao, dataUltimoAcesso,
    statusConta, historicoCursos, indentificacaoProfessor,
    status_matricula, desempenho, frequencia, data_matricula) 
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

OBTER_MATRICULAS = """
SELECT 
    id_matricula, nome, email, senha, telefone, dataCriacao, 
    dataUltimoAcesso, statusConta, historicoCursos, 
    indentificacaoProfessor, status_matricula, desempenho, 
    frequencia, data_matricula
FROM matricula
ORDER BY id_matricula ASC
"""

OBTER_MATRICULA_POR_ID = """
SELECT 
    id_matricula, nome, email, senha, telefone, dataCriacao, 
    dataUltimoAcesso, statusConta, historicoCursos, 
    indentificacaoProfessor, status_matricula, desempenho, 
    frequencia, data_matricula
FROM matricula
WHERE id_matricula = ?
ORDER BY id_matricula ASC
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
WHERE id_matricula = ?
"""


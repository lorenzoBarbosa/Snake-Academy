CRIAR_TABELA_MENSAGEM_COMUNIDADE = """
CREATE TABLE IF NOT EXISTS mensagemComunidade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idMatricula INTEGER NOT NULL,
    idComunidade INTEGER NOT NULL,
    conteudo TEXT NOT NULL,
    dataEnvio TEXT NOT NULL,
    horaEnvio TEXT NOT NULL,
    visualizacao BOOLEAN NOT NULL,
    FOREIGN KEY (idMatricula) REFERENCES matricula(id),
    FOREIGN KEY (idComunidade) REFERENCES comunidade(id)
)
"""

GERAR_MENSAGEM_COMUNIDADE = """
INSERT INTO mensagemComunidade (idMatricula, idComunidade, conteudo, dataEnvio, horaEnvio, visualizacao)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_MENSAGENS_COMUNIDADE = """
SELECT 
    m.id, m.idMatricula, m.idComunidade, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagemComunidade m
JOIN matricula ma ON m.idMatricula = ma.id
JOIN comunidade c ON m.idComunidade = c.id
ORDER BY m.id ASC
"""

OBTER_MENSAGEM_COMUNIDADE_PAGINADO = """
SELECT
    m.id, m.idMatricula, m.idComunidade, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagemComunidade m
JOIN matricula ma ON m.idMatricula = ma.id
JOIN comunidade c ON m.idComunidade = c.id
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_MENSAGEM_COMUNIDADE_POR_TERMO_PAGINADO = """
SELECT
    m.id, m.idMatricula, ma.nome as nomeMatricula, m.idComunidade, c.nome as nomeComunidade, m.conteudo, m.dataEnvio, m.horaEnvio
FROM mensagemComunidade m
JOIN matricula ma ON m.idMatricula = ma.id
JOIN comunidade c ON m.idComunidade = c.id
WHERE ma.nome LIKE ? OR m.conteudo LIKE ?
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_MENSAGEM_COMUNIDADE_POR_ID = """
SELECT 
    m.id, m.idMatricula, m.idComunidade, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagemComunidade m
JOIN comunidade c ON m.idComunidade = c.id
WHERE m.id = ?
ORDER BY m.id ASC
"""


OBTER_MENSAGEM_COMUNIDADE_POR_MATRICULA = """
SELECT 
    m.id, m.idMatricula, m.idComunidade, m.conteudo, m.dataEnvio, m.horaEnvio
FROM mensagemComunidade m
JOIN matricula ma ON m.idMatricula = ma.id
JOIN comunidade c ON m.idComunidade = c.id
WHERE ma.nome LIKE ?
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_MENSAGEM_COMUNIDADE_POR_COMUNIDADE = """
SELECT 
    m.id, m.idMatricula, ma.nome as nomeMatricula, m.idComunidade, c.nome as nomeComunidade, m.conteudo, m.dataEnvio, m.horaEnvio
FROM mensagemComunidade m
JOIN matricula ma ON m.idMatricula = ma.id
JOIN comunidade c ON m.idComunidade = c.id
WHERE c.nome LIKE ?
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_QUANITDADE_MENSAGEM_COMUNIDADE = """
SELECT COUNT(*) FROM mensagemComunidade
"""

OBTER_QUANTIDADE_MENSAGEM_COMUNIDADE_POR_MATRICULA = """
SELECT COUNT(*) FROM mensagemComunidade m
JOIN matricula ma ON m.idMatricula = ma.id
WHERE ma.nome LIKE ?
"""

OBTER_QUANTIDADE_MENSAGEM_COMUNIDADE_POR_COMUNIDADE = """
SELECT COUNT(*) FROM mensagemComunidade m
JOIN comunidade c ON m.idComunidade = c.id
WHERE c.nome LIKE ?
"""

ATUALIZAR_MENSAGEM_COMUNIDADE = """
UPDATE mensagemComunidade
SET 
    idMatricula = ?,
    idComunidade = ?,
    conteudo = ?,
    dataEnvio = ?,
    horaEnvio = ?
WHERE id = ?
"""

EXCLUIR_MENSAGEM_COMUNIDADE = """
DELETE FROM mensagemComunidade
WHERE id = ?
"""


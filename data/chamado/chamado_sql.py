CRIAR_TABELA_CHAMADO = """
CREATE TABLE IF NOT EXISTS chamado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idUsuario INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    dataEnvio TEXT NOT NULL,
    horaEnvio TEXT NOT NULL,
    visualizacao BOOLEAN NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES usuario(id)
)
    """

GERAR_CHAMADO = """
INSERT INTO chamado (idUsuario, descricao, dataEnvio, horaEnvio, visualizacao)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_CHAMADOS = """
SELECT 
    id, idUsuario, descricao, dataEnvio, horaEnvio, visualizacao  
FROM chamado
ORDER BY id ASC
"""

OBTER_CHAMADO_PAGINADO = """
SELECT
    c.id, c.idUsuario, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeUsuario
FROM chamado c
JOIN usuario u ON c.idUsuario = u.id
ORDER BY c.idUsuario
LIMIT ? OFFSET ?
"""

OBTER_CHAMADO_POR_TERMO_PAGINADO = """
SELECT
    c.id, c.idUsuario, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeUsuario
FROM chamado c
JOIN usuario u ON c.idUsuario = u.id
WHERE c.id LIKE ? OR u.nome LIKE ? or c.descricao LIKE ?
ORDER BY c.id_usuario
LIMIT ? OFFSET ?
"""

OBTER_CHAMADO_POR_ID = """
SELECT 
    c.id, c.idUsuario, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeUsuario
FROM chamado as c
JOIN usuario as u ON c.idUsuario = u.id
WHERE c.id = ?
ORDER BY c.id ASC
"""

OBTER_CHAMADO_POR_NOME_USUARIO = """
SELECT
    c.id, c.idUsuario, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeUsuario
FROM chamado c
JOIN usuario u ON c.idUsuario = u.id
WHERE u.nome = ?
ORDER BY c.id_usuario
LIMIT ? OFFSET ?
"""

EXCLUIR_CHAMADO_POR_ID = """
DELETE FROM chamado
WHERE id = ?
"""

OBTER_QUANTIDADE_CHAMADOS = """
SELECT COUNT(*) FROM chamado
"""

OBTER_QUANTIDADE_CHAMADOS_POR_NOME_USUARIO= """
SELECT COUNT(*)
FROM chamado c
JOIN usuario u ON c.idUsuario = u.id
WHERE u.nome LIKE ? 
"""



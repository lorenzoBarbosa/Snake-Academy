CRIAR_TABELA_RCHAMADO = """
CREATE TABLE IF NOT EXISTS respostaChamado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idAdmin INTEGER NOT NULL,
    idChamado INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    dataEnvio TEXT NOT NULL,
    horaEnvio TEXT NOT NULL,
    visualizacao BOOLEAN NOT NULL,
    FOREIGN KEY (idAdmin) REFERENCES admin(id),
    FOREIGN KEY (idChamado) REFERENCES chamado(id)
)
"""

GERAR_RCHAMADO = """
INSERT INTO respostaChamado (idAdmin, idChamado, descricao, dataEnvio, horaEnvio, visualizacao)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_RCHAMADOS = """
SELECT 
    id, idAdmin, idChamado, descricao, dataEnvio, horaEnvio, visualizacao  
FROM respostaChamado
ORDER BY id ASC
"""

OBTER_RCHAMADO_PAGINADO = """
SELECT
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeAdmin
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
JOIN usuario u ON a.id = u.id
ORDER BY c.idAdmin
LIMIT ? OFFSET ?
"""

OBTER_RCHAMADO_POR_TERMO_PAGINADO = """
SELECT
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeAdmin
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
JOIN usuario u ON a.id = u.id
WHERE c.id LIKE ? OR u.nome LIKE ? or c.descricao LIKE ?
ORDER BY c.idAdmin
LIMIT ? OFFSET ?
"""

OBTER_RCHAMADO_POR_ID = """
SELECT 
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeAdmin
FROM respostaChamado as c
JOIN admin a ON c.idAdmin = a.id
JOIN usuario u ON a.id = u.id
WHERE c.id = ?
ORDER BY c.id ASC
"""

OBTER_RCHAMADO_POR_NOME_ADMIN = """
SELECT
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeAdmin
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
JOIN usuario u ON a.id = u.id
WHERE u.nome = ?
ORDER BY c.idAdmin
LIMIT ? OFFSET ?
"""

EXCLUIR_RCHAMADO_POR_ID = """
DELETE FROM respostaChamado
WHERE id = ?
"""

OBTER_QUANTIDADE_RCHAMADOS = """
SELECT COUNT(*) FROM respostaChamado
"""

OBTER_QUANTIDADE_RCHAMADOS_POR_NOME_ADMIN= """
SELECT COUNT(*)
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
JOIN usuario u ON a.id = u.id
WHERE u.nome LIKE ? 
"""

OBTER_RCHAMADO_POR_ID_CHAMADO= """
SELECT 
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, u.nome as nomeAdmin
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
JOIN usuario u ON a.id = u.id
WHERE c.idChamado = ?
ORDER BY c.idAdmin
"""




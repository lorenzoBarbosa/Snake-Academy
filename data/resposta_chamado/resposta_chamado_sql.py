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
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, a.nome as nomeAdmin
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
ORDER BY c.id_admin
LIMIT ? OFFSET ?
"""

OBTER_RCHAMADO_POR_TERMO_PAGINADO = """
SELECT
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, a.nome as nomeAdmin
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
WHERE c.id LIKE ? OR a.nome LIKE ? or c.descricao LIKE ?
ORDER BY c.id_admin
LIMIT ? OFFSET ?
"""

OBTER_RCHAMADO_POR_ID = """
SELECT 
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, a.nome as nomeAdmin
FROM respostaChamado as c
JOIN admin a ON c.idAdmin = a.id
WHERE id = ?
ORDER BY id ASC
"""

OBTER_RCHAMADO_POR_NOME_ADMIN = """
SELECT
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, a.nome as nomeAdmin
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
WHERE a.nome = ?
ORDER BY c.id_admin
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
JOIN admin a ON c.idUsuario = a.id
WHERE a.nome LIKE ? 
"""

OBTER_RCHAMADO_POR_ID_CHAMADO= """
SELECT 
    c.id, c.idAdmin, c.idChamado, c.descricao, c.dataEnvio, c.horaEnvio, c.visualizacao, a.nome as nomeAdmin
FROM respostaChamado c
JOIN admin a ON c.idAdmin = a.id
WHERE c.idChamado = ?
ORDER BY c.id_admin
LIMIT ? OFFSET ?
"""




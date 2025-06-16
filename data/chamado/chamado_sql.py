CRIAR_TABELA_CHAMADO = """
CREATE TABLE IF NOT EXISTS chamado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    dataEnvio TEXT NOT NULL,
    horaEnvio TEXT NOT NULL,
    vizualizacao BOOLEAN NOT NULL,
    FOREIGN KEY (idUsuario) REFERENCES usuario(id)
    """

GERAR_CHAMADO = """
INSERT INTO chamado (descricao, dataEnvio, horaEnvio, vizualizacao, idUsuario)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_CHAMADOS = """
SELECT 
    id, descricao, dataEnvio, horaEnvio, vizualizacao, idUsuario    
FROM chamado
ORDER BY id ASC, idUsuario ASC
"""

OBTER_CHAMADO_POR_ID_USUARIO = """
SELECT 
    id, descricao, dataEnvio, horaEnvio, vizualizacao, idUsuario
FROM chamado
WHERE idUsuario = ?
ORDER BY id ASC
"""

EXCLUIR_CHAMADO_POR_ID = """
DELETE FROM chamado
WHERE id = ?
"""





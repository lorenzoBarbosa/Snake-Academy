CRIAR_TABELA_RESPOSTA_CHAMADO = """
CREATE TABLE IF NOT EXISTS RESPOSTA_CHAMADO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feedback TEXT NOT NULL,
    dataEnvio TEXT NOT NULL,
    visualizacao BOOLEAN NOT NULL,
    horaEnvio TEXT NOT NULL,
    FOREIGN KEY (idAdmin) REFERENCES Admin(id)
    """

GERAR_RESPOSTA_CHAMADO = """
INSERT INTO RESPOSTA_CHAMADO (feedback, dataEnvio, visualizacao, horaEnvio, idAdmin)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_RESPOSTA_CHAMADOS = """
SELECT 
    id, feedback, dataEnvio, visualizacao, horaEnvio,  idAdmin    
FROM RESPOSTA_CHAMADO
ORDER BY id ASC, idAdmin ASC
"""

OBTER_RESPOSTA_CHAMADO_POR_ID_ADMIN = """
SELECT 
    id, feedback, dataEnvio, visualizacao, horaEnvio, idAdmin
FROM RESPOSTA_CHAMADO
WHERE idAdmin = ?
ORDER BY id ASC
"""

EXCLUIR_RESPOSTA_CHAMADO_POR_ID = """
DELETE FROM chamado
WHERE id = ?
"""





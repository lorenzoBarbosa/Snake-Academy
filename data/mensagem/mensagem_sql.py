CRIAR_TABELA_MENSAGEM = """
CREATE TABLE IF NOT EXISTS mensagem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idRemetente INTEGER NOT NULL,
    idDestinatario INTEGER NOT NULL,
    conteudo TEXT NOT NULL,
    dataEnvio TEXT NOT NULL,
    horaEnvio TEXT NOT NULL,
    visualizacao BOOLEAN NOT NULL,
    FOREIGN KEY (idRemetente) REFERENCES usuario(id),
    FOREIGN KEY (idDestinatario) REFERENCES usuario(id)
   
)
    """

GERAR_MENSAGEM = """
INSERT INTO mensagem (idRemetente, idDestinatario, conteudo, dataEnvio, horaEnvio, visualizacao)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_MENSAGENS = """
SELECT 
    m.id, m.idRemetente, r.nome as nomeRemetente, m.idDestinatario, d.nome as nomeDestinatario, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao  
FROM mensagem m
JOIN usuario r ON m.idRemetente = r.id
JOIN usuario d ON m.idDestinatario = d.id
ORDER BY m.id ASC
"""

OBTER_MENSAGEM_PAGINADO = """
SELECT
    m.id, m.idRemetente, r.nome as nomeRemetente, m.idDestinatario, d.nome as nomeDestinatario, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagem m
JOIN usuario r ON m.idRemetente = r.id
JOIN usuario d ON m.idDestinatario = d.id
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_MENSAGEM_POR_TERMO_PAGINADO = """
SELECT
    m.id, m.idRemetente, r.nome as nomeRemetente, m.idDestinatario, d.nome as nomeDestinatario, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagem m
JOIN usuario r ON m.idRemetente = r.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE m.id LIKE ? OR r.nome LIKE ? OR m.conteudo LIKE ?
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_MENSAGEM_POR_ID = """
SELECT 
    m.id, m.idRemetente, r.nome as nomeRemetente, m.idDestinatario, d.nome as nomeDestinatario, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagem m
JOIN usuario r ON m.idRemetente = r.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE m.id = ?
ORDER BY m.id ASC
"""

OBTER_MENSAGEM_POR_ID_TESTE = """
SELECT 
    m.id, m.idRemetente, m.idDestinatario, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagem m
WHERE m.id = ?
ORDER BY m.id ASC
"""

OBTER_MENSAGEM_POR_NOME_REMETENTE= """
SELECT
    m.id, m.idRemetente, r.nome as nomeRemetente, m.idDestinatario, d.nome as nomeDestinatario, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagem m
JOIN usuario r ON m.idRemetente = r.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE r.nome = ?
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_MENSAGEM_POR_NOME_DESTINATARIO = """
SELECT
    m.id, m.idRemetente, r.nome as nomeRemetente, m.idDestinatario, d.nome as nomeDestinatario, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao
FROM mensagem m
JOIN usuario r ON m.idRemetente = r.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE d.nome = ?
ORDER BY m.id
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_MENSAGEM = """
SELECT COUNT(*) FROM mensagem
"""

OBTER_QUANTIDADE_MENSAGEM_POR_NOME_REMETENTE= """
SELECT COUNT(*)
FROM mensagem m
JOIN usuario r ON m.idRemetente = r.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE r.nome LIKE ? 
"""

OBTER_QUANTIDADE_MENSAGEM_POR_NOME_DESTINATARIO = """
SELECT COUNT(*)
FROM mensagem m
JOIN usuario r ON m.idRemetente = r.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE d.nome LIKE ? 
"""

EXCLUIR_MENSAGEM_POR_ID = """
DELETE FROM mensagem
WHERE id = ?
"""

ATUALIZAR_MENSAGEM = """
UPDATE mensagem
SET idRemetente = ?, idDestinatario = ?, conteudo = ?, dataEnvio = ?, horaEnvio = ?, visualizacao = ?
WHERE id = ?
"""

ATUALIZAR_VISUALIZACAO_MENSAGEM = """
UPDATE mensagem
SET visualizacao = ?
WHERE id = ?
"""

EXCLUIR_MENSAGEM_POR_NOME_REMETENTE = """
DELETE FROM mensagem
WHERE idRemetente = (
    SELECT id FROM usuario WHERE nome = ?
)
"""

EXCLUIR_MENSAGEM_POR_NOME_DESTINATARIO = """
DELETE FROM mensagem
WHERE idDestinatario = (
    SELECT id FROM usuario WHERE nome = ?
)
"""




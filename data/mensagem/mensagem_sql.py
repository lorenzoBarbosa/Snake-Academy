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

OBTER_MENSAGEMS = """
SELECT 
    id, idRemetente, idDestinatario, conteudo, dataEnvio, horaEnvio, visualizacao  
FROM mensasgem
ORDER BY id ASC
"""

OBTER_MENSAGEM_PAGINADO = """
SELECT
    m.id, m.idRemetente, m.idDestinatario, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao, u.nome as nomeUsuario
FROM mensagem m
JOIN usuario u ON m.idRemetente = u.id
JOIN usuario d ON m.idDestinatario = d.id
ORDER BY m.idRemetente
LIMIT ? OFFSET ?
"""

OBTER_MENSAGEM_POR_TERMO_PAGINADO = """
SELECT
    m.id, m.idRemetente, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao, u.nome as nomeUsuario
FROM mensagem m
JOIN usuario u ON m.idRemetente = u.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE m.id LIKE ? OR u.nome LIKE ? or m.conteudo LIKE ?
ORDER BY m.id_usuario
LIMIT ? OFFSET ?
"""

OBTER_MENSAGEM_POR_ID = """
SELECT 
    m.id, m.idRemetente, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao, u.nome as nomeUsuario
FROM mensagem as m
JOIN usuario as u ON m.idRemetente = u.id
JOIN usuario as d ON m.idDestinatario = d.id
WHERE id = ?
ORDER BY id ASC
"""

OBTER_MENSAGEM_POR_MATRICULA = """
SELECT
    m.id, m.idRemetente, m.conteudo, m.dataEnvio, m.horaEnvio, m.visualizacao, u.nome as nomeUsuario
FROM mensagem m
JOIN usuario u ON m.idRemetente = u.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE u.nome = ?
ORDER BY m.id_usuario
LIMIT ? OFFSET ?
"""

EXCLUIR_MENSAGEM_POR_ID = """
DELETE FROM mensagem
WHERE id = ?
"""

OBTER_QUANTIDADE_MENSAGEMS = """
SELECT COUNT(*) FROM mensagem
"""

OBTER_QUANTIDADE_MENSAGEMS_POR_NOME_USUARIO= """
SELECT COUNT(*)
FROM mensagem m
JOIN usuario u ON m.idRemetente = u.id
JOIN usuario d ON m.idDestinatario = d.id
WHERE u.nome LIKE ? 
"""



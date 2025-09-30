CRIAR_TABELA_BANNER = """
CREATE TABLE IF NOT EXISTS banner (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idAdmin INTEGER NOT NULL,
    status BOOLEAN NOT NULL,
    imagem TEXT NOT NULL,
    FOREIGN KEY (idAdmin) REFERENCES admin(id)
);
"""

INSERIR_BANNER = """
INSERT INTO banner (idAdmin, status, imagem)
VALUES (?, ?, ?);
"""

OBTER_TODOS_BANNERS = """
SELECT * FROM banner;
"""

OBTER_BANNER_POR_ID = """
SELECT * FROM banner
WHERE id = ?;
"""

OBTER_BANNER_PAGINADO = """
SELECT * FROM banner
LIMIT ? OFFSET ?;
"""

ATUALIZAR_BANNER = """
UPDATE banner
SET idAdmin = ?, status = ?, imagem = ?
WHERE id = ?;
"""

DELETAR_BANNER = """
DELETE FROM banner
WHERE id = ?;
"""

ALTERAR_STATUS_BANNER = """
UPDATE banner
SET status = ?
WHERE id = ?;
"""
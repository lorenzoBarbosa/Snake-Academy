CRIAR_TABELA_BANNER = """
CREATE TABLE IF NOT EXISTS banner (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idAdmin INTEGER NOT NULL,
    imagem TEXT NOT NULL,
    status BOOLEAN NOT NULL,
    FOREIGN KEY (idAdmin) REFERENCES admin(id)
);
"""

INSERIR_BANNER = """
INSERT INTO banner (idAdmin, imagem, status)
VALUES (?, ?, ?);
"""

OBTER_TODOS_BANNERS = """
SELECT * FROM banner;
"""

OBTER_BANNER_POR_ID = """
SELECT * FROM banner
WHERE id = ?;
"""

OOBTER_BANNER_PAGINADO = """
SELECT * FROM banner
LIMIT ? OFFSET ?;
"""

ATUALIZAR_BANNER = """
UPDATE banner
SET idAdmin = ?, imagem = ?, status = ?
WHERE id = ?;
"""

DELETAR_BANNER = """
DELETE FROM banner
WHERE id = ?;
"""
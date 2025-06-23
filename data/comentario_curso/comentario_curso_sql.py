CRIAR_TABELA_COMENTARIO_CURSO = """
CREATE TABLE IF NOT EXISTS comentarioCurso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idAdmin INTEGER NOT NULL,
    idMatricula INTEGER NOT NULL,
    conteudo TEXT NOT NULL,
    dataEnvio TEXT NOT NULL,
    dataSupervisaoAdmin TEXT NOT NULL,
    visualizacao BOOLEAN NOT NULL,
    FOREIGN KEY (idAdmin) REFERENCES admin(id),
    FOREIGN KEY (idMatricula) REFERENCES matricula(id)
)
"""

GERAR_COMENTARIO_CURSO = """
INSERT INTO comentarioCurso (idAdmin, idMatricula, conteudo, dataEnvio, dataSupervisaoAdmin, visualizacao)
VALUES (?, ?, ?, ?, ?, ?)
"""

OBTER_COMENTARIO_CURSO = """
SELECT 
    id, idAdmin, idMatricula, conteudo, dataEnvio, dataSupervisaoAdmin, visualizacao  
FROM comentarioCurso
ORDER BY id ASC
"""

OBTER_COMENTARIO_CURSO_PAGINADO = """
SELECT
    cc.id, cc.idAdmin, cc.idMatricula, cc.conteudo, cc.dataEnvio, cc.dataSupervisaoAdmin, cc.visualizacao, a.nome as nomeAdmin
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
ORDER BY cc.id_Admin
LIMIT ? OFFSET ?
"""

OBTER_RCHAMADO_POR_ID = """
SELECT 
    cc.id, cc.idAdmin, cc.idMatricula, cc.conteudo, cc.dataEnvio, cc.dataSupervisaoAdmin, cc.visualizacao, a.nome as nomeAdmin
FROM comentarioCurso as cc
JOIN admin a ON cc.idAdmin = a.id
WHERE id = ?
ORDER BY id ASC
"""

OBTER_QUANTIDADE_RCHAMADOS = """
SELECT COUNT(*) FROM comentarioCurso
"""
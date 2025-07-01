CRIAR_TABELA_COMENTARIO_CURSO = """
CREATE TABLE IF NOT EXISTS comentarioCurso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    idAdmin INTEGER NOT NULL,
    idMatricula INTEGER NOT NULL,
    conteudo TEXT NOT NULL,
    dataEnvio TEXT NOT NULL,
    dataSupervisaoAdmin TEXT NOT NULL,
    FOREIGN KEY (idAdmin) REFERENCES admin(id),
    FOREIGN KEY (idMatricula) REFERENCES matricula(id)
)
"""

GERAR_COMENTARIO_CURSO = """
INSERT INTO comentarioCurso (idAdmin, idMatricula, conteudo, dataEnvio, dataSupervisaoAdmin)
VALUES (?, ?, ?, ?, ?)
"""

OBTER_COMENTARIO_CURSO = """
SELECT 
    cc.id, cc.idAdmin, uu.nome as nomeAdmin, cc.idMatricula, u.nome as nomeMatricula, cc.conteudo, cc.dataEnvio, cc.dataSupervisaoAdmin 
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
JOIN matricula m ON cc.idMatricula = m.id
JOIN cliente c ON m.idCliente = c.id
JOIN usuario u ON c.id = u.id
ORDER BY cc.id ASC
"""
OBTER_COMENTARIO_CURSO_POR_ID = """
SELECT 
    cc.id, cc.idAdmin, uu.nome as nomeAdmin, cc.idMatricula, u.nome as nomeMatricula, cc.conteudo, cc.dataEnvio, cc.dataSupervisaoAdmin  
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
JOIN matricula m ON cc.idMatricula = m.id
JOIN cliente c ON m.idCliente = c.id
JOIN usuario u ON c.id = u.id
WHERE cc.id = ?
ORDER BY cc.id ASC
"""

OBTER_COMENTARIO_CURSO_POR_NOME_ADMIN = """
SELECT 
    cc.id, cc.idAdmin, uu.nome as nomeAdmin, cc.idMatricula, u.nome as nomeMatricula, cc.conteudo, cc.dataEnvio, cc.dataSupervisaoAdmin  
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
JOIN matricula m ON cc.idMatricula = m.id
JOIN cliente c ON m.idCliente = c.id
JOIN usuario u ON c.id = u.id
WHERE uu.nome = ?
ORDER BY cc.id ASC
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_COMENTARIO_CURSO = """
SELECT COUNT(*) FROM comentarioCurso
"""

OBTER_QUANTIDADE_COMENTARIO_CURSO_POR_NOME_ADMIN = """
SELECT COUNT(*)
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
WHERE uu.nome LIKE ?
"""

OBTER_COMENTARIO_CURSO_PAGINADO = """
SELECT
    cc.id, cc.idAdmin, cc.idCMatricula, cc.conteudo, cc.dataEnvio, cc.horaEnvio, uu.nome as nomeAdmin
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
ORDER BY cc.id_Admin
LIMIT ? OFFSET ?
"""

OBTER_COMENTARIO_CURSO_POR_TERMO_PAGINADO = """
SELECT
   cc.id,cc.idAdmin, cc.idcchamado, cc.desccriccao, cc.dataEnvio, cc.horaEnvio, uu.nome as nomeAdmin
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
WHERE cc.id LIKE ? OR uu.nome LIKE ? or cc.conteudo LIKE ?
ORDER BY cc.id_Admin
LIMIT ? OFFSET ?
"""

OBTER_COMENTARIO_CURSO_POR_ID = """
SELECT 
    cc.id, cc.idAdmin, cc.idMatricula, cc.conteudo, cc.dataEnvio, cc.dataSupervisaoAdmin, uu.nome as nomeAdmin
FROM comentarioCurso as cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
WHERE cc.id = ?
ORDER BY cc.id ASC
"""

OBTER_COMENTARIO_CURSO_POR_NOME_ADMIN = """
SELECT
    cc.id, cc.idAdmin, cc.idMatricula, cc.coneteudo, cc.dataEnvio, cc.dataSupervisaoAdmin, uu.nome as nomeAdmin
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
WHERE uu.nome = ?
ORDER BY cc.idAdmin
LIMIT ? OFFSET ?
"""

EXCLUIR_COMENTARIO_CURSO_POR_ID = """
DELETE FROM comentarioCurso
WHERE id = ?
"""

OBTER_QUANTIDADE_COMENTARIO_CURSO = """
SELECT COUNT(*) FROM respostaChamado
"""

OBTER_QUANTIDADE_COMENTARIO_CURSO_POR_NOME_ADMIN= """
SELECT COUNT(*)
FROM respostaChamado c
JOIN admin a ON c.idUsuario = a.id
WHERE uu.nome LIKE ? 
"""

OBTER_COMENTARIO_CURSO_POR_ID_CHAMADO= """
SELECT 
    cc.id, cc.idAdmin, cc.idChamado, cc.conteudo, cc.dataEnvio, c.dataSupervisaoAdmin, uu.nome as nomeAdmin
FROM comentarioCurso cc
JOIN admin a ON cc.idAdmin = a.id
JOIN usuario uu ON a.id = uu.id
WHERE cc.idChamado = ?
ORDER BY c.id_admin
LIMIT ? OFFSET ?
"""




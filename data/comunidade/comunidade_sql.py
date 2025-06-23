CRIAR_TABELA_COMUNIDADE = """
CREATE TABLE IF NOT EXISTS Comunidade (
    idComunidade INTEGER PRIMARY KEY AUTOINCREMENT,
    idCurso INTEGER NOT NULL,
    quantidadeParticipantes INTEGER NOT NULL,
    listaParticipantes TEXT NOT NULL, 
    FOREIGN KEY (idCurso) REFERENCES curso(id),
)
"""

#no listaParticipantes eu vi que não pode ser uma lista depois rever isso, deixei como text not null. Teria que fazer outra tabela relacional

GERAR_COMUNIDADE = """
INSERT INTO Comunidade (idCurso, quantidadeParticipantes, listaParticipantes)
VALUES (?, ?, ?,)
"""

OBTER_COMENTARIO_CURSO = """
SELECT 
    idComunidade, idCurso, quantidadeParticipantes, listaParticipantes
FROM Comunidade
ORDER BY id ASC
"""

OBTER_COMUNIDADE_POR_TERMO_PAGINADO = """
SELECT 
    com.idComunidade, com.idCurso, com.quantidadeParticipantes, listaParticipantes
FROM Comunidade com
JOIN curso c ON com.idCurso = c.id
WHERE (com.idComunidade LIKE ? OR c.idCurso LIKE ?)
ORDER BY com.id
LIMIT ? OFFSET ?
"""

EXCLUIR_COMUNIDADE_POR_ID = """
DELETE FROM comunidade WHERE id = ?
"""
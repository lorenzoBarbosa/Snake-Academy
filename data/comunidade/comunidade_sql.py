CRIAR_TABELA_COMUNIDADE = """(
    id INTEGER PRIMARY KEY,
    idCurso INTEGER NOT NULL,),
    nome TEXT NOT NULL,
    quantidadeParticipantes INTEGER,
    listaParticipantes TEXT[],
    FOREIGN KEY (idCurso) REFERENCES curso(id)
)"""

INSERIR_COMUNIDADE = """
INSERT INTO comunidade (idCurso, nome, quantidadeParticipantes, listaParticipantes)
VALUES (?, ?, ?, ?)
"""

OBTER_COMUNIDADE = """
SELECT 
    co.id, co.idCurso, c.nome as nomeCurso, co.nome, co.quantidadeParticipantes, co.listaParticipantes
FROM comunidade co
JOIN curso c ON co.idCurso = c.id
ORDER BY id 
"""

OBTER_COMUNIDADES_PAGINADO = """
SELECT 
    co.id, co.idCurso, c.nome as nomeCurso, co.nome, co.quantidadeParticipantes, co.listaParticipantes
FROM comunidade co
JOIN curso c ON co.idCurso = c.id
ORDER BY id
LIMIT ? OFFSET ?
"""

OBTER_COMUNIDADE_POR_ID = """
SELECT 
    co.id, co.idCurso, c.nome as nomeCurso, co.nome, co.quantidadeParticipantes, co.listaParticipantes
FROM comunidade co
JOIN curso c ON co.idCurso = c.id
WHERE co.id = ?;
"""
OBTER_COMUNIDADE_POR_NOME_CURSO = """
SELECT 
    co.id, co.idCurso, c.nome as nomeCurso, co.nome, co.quantidadeParticipantes, co.listaParticipantes
FROM comunidade co
JOIN curso c ON co.idCurso = c.id
WHERE c.nome = ?;
"""
OBTER_COMUNIDADE_POR_TERMO_PAGINADO = """
SELECT 
    co.id, co.idCurso, c.nome as nomeCurso, co.nome, co.quantidadeParticipantes, co.listaParticipantes
FROM comunidade co
JOIN curso c ON co.idCurso = c.id
WHERE (c.nome LIKE ? OR co.listaParticipantes LIKE ?)
ORDER BY co.id
LIMIT ? OFFSET ?
"""

OBTER_QUANTIDADE_COMUNIDADES = """
SELECT COUNT(*) FROM comunidade 
"""

OBTER_QUANTIDADE_COMUNIDADES_POR_NOME_CURSO = """
SELECT COUNT(*) FROM comunidade co
JOIN curso c ON co.idCurso = c.id
WHERE c.nome = ?
"""

ATUALIZAR_COMUNIDADE = """
UPDATE comunidade
SET idCurso = ?, quantidadeParticipantes = ?, listaParticipantes = ?
WHERE id = ?;
"""

EXCLUIR_COMUNIDADE_POR_ID = """
DELETE FROM comunidade
WHERE id = ?;
"""


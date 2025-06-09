from dataclasses import dataclass


@dataclass
class Cliente:
    id: int
    nome: str
    email: str
    senha: str
    telefone: str
    dataCriacao: str
    dataUltimoAcesso: str
    statusConta: bool
    historicoCursos: list
    indentificacaoProfessor: bool
from dataclasses import dataclass


@dataclass
class Progresso:
    id: int
    idAula: int
    idMatricula: int
    dataInicio: str
    dataFim: str
    statusAula: str
    porcentagemConclusao: float

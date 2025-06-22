from dataclasses import dataclass
from data.professor.professor_model import Professor


@dataclass
class Curso:
    id: int
    nome: str
    idProfessor: Professor
    custo: float
    descricaoCurso: str
    duracaoCurso: str
    avaliacao: str
    dataCriacao: str
    statusCurso: bool

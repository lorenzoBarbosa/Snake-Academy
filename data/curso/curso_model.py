from dataclasses import dataclass
from typing import Optional
from data.professor.professor_model import Professor


@dataclass
class Curso:
    id: int
    nome: str
    idProfessor: int
    custo: float
    descricaoCurso: str
    duracaoCurso: str
    avaliacao: str
    dataCriacao: str
    statusCurso: bool
    professor: Optional[Professor] = None
    
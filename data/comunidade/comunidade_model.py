from dataclasses import dataclass
from data.curso.curso_model import Curso


@dataclass
class Comunidade:
    idCurso: Curso
    nome: str
    quantidadeParticipantes: int
    listaParticipantes: list
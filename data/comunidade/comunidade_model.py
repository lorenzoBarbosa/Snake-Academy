from dataclasses import dataclass
from typing import Optional
from data.curso.curso_model import Curso


@dataclass
class Comunidade:
    id: int
    idCurso: Curso
    nome: str
    quantidadeParticipantes: int
    listaParticipantes: list
    nomeCurso: Optional[Curso] = None

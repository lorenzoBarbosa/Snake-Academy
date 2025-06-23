from dataclasses import dataclass
from data.curso.curso_model import id


@dataclass
class Comunidade:
    idComunidade: int
    idCurso: id
    quantidade_participantes: int
    listaParticipantes: list
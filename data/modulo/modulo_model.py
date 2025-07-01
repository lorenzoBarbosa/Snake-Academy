from dataclasses import dataclass
from typing import Optional

from data.curso.curso_model import Curso


@dataclass
class Modulo():
    id: int
    idCurso: int
    titulo: str
    descricaoModulo: str
    listaAulas: list
    listaExercicios: list
    curso: Optional[Curso] = None

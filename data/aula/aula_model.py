from dataclasses import dataclass
from typing import Optional

from data.modulo.modulo_model import Modulo


@dataclass
class Aula:
    id: int
    idModulo: int
    titulo: str
    descricaoAula: str
    duracaoAula: str
    url: str
    videoId: str
    dataDisponibilidade: str
    status: int
    modulo: Optional[Modulo] = None
    nomeCurso: Optional[str] = None

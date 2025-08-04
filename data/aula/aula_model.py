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
    tipo: str
    ordem: int
    dataDisponibilidade: str
    modulo: Optional[Modulo] = None
    nomeCurso: Optional[str] = None

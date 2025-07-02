from dataclasses import dataclass
from typing import Optional

from data.aula.aula_model import Aula
from data.matricula.matricula_model import Matricula


@dataclass
class Progresso:
    id: int
    idAula: int
    idMatricula: int
    dataInicio: str
    dataFim: str
    statusAula: str
    porcentagemConclusao: float
    aula: Optional[Aula] = None
    matricula: Optional[Matricula] = None

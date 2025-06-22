from dataclasses import dataclass
from data.cliente.cliente_model import Cliente


@dataclass
class Matricula(Cliente):
    idMatricula: int
    idCurso: int
    statusMatricula: str
    desempenho: str
    frequencia: str
    dataMatricula: str



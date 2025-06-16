from dataclasses import dataclass
from data.cliente.cliente_model import Cliente


@dataclass
class matricula(Cliente):
    idMatricula: int
    statusMatricula: str
    desempenho: str
    frequencia: str
    dataMatricula: str



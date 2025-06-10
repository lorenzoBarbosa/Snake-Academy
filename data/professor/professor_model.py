from dataclasses import dataclass
from data.cliente.cliente_model import Cliente


@dataclass
class Professor(Cliente):
    cursosPostados: list
    quantidadeAlunos: int
    dataCriacaoProfessor: str

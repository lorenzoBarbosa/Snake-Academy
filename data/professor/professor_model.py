from dataclasses import dataclass
from typing import Optional
from data.cliente.cliente_model import Cliente


@dataclass
class Professor(Cliente):
    cursosPostados: list
    quantidadeAlunos: int
    dataCriacaoProfessor: str
    descricaoProfessor: Optional[str] = None

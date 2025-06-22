from dataclasses import dataclass


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


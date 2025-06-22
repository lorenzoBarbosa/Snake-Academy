from dataclasses import dataclass


@dataclass
class Modulo():
    id: int
    idCurso: int
    titulo: str
    descricaoModulo: str
    listaAulas: list
    listaExercicios: list

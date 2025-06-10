from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass
class Cliente(Usuario):
    dataUltimoAcesso: str
    statusConta: bool
    historicoCursos: list
    indentificacaoProfessor: bool
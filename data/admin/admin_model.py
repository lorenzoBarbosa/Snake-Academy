from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass
class Admin(Usuario):
    nivelAcesso: int

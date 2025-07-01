from typing import Optional
from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass
class Admin():
    nivelAcesso: int
    usuario: Optional[Usuario] = None
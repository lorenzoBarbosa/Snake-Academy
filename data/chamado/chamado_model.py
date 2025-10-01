from dataclasses import dataclass
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Chamado:
    id: int
    idUsuario: int
    descricao: str
    dataEnvio: str
    horaEnvio: str
    visualizacao: bool
    tipo: str
    usuario: Optional[Usuario] = None
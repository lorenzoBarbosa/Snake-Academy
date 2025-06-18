from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass
class Chamado:
    id: int
    idUsuario: Usuario
    descricao: str
    dataEnvio: str
    horaEnvio: str
    visualizacao: bool
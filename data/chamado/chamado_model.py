from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass
class Chamado:
    id: int
    descricao: str
    dataEnvio: str
    horaEnvio: str
    visualizacao: bool
    idUsuario: Usuario[0]
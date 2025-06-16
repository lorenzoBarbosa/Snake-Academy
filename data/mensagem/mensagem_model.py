from dataclasses import dataclass
from data.usuario.usuario_model import Usuario


@dataclass
class Mensagem:
    id: int
    conteudo: str
    dataEnvio: str
    horaEnvio: str
    visualizacao: bool
    #inacabado
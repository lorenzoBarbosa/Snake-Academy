from dataclasses import dataclass
from typing import Optional
from data.usuario.usuario_model import Usuario


@dataclass
class Mensagem:
    id: int
    idRmetente: int
    idDestinatario: int
    conteudo: str
    dataEnvio: str
    horaEnvio: str
    visualizacao: bool
    remetente: Optional[Usuario] =  None
    destinatario: Optional[Usuario] = None
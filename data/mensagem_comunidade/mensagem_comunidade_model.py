from dataclasses import dataclass

from data.comunidade.comunidade_model import Comunidade
from data.matricula.matricula_model import Matricula


@dataclass
class MensagemComunidade():
    id: int
    idMatricula: int
    idComunidade: int
    conteudo: str
    dataEnvio: str
    horaEnvio: str
    visualizacao: bool


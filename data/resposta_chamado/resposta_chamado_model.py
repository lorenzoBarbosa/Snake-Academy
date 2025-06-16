from dataclasses import dataclass
from data.admin.admin_model import Admin


@dataclass
class resposta_chamado:
    Id: int
    feedback: str
    dataEnvio: str
    visualizacao: bool
    horaEnvio: str
    idAdmin: Admin[0]
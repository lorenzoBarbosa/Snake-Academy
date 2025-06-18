from dataclasses import dataclass
from data.admin.admin_model import Admin
from data.chamado.chamado_model import Chamado


@dataclass
class respostaChamado:
    id: int
    idAdmin: Admin
    idChamado: Chamado
    descricao: str
    dataEnvio: str
    horaEnvio: str
    visualizacao: bool
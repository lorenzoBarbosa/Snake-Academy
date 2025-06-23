from dataclasses import dataclass
from data.admin.admin_model import Admin
from data.matricula.matricula_model import matricula

@dataclass

class comentarioCurso:
    id: int
    idAdmin: Admin
    idMatricula: matricula
    conteudo: str
    dataEnvio: str
    dataSupervisaoAdmin: str
    visualizacao: bool
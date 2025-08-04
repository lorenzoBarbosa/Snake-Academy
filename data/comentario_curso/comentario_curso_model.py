from dataclasses import dataclass
from data.admin.admin_model import Admin
from data.matricula.matricula_model import Matricula

@dataclass

class comentarioCurso:
    id: int
    idAdmin: int
    idMatricula: int
    conteudo: str
    dataEnvio: str
    dataSupervisaoAdmin: str
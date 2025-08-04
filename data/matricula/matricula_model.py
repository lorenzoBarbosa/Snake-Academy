from dataclasses import dataclass
from typing import Optional
from data.cliente.cliente_model import Cliente
from data.curso.curso_model import Curso
from data.usuario.usuario_model import Usuario


@dataclass
class Matricula():
    idMatricula: int
    idCliente: int
    idCurso: int
    statusMatricula: str
    desempenho: str
    frequencia: str
    dataMatricula: str
    curso: Optional[Curso] = None
    usuario: Optional[Usuario] = None



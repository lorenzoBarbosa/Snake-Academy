from dataclasses import dataclass
from typing import Optional
from data.categoria.categoria_model import Categoria


@dataclass
class Topico:
    id: int
    nome: str
    idCategoria: int
    categoria: Optional[Categoria] = None

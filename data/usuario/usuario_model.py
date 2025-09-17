from dataclasses import dataclass
from typing import Optional


@dataclass
class Usuario:
    id: int
    nome: str
    email: str
    senha: str
    telefone: str
    dataNascimento: str
    perfil: str
    token_redefinicao: Optional[str]
    data_token: Optional[str]
    data_cadastro: Optional[str]
    foto: Optional[str] 


from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    nome: str
    email: str
    senha: str
    telefone: str
    dataCriacao: str

    @classmethod  #criei esse metódo para simplifcar em chamado_repo, no caso para eu pegar só o id
    def somente_id(cls, id: int):
        return cls(
            id=id,
            nome="",
            email="",
            senha="",
            telefone="",
            dataCriacao=""
        )
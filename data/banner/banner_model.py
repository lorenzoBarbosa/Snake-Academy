from dataclasses import dataclass


@dataclass
class Banner:
    id: int
    idAdmin: int
    imagem: str
    status: bool
    
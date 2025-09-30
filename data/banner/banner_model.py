from dataclasses import dataclass
from typing import Optional


@dataclass
class Banner:
    id: int
    idAdmin: int
    status: bool
    imagem: Optional[str]
    
from dataclasses import dataclass


@dataclass
class Banner:
    id: int
    idAdmin: int
    status: bool
    
from pydantic import BaseModel, field_validator


class InserirTopicoDTO(BaseModel):
    nome: str
    idCategoria: int

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 3:
            raise ValueError("O nome do tópico deve ter pelo menos 3 caracteres.")
        if len(v) > 100:
            raise ValueError("O nome do tópico deve ter no máximo 100 caracteres.")
        return v

    @field_validator("idCategoria")
    @classmethod
    def validar_categoria(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Selecione uma categoria válida.")
        return v


class AtualizarTopicoDTO(BaseModel):
    nome: str
    idCategoria: int

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, v: str) -> str:
        v = v.strip()
        if len(v) < 3:
            raise ValueError("O nome do tópico deve ter pelo menos 3 caracteres.")
        if len(v) > 100:
            raise ValueError("O nome do tópico deve ter no máximo 100 caracteres.")
        return v

    @field_validator("idCategoria")
    @classmethod
    def validar_categoria(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Selecione uma categoria válida.")
        return v
"""
DTOs relacionados a usuários.
Agrupa todas as validações e estruturas de dados para operações com usuários.
"""

from pydantic import EmailStr, Field, field_validator
from typing import Optional
from .base_dto import BaseDTO
from util.validacoes_dto import *


class InserirCategoriaDTO(BaseDTO):

    nome: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Nome completo da categoria"
    )
    

    @field_validator('nome')
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        validar_texto_obrigatorio(valor, "Nome", min_chars=2, max_chars=100)
        return valor


class AtualizarCategoriaDTO(BaseDTO):
    """
    DTO para atualização de dados da categoria.
    Campos opcionais para atualização parcial.
    """

    nome: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description="Nome completo"
    )


    @field_validator('nome')
    @classmethod
    def validar_nome(cls, v: Optional[str]) -> Optional[str]:
        if v is not None:
            validar_texto_obrigatorio(v, "Nome", min_chars=2, max_chars=100)
        return v



# Configurar exemplos JSON nos model_config
InserirCategoriaDTO.model_config.update({
    "json_schema_extra": {
        "example": InserirCategoriaDTO.criar_exemplo_json()
    }
})
"""
DTOs relacionados a usuários.
Agrupa todas as validações e estruturas de dados para operações com usuários.
"""

from pydantic import EmailStr, Field, field_validator
from typing import Optional
from .base_dto import BaseDTO
from util.validacoes_dto import *


class InserirUsuarioDTO(BaseDTO):

    nome: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Nome completo do usuário"
    )
    email: EmailStr = Field(
        ...,
        description="E-mail válido do usuário"
    )
    telefone: str = Field(
        ...,
        min_length=10,
        description="Telefone com DDD"
    )
    senha: str = Field(
        ...,
        min_length=6,
        max_length=100,
        description="Senha do usuário"
    )
    confirmar_senha: str = Field(
        ...,
        min_length=6,
        max_length=100,
        description="Confirmação da senha do usuário"
    )

    @field_validator('senha')
    @classmethod
    def validar_senha(cls, v: str) -> str:
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_senha(
                valor, campo, min_chars=6, max_chars=100
            ),
            "Senha"
        )
        return validador(v)

    @field_validator('confirmar_senha')
    @classmethod
    def senhas_devem_coincidir(cls, v, info):
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_senhas_coincidem(
                valor, info.data.get('senha'), campo
            ),
            "Confirmar Senha"
        )
        return validador(v)

    @field_validator('nome')
    @classmethod
    def validar_nome(cls, v: str) -> str:
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_texto_obrigatorio(
                valor, campo, min_chars=2, max_chars=100
            ),
            "Nome"
        )
        return validador(v)
    
    @field_validator('email')
    @classmethod
    def validar_email(cls, v: str) -> str:
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_texto_obrigatorio(
                valor, campo, min_chars=5, max_chars=100
            ),
            "Email"
        )
        return validador(v)

    @field_validator('telefone')
    @classmethod
    def validar_telefone_campo(cls, v: str) -> str:
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_telefone(valor),
            "Telefone"
        )
        return validador(v)


class AtualizarUsuarioDTO(BaseDTO):
    """
    DTO para atualização de dados do usuário.
    Campos opcionais para atualização parcial.
    """

    nome: Optional[str] = Field(
        None,
        min_length=2,
        max_length=100,
        description="Nome completo"
    )
    telefone: Optional[str] = Field(
        None,
        description="Telefone"
    )

    @field_validator('nome')
    @classmethod
    def validar_nome(cls, v: Optional[str]) -> Optional[str]:
        if not v:
            return v
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_texto_obrigatorio(
                valor, campo, min_chars=2, max_chars=100
            ),
            "Nome"
        )
        return validador(v)

    @field_validator('telefone')
    @classmethod
    def validar_telefone_campo(cls, v: Optional[str]) -> Optional[str]:
        if not v:
            return v
        validador = cls.validar_campo_wrapper(
            lambda valor, campo: validar_telefone(valor),
            "Telefone"
        )
        return validador(v)


# Configurar exemplos JSON nos model_config
InserirUsuarioDTO.model_config.update({
    "json_schema_extra": {
        "example": InserirUsuarioDTO.criar_exemplo_json()
    }
})
from pydantic import BaseModel, field_validator

from dtos.validacoes_dto import validar_texto_obrigatorio


class chamadoDTO (BaseModel):
   idUsuario: int
   descricao: str

   @field_validator("descricao")
   @classmethod
   def validar_chamado(cls, descricao):
       descricao_validada = validar_texto_obrigatorio(descricao, "Descrição", min_chars=10, max_chars=500)
       return descricao_validada

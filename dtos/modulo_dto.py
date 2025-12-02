from pydantic import BaseModel, field_validator

from data.topico.topico_repo import obter_topico_por_id
from util.validacoes_dto import validar_texto_obrigatorio, validar_titulo, validar_valor_monetario


class ModuloDTO(BaseModel):
    titulo: str
    descricao: str

    @field_validator("titulo")
    def validar_titulo_curso(cls, titulo):
        return validar_titulo(titulo)
    
    @field_validator("descricao")
    def validar_descricao_curso(cls, descricao):
        return validar_texto_obrigatorio(descricao, campo="Descrição do curso", min_chars=10, max_chars=1000)
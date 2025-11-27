from pydantic import BaseModel, field_validator

from data.topico.topico_repo import obter_topico_por_id
from util.validacoes_dto import validar_texto_obrigatorio, validar_titulo, validar_valor_monetario


class CursoDTO(BaseModel):
    titulo: str
    custo: float
    descricao: str
    topico_id: int

    @field_validator("titulo")
    def validar_titulo_curso(cls, titulo):
        return validar_titulo(titulo)
    
    @field_validator("custo")
    def validar_custo(cls, custo):
        return validar_valor_monetario(custo, campo="Custo do curso", obrigatorio=True, min_valor=0)
    
    @field_validator("descricao")
    def validar_descricao_curso(cls, descricao):
        return validar_texto_obrigatorio(descricao, campo="Descrição do curso", min_chars=10, max_chars=1000)

    @field_validator("topico_id")
    def validar_topico_id(cls, topico_id):
        if topico_id is None or topico_id <= 0:
            raise ValueError("O campo topico_id deve ser um ID válido.")
        
        topico = obter_topico_por_id(topico_id)
        if not topico:
            raise ValueError("O tópico especificado não existe.")
        return topico_id

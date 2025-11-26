from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Optional

class VideoBase(BaseModel):
    titulo: str = Field(..., max_length=255, description="Título do vídeo")
    descricao: Optional[str] = Field(None, description="Descrição do vídeo")
    youtube_url: str = Field(..., description="URL do YouTube")

class VideoCreate(VideoBase):
    pass

class VideoResponse(VideoBase):
    id: int
    youtube_video_id: str
    usuario_id: Optional[int]
    data_criacao: datetime
    visualizacoes: int
    ativo: bool
    
    class Config:
        from_attributes = True

class VideoUpdate(BaseModel):
    titulo: Optional[str] = Field(None, max_length=255)
    descricao: Optional[str] = None
    youtube_url: Optional[str] = None
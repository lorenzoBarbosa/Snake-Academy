import re
from urllib.parse import urlparse, parse_qs

def extrair_video_id(url: str) -> str | None:
    """
    Extrai o ID do vídeo de diferentes formatos de URL do YouTube
    
    Formatos suportados:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    """
    
    padroes = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/watch\?.*v=([a-zA-Z0-9_-]{11})',
    ]
    
    for padrao in padroes:
        match = re.search(padrao, url)
        if match:
            return match.group(1)
    
    return None

def validar_url_youtube(url: str) -> bool:
    """
    Valida se a URL é do YouTube
    """
    dominios_validos = ['youtube.com', 'youtu.be', 'www.youtube.com']
    
    try:
        parsed = urlparse(url)
        return parsed.netloc in dominios_validos
    except:
        return False

def gerar_url_embed(video_id: str) -> str:
    """
    Gera URL de embed a partir do video_id
    """
    return f"https://www.youtube.com/embed/{video_id}"
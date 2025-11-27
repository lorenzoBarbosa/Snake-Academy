from fastapi import APIRouter,  Depends, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List

from data.aula.aula_model import Aula
from data.aula.aula_repo import *
from dtos.aula_dto import *
from util.video_helper import extrair_video_id, validar_url_youtube, gerar_url_embed


templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/criar-curso/criar-modulo")
@requer_autenticacao(["professor"])
async def get_criar_modulo(request: Request, usuario_logado: dict = None):
    usuario_logado["indentificacaoProfessor"] = True
    response = templates.TemplateResponse("professor/cursos/criar_modulo.html", {"request": request, "usuario": usuario_logado})
    return response

@router.get("/professor/cursos/criar-curso/criar-aula")
@requer_autenticacao(["professor"])
async def get_criar_aula(request: Request, usuario_logado: dict = None):
    usuario_logado["indentificacaoProfessor"] = True
    aulas = obter_aula_paginada_por_modulo(1, 10)
    response = templates.TemplateResponse("professor/cursos/criar_aula.html", {"request": request, "usuario": usuario_logado})
    return response


@router.post("/professor/cursos/criar-curso/criar-aula")
async def upload_video(
    request: Request,
    titulo: str = Form(...),
    descricao: str = Form(None),
    youtube_url: str = Form(...),
    usuario_logado: dict = None
):
    """Processa upload de vídeo"""
    
    # Validações
    if not validar_url_youtube(youtube_url):
        return templates.TemplateResponse(
            "videos/upload.html",
            {
                "request": request,
                "error": "URL inválida! Use uma URL do YouTube."
            }
        )
    
    video_id = extrair_video_id(youtube_url)
    
    if not video_id:
        return templates.TemplateResponse(
            "videos/upload.html",
            {
                "request": request,
                "error": "Não foi possível extrair o ID do vídeo. Verifique a URL."
            }
        )
    
    # Criar registro no banco
    novo_video = Aula(
        titulo=titulo,
        descricao=descricao,
        url=youtube_url,
        youtube_video_id=video_id,
        usuario_id=usuario_logado["id"],
    )
    
    try:
        inserir_aula(novo_video)
        return RedirectResponse(url="/videos/lista", status_code=303)
    except Exception as e:
        return templates.TemplateResponse(
            "videos/upload.html",
            {
                "request": request,
                "error": f"Erro ao cadastrar vídeo: {str(e)}"
            }
        )

@router.post("/professor/cursos/criar-curso/criar-modulo/deletar-aula/{video_id}")
async def deletar_video(request: Request, video_id: int, usuario_logado: dict = None):
    """Soft delete do vídeo"""
    video = obter_aula_por_id(video_id)
    
    if not video:
        raise HTTPException(status_code=404, detail="Vídeo não encontrado")
    
    video.status = False
    atualizar_aula_por_id(video)
    
    return RedirectResponse(url="/videos/lista", status_code=303)


@router.get("/player/{video_id}", response_class=HTMLResponse)
async def player(video_id: int, request: Request, usuario_logado: dict = None):
    """Player individual do vídeo"""
    video = obter_aula_por_id(video_id)
    
    if not video:
        raise HTTPException(status_code=404, detail="Vídeo não encontrado")
    
    embed_url = gerar_url_embed(video.videoId)
    
    return templates.TemplateResponse(
        "videos/player.html",
        {"request": request, "video": video, "embed_url": embed_url}
    )
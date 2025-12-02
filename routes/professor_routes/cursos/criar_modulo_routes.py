from fastapi import APIRouter,  Depends, HTTPException, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError


from data.modulo.modulo_model import Modulo
from data.modulo.modulo_repo import inserir_modulo, obter_todos_modulos
from dtos.modulo_dto import ModuloDTO
from util.auth_decorator import *
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List

from data.aula.aula_model import Aula
from data.aula.aula_repo import *
from dtos.aula_dto import *
from util.flash_messages import get_flashed_messages, informar_sucesso
from util.video_helper import extrair_video_id, validar_url_youtube, gerar_url_embed


templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/criar-curso/{curso_id}/criar-modulo")
@requer_autenticacao(["professor"])
async def get_criar_modulo(request: Request, curso_id: int, usuario_logado: dict = None):
    usuario_logado["indentificacaoProfessor"] = True
    mensagens = get_flashed_messages(request)
    response = templates.TemplateResponse("professor/cursos/criar_modulo.html", {"request": request, "usuario": usuario_logado, "mensagens": mensagens})
    return response

@router.post("/professor/cursos/criar-curso/{curso_id}/criar-modulo")
@requer_autenticacao(["professor"])
async def post_criar_modulo(request: Request, 
                            curso_id: int,
                            usuario_logado: dict = None,
                            titulo: str = Form(...),
                            descricao: str = Form(...)):
    
    usuario_logado["indentificacaoProfessor"] = True
    dados = {
        "titulo": titulo,
        "descricao": descricao}
    
    try:
        modulo_dto = ModuloDTO(
            titulo=titulo,
            descricao=descricao
        )
        modulo= Modulo(
            id=0,
            idCurso=curso_id,
            titulo=modulo_dto.titulo,
            descricao=modulo_dto.descricao,
            listaAulas=None,
            listaExercicios=None
        )
        modulo_id= inserir_modulo(modulo)
        informar_sucesso(request, "Módulo salvo com sucesso")

        return RedirectResponse(url=f"/professor/cursos/criar-curso/{modulo.id}/criar-aula")
    except ValidationError as v:
        erros = []
        for err in v.errors():
            campo = err['loc'][0]
            mensagem = err['msg']
            erros[campo.upper()] = mensagem

        return templates.TemplateResponse(
            "professor/cursos/criar_modulo.html",
            {
                "request": request,
                "usuario": usuario_logado,
                "dados": dados,
                "erros": erros
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "professor/cursos/criar_curso.html",
            {
                "request": request,
                "usuario": usuario_logado,
                "dados": dados,
                "erros": {"GERAL": f"Ocorreu um erro ao criar o módulo: {str(e)}"}
            }
        )
    
    
    usuario_logado["indentificacaoProfessor"] = True


@router.get("/professor/cursos/criar-curso/criar-aula")
@requer_autenticacao(["professor"])
async def get_criar_aula(request: Request, usuario_logado: dict = None):
    usuario_logado["indentificacaoProfessor"] = True
    modulos = obter_todos_modulos()
    if modulos:
        aulas = obter_aula_paginada_por_modulo(1, 10, 1)
    else:
        aulas = None
        
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
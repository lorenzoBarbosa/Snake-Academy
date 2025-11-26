# from fastapi import APIRouter,  Depends, HTTPException, Request, Form
# from fastapi.templating import Jinja2Templates

# from util.auth_decorator import *
# from fastapi.responses import HTMLResponse, RedirectResponse
# from fastapi.templating import Jinja2Templates
# from typing import List

# from data.aula.aula_model import Aula
# from data.aula.aula_repo import *
# from dtos.aula_dto import *
# from util.video_helper import extrair_video_id, validar_url_youtube, gerar_url_embed


# templates = Jinja2Templates(directory="templates")
# router = APIRouter()

# @router.get("/professor/cursos/criar-curso/criar-modulo")
# @requer_autenticacao(["professor"])
# async def get_criar_modulo(request: Request, usuario_logado: dict = None):
#     usuario_logado["indentificacaoProfessor"] = True
#     response = templates.TemplateResponse("professor/cursos/criar_modulo.html", {"request": request, "usuario": usuario_logado})
#     return response

# @router.get("/professor/cursos/criar-curso/criar-aula")
# @requer_autenticacao(["professor"])
# async def get_criar_aula(request: Request, usuario_logado: dict = None):
#     usuario_logado["indentificacaoProfessor"] = True
#     aulas = obter_aula_paginada_por_modulo(1, 10)
#     response = templates.TemplateResponse("professor/cursos/criar_aula.html", {"request": request, "usuario": usuario_logado})
#     return response


# @router.post("/professor/cursos/criar-curso/criar-aula")
# async def upload_video(
#     request: Request,
#     titulo: str = Form(...),
#     descricao: str = Form(None),
#     youtube_url: str = Form(...),
#     usuario_logado: dict = None
# ):
#     """Processa upload de vídeo"""
    
#     # Validações
#     if not validar_url_youtube(youtube_url):
#         return templates.TemplateResponse(
#             "videos/upload.html",
#             {
#                 "request": request,
#                 "error": "URL inválida! Use uma URL do YouTube."
#             }
#         )
    
#     video_id = extrair_video_id(youtube_url)
    
#     if not video_id:
#         return templates.TemplateResponse(
#             "videos/upload.html",
#             {
#                 "request": request,
#                 "error": "Não foi possível extrair o ID do vídeo. Verifique a URL."
#             }
#         )
    
#     # Criar registro no banco
#     novo_video = Aula(
#         titulo=titulo,
#         descricao=descricao,
#         url=youtube_url,
#         youtube_video_id=video_id,
#         usuario_id=usuario_logado["id"],
#     )
    
#     try:
#         inserir_aula(novo_video)
#         return RedirectResponse(url="/videos/lista", status_code=303)
#     except Exception as e:
#         return templates.TemplateResponse(
#             "videos/upload.html",
#             {
#                 "request": request,
#                 "error": f"Erro ao cadastrar vídeo: {str(e)}"
#             }
#         )


# @router.get("/player/{video_id}", response_class=HTMLResponse)
# async def player(video_id: int, request: Request, db: Session = Depends(get_db)):
#     """Player individual do vídeo"""
#     video = db.query(Video).filter(Video.id == video_id).first()
    
#     if not video:
#         raise HTTPException(status_code=404, detail="Vídeo não encontrado")
    
#     # Incrementar visualizações
#     video.visualizacoes += 1
#     db.commit()
    
#     embed_url = gerar_url_embed(video.youtube_video_id)
    
#     return templates.TemplateResponse(
#         "videos/player.html",
#         {"request": request, "video": video, "embed_url": embed_url}
#     )

# @router.post("/deletar/{video_id}")
# async def deletar_video(video_id: int, db: Session = Depends(get_db)):
#     """Soft delete do vídeo"""
#     video = db.query(Video).filter(Video.id == video_id).first()
    
#     if not video:
#         raise HTTPException(status_code=404, detail="Vídeo não encontrado")
    
#     video.ativo = False
#     db.commit()
    
#     return RedirectResponse(url="/videos/lista", status_code=303)

# # ===== ROTAS API (JSON) - Opcionais =====

# @router.get("/api/videos", response_model=List[VideoResponse])
# async def api_lista_videos(db: Session = Depends(get_db)):
#     """API: Retorna lista de vídeos em JSON"""
#     videos = db.query(Video).filter(Video.ativo == True).order_by(Video.data_criacao.desc()).all()
#     return videos

# @router.get("/api/videos/{video_id}", response_model=VideoResponse)
# async def api_get_video(video_id: int, db: Session = Depends(get_db)):
#     """API: Retorna um vídeo específico"""
#     video = db.query(Video).filter(Video.id == video_id).first()
#     if not video:
#         raise HTTPException(status_code=404, detail="Vídeo não encontrado")
#     return video


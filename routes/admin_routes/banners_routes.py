from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.banner.banner_repo import *
from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/banners")
@requer_autenticacao(["admin"])
async def get_banners(request:Request, usuario_logado: dict = None):
    banners = obter_todos_banners()
    response = templates.TemplateResponse("admin/banners/banners.html", {"request": request, "usuario": usuario_logado, "banners": banners})
    return response

@router.post("/admin/banners/alterar-vizualizacao/{id_banner}")
@requer_autenticacao(["admin"])
async def alterar_vizualizacao_banner(request:Request, id_banner: int, usuario_logado: dict = None):
    banner = obter_banner_por_id(id_banner)
    if banner:
        novo_status = not banner.is_visible
    return templates.TemplateResponse("admin/banners/banners.html", {"request": request, "usuario": usuario_logado, "banners": obter_todos_banners()})
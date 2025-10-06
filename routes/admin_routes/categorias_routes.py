from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from data.categoria import categoria_repo
from util.auth_decorator import requer_autenticacao
router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias")
@requer_autenticacao(["admin"])
async def get_categorias(request: Request, usuario_logado: dict = None):
    categorias = categoria_repo.obter_categorias()
    response = templates.TemplateResponse("admin/categorias/categorias.html", {"request": request, "usuario": usuario_logado, "categorias": categorias })
    return response

@router.post("/admin/categorias")
@requer_autenticacao(["admin"])
async def post_categorias(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/categorias/categorias.html", {"request": request, "usuario": usuario_logado})
    return response

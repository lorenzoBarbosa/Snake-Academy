from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias/excluir-categoria")
@requer_autenticacao(["admin"])
async def get_excluir_categoria(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/categorias/excluir_categoria.html", {"request": request, "usuario": usuario_logado})
    return response
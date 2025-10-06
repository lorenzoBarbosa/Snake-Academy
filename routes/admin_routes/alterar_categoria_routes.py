from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.categoria import categoria_repo
from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias/alterar-categoria/{id}")
@requer_autenticacao(["admin"])
async def get_alterar_categoria(request: Request, id: int = None, usuario_logado: dict = None):
    categorias = categoria_repo.obter_categorias()
    categoria = categoria_repo.obter_categoria_por_id(id)
    response = templates.TemplateResponse("admin/categorias/alterar_categoria.html", {"request": request, "usuario": usuario_logado, "categorias": categorias, "categoria": categoria})
    return response


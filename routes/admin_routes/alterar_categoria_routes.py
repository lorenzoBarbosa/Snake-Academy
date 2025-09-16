from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/alterar-categoria")
@requer_autenticacao(["admin"])
async def get_alterar_categoria():
    response = templates.TemplateResponse("admin/categorias/alterar_categoria.html", {"request": {}})
    return response
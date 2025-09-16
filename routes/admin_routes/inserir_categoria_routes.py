from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias/inserir-categoria")
@requer_autenticacao(["adimin"])
async def get_inserir_categoria():
    response = templates.TemplateResponse("admin/categorias/inserir_categoria.html", {"request": {}})
    return response
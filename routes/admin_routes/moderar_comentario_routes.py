from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/comentarios/moderar-comentario")
@requer_autenticacao(["admin"])
async def get_moderar_comentario():
    response = templates.TemplateResponse("admin/curso/moderar-comentario.html", {"request": {}})
    return response
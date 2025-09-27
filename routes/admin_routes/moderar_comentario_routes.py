from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/cursos/curso-admin/comentarios/moderar-comentario")
@requer_autenticacao(["admin"])
async def get_moderar_comentario(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/curso/moderar-comentario.html", {"request": request, "usuario": usuario_logado})
    return response
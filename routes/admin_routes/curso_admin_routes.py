from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/curso-admin")
@requer_autenticacao(["admin"])
async def get_curso_admin(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/curso/curso_admin.html", {"request": request, "usuario": usuario_logado})
    return response
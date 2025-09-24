from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/usuarios/confirmar-alteracao-status-admin/{id}")
@requer_autenticacao(["admin"])
async def get_confirmar_alteracao_status_admin(request: Request, id: int, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/usuarios/confirmar_alteracao_status_admin.html", {"request": request, "usuario": usuario_logado})
    return response
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/denuncias/notificar-usuario/{id}")
@requer_autenticacao(["admin"])
async def get_notificar_usuario(request: Request, id: int, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/denuncias/notificar_usuario.html", {"request": request, "usuario": usuario_logado})
    return response
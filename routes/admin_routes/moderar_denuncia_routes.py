from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/denuncias/moderar-denuncia")
@requer_autenticacao(["admin"])
async def get_moderar_denuncia(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/denuncias/moderar_denuncia.html", {"request": request, "usuario": usuario_logado})
    return response
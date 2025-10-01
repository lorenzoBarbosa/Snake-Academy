from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/banners/alterar/{banner_id}")
@requer_autenticacao(["admin"])
async def get_alterar(request: Request, usuario_logado: dict = None, banner_id: int = None):
    response = templates.TemplateResponse("admin/banners/alterar.html", {"request": request, "usuario": usuario_logado, "banner_id": banner_id})
    return response
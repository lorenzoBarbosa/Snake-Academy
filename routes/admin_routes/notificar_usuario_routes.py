from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/denuncias/notificar-usuario")
@requer_autenticacao(["admin"])
async def get_notificar_usuario():
    response = templates.TemplateResponse("admin/denuncias/notificar_usuario.html", {"request": {}})
    return response
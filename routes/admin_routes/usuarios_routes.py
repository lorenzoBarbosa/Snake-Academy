from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/usuarios")
@requer_autenticacao(["admin"])
async def get_usuarios():
    response = templates.TemplateResponse("admin/usuarios/usuarios.html", {"request": {}})
    return response
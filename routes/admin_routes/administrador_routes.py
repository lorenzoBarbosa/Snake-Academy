from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/administrador")
@requer_autenticacao(["admin"])
async def get_administrador():
    response = templates.TemplateResponse("admin/administrador.html", {"request": {}})
    return response

from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/banners/excluir")
@requer_autenticacao(["admin"])
async def get_excluir():
    response = templates.TemplateResponse("admin/banners/excluir.html", {"request": {}})
    return response
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/denuncias")
@requer_autenticacao(["admin"])
async def get_denuncias():
    response = templates.TemplateResponse("admin/denuncias/denuncias.html", {"request": {}})
    return response
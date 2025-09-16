from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/alterar-senha")
@requer_autenticacao(["cliente", "professor", "admin"])
async def get_alterar_senha():
    response = templates.TemplateResponse("cliente/alterar_senha.html", {"request": {}})
    return response


    
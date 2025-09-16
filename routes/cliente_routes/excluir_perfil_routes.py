from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/excluir-perfil")
@requer_autenticacao(["cliente", 'professor', 'admin'])
async def get_excluir_perfil():
    response = templates.TemplateResponse("cliente/excluir_perfil.html", {"request": {}})
    return response


    
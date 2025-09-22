from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/carrinho")
@requer_autenticacao(["cliente", 'professor', 'admin'])
async def get_carrinho(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("cliente/carrinho.html", {"request": request, "usuario": usuario_logado})
    return response


    
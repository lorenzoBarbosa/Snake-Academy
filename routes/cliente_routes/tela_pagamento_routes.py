from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/tela-pagamento")
@requer_autenticacao(["cliente", 'professor', 'admin'])
async def get_tela_pagamento():
    response = templates.TemplateResponse("cliente/tela_pagamento.html", {"request": {}})
    return response
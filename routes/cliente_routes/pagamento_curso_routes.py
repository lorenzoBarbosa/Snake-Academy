from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo
from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/pagamento-curso")
@requer_autenticacao(["cliente", 'professor', 'admin'])
async def get_pagamento_curso(request: Request, usuario_logado: dict= None):
    response = templates.TemplateResponse("cliente/pagamento_curso.html", {"request": request, "usuario": usuario_logado})
    return response


    
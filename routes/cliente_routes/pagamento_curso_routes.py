from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/pagamento_curso")
async def get_pagamento_curso():
    response = templates.TemplateResponse("cliente/pagamento_curso.html", {"request": {}})
    return response


    
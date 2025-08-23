from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/tela_pagamento")
async def get_tela_pagamento():
    response = templates.TemplateResponse("cliente/tela_pagamento.html", {"request": {}})
    return response
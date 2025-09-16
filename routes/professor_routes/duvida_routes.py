from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/comunicacao/duvida")
@requer_autenticacao(["professor"])
async def get_duvida():
    response = templates.TemplateResponse("professor/duvida.html", {"request": {}})
    return response
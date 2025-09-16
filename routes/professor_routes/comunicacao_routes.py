from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/comunicacao")
@requer_autenticacao(["professor"])
async def get_comunicacao():
    response = templates.TemplateResponse("professor/comunicacao.html", {"request": {}})
    return response
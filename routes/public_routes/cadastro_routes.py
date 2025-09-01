from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cadastro")
async def get_cadastro():
    response = templates.TemplateResponse("publico/cadastro.html", {"request": {}})
    return response

@router.post("/cadastro")
async def post_cadastro(nome: str, email: str, senha: str):
    pass
    
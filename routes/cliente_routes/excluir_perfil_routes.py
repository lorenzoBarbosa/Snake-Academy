from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/excluir_perfil")
async def get_excluir_perfil():
    response = templates.TemplateResponse("cliente/excluir_perfil.html", {"request": {}})
    return response


    
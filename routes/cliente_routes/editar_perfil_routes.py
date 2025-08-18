from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/editar_perfil")
async def get_editar_perfil():
    response = templates.TemplateResponse("cliente/editar_perfil.html", {"request": {}})
    return response


    
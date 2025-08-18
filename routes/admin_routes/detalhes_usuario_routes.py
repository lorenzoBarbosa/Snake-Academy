from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/detalhes_usuario")
async def get_detalhes_usuario():
    response = templates.TemplateResponse("admin/usuarios/detalhes_usuario.html", {"request": {}})
    return response
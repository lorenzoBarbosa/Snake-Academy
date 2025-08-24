from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/usuarios")
async def get_usuarios():
    response = templates.TemplateResponse("admin/usuarios/usuarios.html", {"request": {}})
    return response
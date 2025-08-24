from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/notificar_usuario")
async def get_notificar_usuario():
    response = templates.TemplateResponse("admin/denuncias/notificar_usuario.html", {"request": {}})
    return response
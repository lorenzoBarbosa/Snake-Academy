from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/moderar_comentario")
async def get_moderar_comentario():
    response = templates.TemplateResponse("admin/curso/moderar_comentario.html", {"request": {}})
    return response
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/alterar_categoria")
async def get_alterar_categoria():
    response = templates.TemplateResponse("admin/categorias/alterar_categoria.html", {"request": {}})
    return response
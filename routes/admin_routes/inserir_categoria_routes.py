from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/inserir_categoria")
async def get_inserir_categoria():
    response = templates.TemplateResponse("admin/categorias/inserir_categoria.html", {"request": {}})
    return response
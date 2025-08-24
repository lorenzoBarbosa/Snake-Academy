from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias")
async def get_categorias():
    response = templates.TemplateResponse("admin/categorias/categorias.html", {"request": {}})
    return response
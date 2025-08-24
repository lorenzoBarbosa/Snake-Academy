from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/excluir")
async def get_excluir():
    response = templates.TemplateResponse("admin/banners/excluir.html", {"request": {}})
    return response
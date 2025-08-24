from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/moderar_denuncia")
async def get_moderar_denuncia():
    response = templates.TemplateResponse("admin/denuncias/moderar_denuncia.html", {"request": {}})
    return response
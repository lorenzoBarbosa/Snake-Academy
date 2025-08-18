from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/confirmar_alteracao_status")
async def get_confirmar_alteracao_status():
    response = templates.TemplateResponse("admin/usuarios/confirmar_alteracao_status.html", {"request": {}})
    return response
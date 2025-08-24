from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/confirmar_alteracao_status_admin")
async def get_confirmar_alteracao_status_admin():
    response = templates.TemplateResponse("admin/usuarios/confirmar_alteracao_status_admin.html", {"request": {}})
    return response
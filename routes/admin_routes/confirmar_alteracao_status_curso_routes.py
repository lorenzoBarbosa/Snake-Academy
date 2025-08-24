from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/confirmar_alteracao_status_curso")
async def get_confirmar_alteracao_status_curso():
    response = templates.TemplateResponse("admin/curso/confirmar_alteracao_status_curso.html", {"request": {}})
    return response

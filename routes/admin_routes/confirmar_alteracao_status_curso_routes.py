from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/cursos/curso-admin/confirmar-alteracao-status-curso")
async def get_confirmar_alteracao_status_curso(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/curso/confirmar_alteracao_status_curso.html", {"request": request, "usuario": usuario_logado})
    return response

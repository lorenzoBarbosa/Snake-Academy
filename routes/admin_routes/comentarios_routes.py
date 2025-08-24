from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/comentarios")
async def get_comentarios():
    response = templates.TemplateResponse("admin/curso/comentarios.html", {"request": {}})
    return response
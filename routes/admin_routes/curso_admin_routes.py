from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/curso_admin")
async def get_curso_admin():
    response = templates.TemplateResponse("admin/curso/curso_admin.html", {"request": {}})
    return response
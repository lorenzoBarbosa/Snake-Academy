from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/denuncias")
async def get_denuncias():
    response = templates.TemplateResponse("admin/denuncias/denuncias.html", {"request": {}})
    return response
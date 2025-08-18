from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/administrador")
async def get_administrador():
    response = templates.TemplateResponse("admin/administrador.html", {"request": {}})
    return response

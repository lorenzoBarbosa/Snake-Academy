from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/cadastrar")
async def get_cadastrar():
    response = templates.TemplateResponse("admin/banners/cadastrar.html", {"request": {}})
    return response
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/alterar")
async def get_alterar():
    response = templates.TemplateResponse("admin/banners/alterar.html", {"request": {}})
    return response
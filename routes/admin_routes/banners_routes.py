from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/banners")
async def get_banners():
    response = templates.TemplateResponse("admin/banners/banners.html", {"request": {}})
    return response
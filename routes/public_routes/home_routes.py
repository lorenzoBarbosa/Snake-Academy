from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_root():
    response = templates.TemplateResponse("publico/home.html", {"request": {}})
    return response


    
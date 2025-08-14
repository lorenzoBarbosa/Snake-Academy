from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
async def get_login():
    response = templates.TemplateResponse("publico/login.html", {"request": {}})
    return response



    
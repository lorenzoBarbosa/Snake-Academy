from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/recuperar_senha")
async def get_recuperar_senha():
    response = templates.TemplateResponse("publico/recuperar_senha.html", {"request": {}})
    return response


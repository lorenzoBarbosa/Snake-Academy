from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/redefinir_senha")
async def get_restaurar_senha():
    response = templates.TemplateResponse("publico/redefinir_senha.html", {"request": {}})
    return response


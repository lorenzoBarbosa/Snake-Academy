from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/alterar_senha")
async def get_alterar_senha():
    response = templates.TemplateResponse("cliente/alterar_senha.html", {"request": {}})
    return response


    
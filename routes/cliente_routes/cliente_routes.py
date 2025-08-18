from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente")
async def get_cliente():
    response = templates.TemplateResponse("cliente/cliente.html", {"request": {}})
    return response


    
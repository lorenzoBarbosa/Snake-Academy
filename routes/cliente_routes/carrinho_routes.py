from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/carrinho")
async def get_carrinho():
    response = templates.TemplateResponse("cliente/carrinho.html", {"request": {}})
    return response


    
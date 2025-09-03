from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/confirmacao_cadastro")
async def get_confirmacao_cadastro():
    response = templates.TemplateResponse("publico/confirmacao_cadastro.html", {"request": {}})
    return response

from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/validacao_email")
async def get_validacao_email():
    response = templates.TemplateResponse("publico/validacao_email.html", {"request": {}})
    return response
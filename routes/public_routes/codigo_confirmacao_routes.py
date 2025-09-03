from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/codigo_confirmacao")
async def get_codigo_confirmacao():
    response = templates.TemplateResponse("publico/codigo_confirmacao.html", {"request": {}})
    return response
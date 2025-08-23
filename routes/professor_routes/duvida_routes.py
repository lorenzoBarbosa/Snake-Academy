from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/comunicacao/duvida")
async def get_duvida():
    response = templates.TemplateResponse("professor/duvida.html", {"request": {}})
    return response
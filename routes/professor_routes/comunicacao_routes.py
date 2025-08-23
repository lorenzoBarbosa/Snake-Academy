from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/comunicacao")
async def get_comunicacao():
    response = templates.TemplateResponse("professor/comunicacao.html", {"request": {}})
    return response
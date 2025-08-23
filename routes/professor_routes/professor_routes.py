from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor")
async def get_professor():
    response = templates.TemplateResponse("professor/professor.html", {"request": {}})
    return response
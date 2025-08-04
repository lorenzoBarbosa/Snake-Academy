from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def get_root():
    response = templates.TemplateResponse("publico/home.html", {"request": {}})
    return response

@router.get("/cadastro")
async def get_cadastro():
    response = templates.TemplateResponse("publico/cadastro.html", {"request": {}})
    return response

@router.get("/login")
async def get_login():
    response = templates.TemplateResponse("publico/login.html", {"request": {}})
    return response

@router.get("/curso")
async def get_curso():
    response = templates.TemplateResponse("publico/curso.html", {"request": {}})
    return response


    
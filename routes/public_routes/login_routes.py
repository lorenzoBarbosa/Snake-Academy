from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.params import Form

from data.usuario import usuario_repo

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
async def get_login():
    response = templates.TemplateResponse("publico/login.html", {"request": {}})
    return response

@router.post("/login")
async def post_login(email: str = Form(...), senha: str = Form(...)):
    usuario = usuario_repo.obter_usuario_por_email(email)
    id = usuario.id if usuario else None
    if usuario and usuario.senha == senha:
        return RedirectResponse(url=f"/cliente{id}", status_code=303)
    else:
        response = templates.TemplateResponse("publico/login.html", {"request": {}, "mensagem": "Email ou senha inválidos."})
    return response

    
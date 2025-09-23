from urllib import request
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.params import Form

from data.usuario import usuario_repo
from util.auth_decorator import *
from util.security import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/login")
async def get_login(request: Request, redirect: str = None):
    if esta_logado(request):
        response = RedirectResponse(redirect, status.HTTP_303_SEE_OTHER)
    else:
        response = templates.TemplateResponse("publico/login.html", {"request": request, "redirect": redirect})
    return response

@router.post("/login")
async def post_login(
            request: Request,
            email: str = Form(...),
            senha: str = Form(...),
            redirect: str = Form(None)):
    
    usuario = usuario_repo.obter_usuario_por_email(email)
    id = usuario.id if usuario else None

    if not usuario or not verificar_senha(senha, usuario.senha):
        return templates.TemplateResponse("publico/login.html", {"request": request, "mensagem": "Email ou senha inválidos."})

    usuario_dict = {
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email,
        "perfil": usuario.perfil,
        "foto": usuario.foto
    }
    criar_sessao(request, usuario_dict)
    if usuario.perfil == "admin":
        url_redirect = redirect if redirect else "/administrador"
    else:
        url_redirect = redirect if redirect else "/cliente"
    return RedirectResponse(url_redirect, status.HTTP_303_SEE_OTHER)

@router.get("/logout")
async def logout(request: Request):
    destruir_sessao(request)
    return RedirectResponse("/", status.HTTP_303_SEE_OTHER)
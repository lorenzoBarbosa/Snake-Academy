from urllib import request
from fastapi import APIRouter, Request, logger
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.params import Form
from pydantic_core import ValidationError

from data.usuario import usuario_repo
from dtos.login_dto import LoginDTO
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
            email: str = Form(),
            senha: str = Form(),
            redirect: str = Form(None)):
    
    dados_formulario = {
        "email": email
    }


    try:
        login_dto = LoginDTO(email=email, senha=senha)

        usuario = usuario_repo.obter_usuario_por_email(login_dto.email)
        id = usuario.id if usuario else None

        if not usuario or not verificar_senha(login_dto.senha, usuario.senha):
            return templates.TemplateResponse("publico/login.html", {"request": request, 'dados': dados_formulario, "mensagem": "Email ou senha inválidos."})

        usuario_dict = {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "perfil": usuario.perfil,
            "foto": usuario.foto,
            "identificacaoProfessor": False
        }
        criar_sessao(request, usuario_dict)
        if usuario.perfil == "admin":
            url_redirect = redirect if redirect else "/administrador"
        else:
            url_redirect = redirect if redirect else "/cliente"
        return RedirectResponse(url_redirect, status.HTTP_303_SEE_OTHER)
    
    except ValidationError as e:
        # Extrair mensagens de erro do Pydantic
        erros = dict()
        for erro in e.errors():
            campo = erro['loc'][0] if erro['loc'] else 'campo'
            mensagem = erro['msg']
            erros[campo.upper()] = mensagem.replace('Value error, ', '')
        #logger.warning(f"Erro de validação no login: {erro_msg}")

        # Retornar template com dados preservados e erro
        return templates.TemplateResponse("publico/login.html", {
            "request": request,
            "erros": erros,
            "dados": dados_formulario  # Preservar dados digitados
        })

    except Exception as e:
        #logger.error(f"Erro ao processar login: {e}")

        return templates.TemplateResponse("publico/login.html", {
            "request": request,
            "erros": {"GERAL": "Erro ao processar login. Tente novamente."},
            "dados": dados_formulario
        })

@router.get("/logout")
async def logout(request: Request):
    destruir_sessao(request)
    return RedirectResponse("/", status.HTTP_303_SEE_OTHER)
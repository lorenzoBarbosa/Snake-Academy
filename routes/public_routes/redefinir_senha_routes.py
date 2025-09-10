from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


import re

# Função de verificação de força da senha
def verificar_forca_senha(senha: str) -> str:
    pontuacao = 0

    if len(senha) >= 8:
        pontuacao += 1
    if re.search(r"[A-Z]", senha):
        pontuacao += 1
    if re.search(r"[a-z]", senha):
        pontuacao += 1
    if re.search(r"\d", senha):
        pontuacao += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        pontuacao += 1

    if pontuacao <= 2:
        return "fraca"
    elif pontuacao == 3 or pontuacao == 4:
        return "média"
    else:
        return "forte"



router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/redefinir_senha")
async def get_restaurar_senha(request: Request):
    response = templates.TemplateResponse("publico/redefinir_senha.html", {"request": request, "usuario": None})
    return response

@router.post("/redefinir_senha", response_class=HTMLResponse)
async def post_restaurar_senha(
    request: Request,
    senha_nova: str = Form(...),
    senha_confirmacao: str = Form(...)
):
    if senha_nova != senha_confirmacao:
        # Senhas não coincidem — aponta erro no template
        return templates.TemplateResponse("publico/redefinir_senha.html", {
            "request": request,
            "erro_senha": True
        })
    
    # Verifica a força da senha
    forca = verificar_forca_senha(senha_nova)

    if forca == "fraca":
        return templates.TemplateResponse("publico/redefinir_senha.html", {
            "request": request,
            "erro_forca": True,
            "mensagem_erro": "A senha é muito fraca. Por favor, escolha uma senha mais forte."
        })
    else:
        return RedirectResponse(url="/", status_code=303)


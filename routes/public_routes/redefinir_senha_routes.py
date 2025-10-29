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

@router.get("/redefinir-senha")
async def get_restaurar_senha(request: Request):
    response = templates.TemplateResponse("publico/redefinir_senha.html", {"request": request, "usuario": None})
    return response

@router.post("/redefinir-senha", response_class=HTMLResponse)
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
            "mensagem_erro": "Sua senha está fraca. Tente novamente"
        })
    else:
        return RedirectResponse(url="/login", status_code=303)


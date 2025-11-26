import re
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


def validar_senha(senha: str) -> tuple[bool, list[str]]:
    """
    Valida se a senha atende todos os requisitos obrigatórios.
    
    Retorna:
        tuple: (senha_valida: bool, erros: list[str])
    """
    erros = []
    
    # Requisito 1: Tamanho mínimo
    if len(senha) < 8:
        erros.append("A senha deve ter no mínimo 8 caracteres")
    
    # Requisito 2: Pelo menos uma letra maiúscula
    if not re.search(r"[A-Z]", senha):
        erros.append("A senha deve conter pelo menos uma letra MAIÚSCULA")
    
    # Requisito 3: Pelo menos uma letra minúscula
    if not re.search(r"[a-z]", senha):
        erros.append("A senha deve conter pelo menos uma letra minúscula")
    
    # Requisito 4: Pelo menos um número
    if not re.search(r"\d", senha):
        erros.append("A senha deve conter pelo menos um número")
    
    # Requisito 5: Pelo menos um símbolo especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        erros.append("A senha deve conter pelo menos um símbolo especial (!@#$%...)")
    
    senha_valida = len(erros) == 0
    return senha_valida, erros


def verificar_forca_senha(senha: str) -> str:
    """
    Calcula a força da senha (fraca, média, forte).
    Essa função agora é apenas informativa, pois a validação já garante requisitos mínimos.
    """
    pontuacao = 0
    
    if len(senha) >= 8:
        pontuacao += 1
    if len(senha) >= 12:  # Bônus por senha longa
        pontuacao += 1
    if re.search(r"[A-Z]", senha):
        pontuacao += 1
    if re.search(r"[a-z]", senha):
        pontuacao += 1
    if re.search(r"\d", senha):
        pontuacao += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        pontuacao += 1
    
    if pontuacao <= 3:
        return "fraca"
    elif pontuacao <= 5:
        return "média"
    else:
        return "forte"


@router.get("/redefinir_senha")
async def get_restaurar_senha(request: Request):
    return templates.TemplateResponse(
        "publico/redefinir_senha.html", 
        {"request": request}
    )


@router.post("/redefinir_senha", response_class=HTMLResponse)
async def post_restaurar_senha(
    request: Request,
    senha_nova: str = Form(...),
    senha_confirmacao: str = Form(...)
):
    # Validação 1: Senhas coincidem
    if senha_nova != senha_confirmacao:
        return templates.TemplateResponse(
            "publico/redefinir_senha.html", {
                "request": request,
                "erro_senha": True,
                "mensagem_erro": "As senhas não coincidem"
            }
        )
    
    # Validação 2: Requisitos obrigatórios
    senha_valida, erros = validar_senha(senha_nova)
    
    if not senha_valida:
        # Retorna todos os erros de requisitos
        return templates.TemplateResponse(
            "publico/redefinir_senha.html", {
                "request": request,
                "erro_requisitos": True,
                "lista_erros": erros
            }
        )
    
    # Validação 3: Força da senha (opcional - apenas aviso)
    forca = verificar_forca_senha(senha_nova)
    
    return RedirectResponse(
        url="/login", 
        status_code=303
    )
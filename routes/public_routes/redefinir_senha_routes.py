from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/redefinir_senha")
async def get_restaurar_senha():
    response = templates.TemplateResponse("publico/redefinir_senha.html", {"request": {}})
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
    else:
        return RedirectResponse(url="/", status_code=303)


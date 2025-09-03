from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

CODIGO_CORRETO = "123456"  

@router.get("/validacao_email")
async def get_validacao_email(request: Request):
    return templates.TemplateResponse(
        "publico/validacao_email.html", 
        {"request": request, "erro": False}
    )


@router.post("/validacao_email")
async def post_validacao_email(request: Request, codigo: str = Form(...)):
    if codigo == CODIGO_CORRETO:
        return RedirectResponse(url="/redefinir_senha", status_code=303)
    else:
        return templates.TemplateResponse(
            "publico/validacao_email.html",
            {"request": request, "erro": True}
        )


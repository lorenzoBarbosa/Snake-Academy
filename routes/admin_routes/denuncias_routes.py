from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from util.auth_decorator import requer_autenticacao
from data.chamado.chamado_repo import obter_todos_chamados

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/denuncias")
@requer_autenticacao(["admin"])
async def get_denuncias(request: Request, usuario_logado: dict = None):
    denuncias = obter_todos_chamados()
    return templates.TemplateResponse(
        "admin/denuncias/denuncias.html",
        {"request": request, "usuario": usuario_logado, "denuncias": denuncias}
    )

@router.post("/admin/denuncias/filtro")
@requer_autenticacao(["admin"])
async def filtro_denuncias(
    request: Request,
    usuario_logado: dict = None,
    tipo_denuncia: str = Form(...),
    ordenar_por: str = Form(...)
):
    denuncias = obter_todos_chamados()

    if tipo_denuncia.lower() != "todas":
        denuncias = [d for d in denuncias if d.tipo.lower() == tipo_denuncia.lower()]

    if ordenar_por == "recentes":
        denuncias = sorted(
            denuncias,
            key=lambda d: (d.dataEnvio, d.horaEnvio),
            reverse=True
        )

    return templates.TemplateResponse(
        "admin/denuncias/denuncias.html",
        {"request": request, "usuario": usuario_logado, "denuncias": denuncias}
    )

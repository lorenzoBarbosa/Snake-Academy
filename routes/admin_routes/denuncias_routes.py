from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from util.auth_decorator import requer_autenticacao
from data.chamado.chamado_repo import obter_todos_chamados
from data.usuario.usuario_repo import obter_todos_usuarios  # importa usuários se ainda não tiver

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/admin/denuncias")
@requer_autenticacao(["admin"])
async def get_denuncias(request: Request, usuario_logado: dict = None):
    denuncias = obter_todos_chamados()
    usuarios = obter_todos_usuarios()  # lista de usuários pra popular o select
    return templates.TemplateResponse(
        "admin/denuncias/denuncias.html",
        {
            "request": request,
            "usuario": usuario_logado,
            "denuncias": denuncias,
            "usuarios": usuarios
        }
    )


@router.post("/admin/denuncias/filtro")
@requer_autenticacao(["admin"])
async def filtro_denuncias(
    request: Request,
    usuario_logado: dict = None,
    tipo_denuncia: str = Form(""),
    usuario_id: str = Form(""),
    q: str = Form(""),
    ordenar_por: str = Form("")
):
    denuncias = obter_todos_chamados()
    usuarios = obter_todos_usuarios()

    # --- Filtro por tipo de denúncia ---
    if tipo_denuncia and tipo_denuncia.lower() != "todas":
        denuncias = [d for d in denuncias if d.tipo.lower() == tipo_denuncia.lower()]

    # --- Filtro por usuário ---
    if usuario_id:
        try:
            usuario_id_int = int(usuario_id)
            denuncias = [d for d in denuncias if getattr(d, "usuario_id", None) == usuario_id_int]
        except ValueError:
            pass

    # --- Busca textual (nome, email, descrição) ---
    if q:
        q_lower = q.lower()
        denuncias = [
            d for d in denuncias
            if q_lower in getattr(d, "descricao", "").lower()
            or q_lower in getattr(getattr(d, "usuario", {}), "nome", "").lower()
            or q_lower in getattr(getattr(d, "usuario", {}), "email", "").lower()
        ]

    # --- Ordenação ---
    if ordenar_por == "recentes":
        denuncias = sorted(denuncias, key=lambda d: (d.dataEnvio, d.horaEnvio), reverse=True)
    elif ordenar_por == "antigos":
        denuncias = sorted(denuncias, key=lambda d: (d.dataEnvio, d.horaEnvio))
    else:
        denuncias = sorted(denuncias, key=lambda d: (d.dataEnvio, d.horaEnvio), reverse=True)

    return templates.TemplateResponse(
        "admin/denuncias/denuncias.html",
        {
            "request": request,
            "usuario": usuario_logado,
            "denuncias": denuncias,
            "usuarios": usuarios
        }
    )

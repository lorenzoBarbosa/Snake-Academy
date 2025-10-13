from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from data.admin.admin_repo import obter_todos_admins
from data.cliente.cliente_repo import excluir_cliente_por_id, obter_todos_clientes
from data.matricula.matricula_repo import obter_todas_matriculas
from data.professor.professor_repo import excluir_professor_por_id, obter_todos_professores
from data.usuario.usuario_repo import *
from util.auth_decorator import requer_autenticacao
from util.flash_messages import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/usuarios")
@requer_autenticacao(["admin"])
async def get_usuarios(request: Request, usuario_logado: dict = None):
    usuarios = obter_todos_usuarios()
    print(usuarios)
    response = templates.TemplateResponse("admin/usuarios/usuarios.html", {"request": request, "usuario": usuario_logado, "usuarios": usuarios})
    return response

@router.post("/admin/usuarios/filtro")
@requer_autenticacao(["admin"])
async def filtro_usuarios(
    request: Request,
    usuario_logado: dict = None,
    tipo_usuario: str = Form(...),
    status_usuario: Optional[str] = Form(None)
):
    if tipo_usuario == "todos":
        usuarios = obter_todos_usuarios()
    elif tipo_usuario == "clientes":
        if status_usuario == "matriculados":
            usuarios = obter_todas_matriculas()
        else:
            usuarios = obter_todos_clientes()
    elif tipo_usuario == "professores":
        usuarios = obter_todos_professores()
    elif tipo_usuario == "administradores":
        usuarios = obter_todos_admins()
    else:
        usuarios = obter_todos_usuarios()

    return templates.TemplateResponse(
        "admin/usuarios/usuarios.html",
        {"request": request, "usuario": usuario_logado, "usuarios": usuarios}
    )

@router.get("/admin/usuarios/detalhes-usuario/{usuario_id}")
@requer_autenticacao(["admin"])
async def get_usuario_detalhes(request: Request, usuario_id: int, usuario_logado: dict = None):
    usuario = obter_usuario_por_id(usuario_id)

    return templates.TemplateResponse("admin/usuarios/detalhes_usuario.html", {"request": request, "usuario": usuario_logado, "detalhes_usuario": usuario})

@router.post("/admin/usuarios/detalhes-usuario/{usuario_id}/excluir")
@requer_autenticacao(["admin"])
async def excluir_usuario(request: Request, usuario_id: int, usuario_logado: dict = None):
    detalhes_usuario = obter_usuario_por_id(usuario_id)
    try:
        if detalhes_usuario.perfil == "professor":
            excluir_professor_por_id(usuario_id)
        excluir_cliente_por_id(usuario_id)
        excluir_usuario_por_id(usuario_id)
        informar_sucesso(request, "Usuário excluído com sucesso.")
        return RedirectResponse("/admin/usuarios", status_code=303)
    except Exception as e:
        informar_erro(request, "Erro ao excluir usuário. Tente novamente.")
        return templates.TemplateResponse("admin/usuarios/cadastro.html", {
            "request": request,
            "erros": {"GERAL": "Erro ao excluir usuário. Tente novamente."},
            "usuario": usuario_logado,
            "detalhes_usuario": detalhes_usuario
        })

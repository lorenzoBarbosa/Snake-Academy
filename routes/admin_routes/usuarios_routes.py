from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

from data.admin.admin_repo import obter_todos_admins
from data.cliente.cliente_repo import obter_todos_clientes
from data.matricula.matricula_repo import obter_todas_matriculas
from data.professor.professor_repo import obter_todos_professores
from data.usuario.usuario_repo import *
from util.auth_decorator import requer_autenticacao

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

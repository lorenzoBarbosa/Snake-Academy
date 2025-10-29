from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates

from data.banner.banner_repo import *
from data.cliente.cliente_repo import obter_cliente_por_termo_paginado
from data.curso.curso_repo import *
from data.matricula import matricula_repo
from data.professor.professor_repo import obter_professor_por_termo_paginado
from data.usuario.usuario_repo import obter_usuario_por_termo_paginado
from util.auth_decorator import requer_autenticacao
from util.flash_messages import informar_erro

router = APIRouter()
templates = Jinja2Templates(directory="templates")

banners = obter_todos_banners()

@router.get("/administrador")
@requer_autenticacao(["admin"])
async def get_administrador(request: Request, usuario_logado: dict = None):
    return templates.TemplateResponse(
        "admin/administrador.html",
        {"request": request, "usuario": usuario_logado, "banners": banners}
    )


@router.get("/admin/pesquisar")
@requer_autenticacao(["admin"])
async def pesquisar(
    request: Request,
    usuario_logado: dict = None,
    termo_pesquisa: str = Query(...)
):
    banners = obter_todos_banners()
    termo = termo_pesquisa.lower()
    pesquisas = ["curso", "usuario"]
  
    for p in pesquisas:
        if p == "curso":
            resultado = obter_curso_por_termo_paginado(termo, 1, 20)
            lista_cursoQtdAlunos = []
            for c in resultado:
                qtdAlunos = len(matricula_repo.obter_matriculas_por_curso(c.nome))
                lista_cursoQtdAlunos.append({"curso": c, "qtdAlunos": qtdAlunos})
            if resultado:
                return templates.TemplateResponse(
                    "admin/curso/cursos.html",
                    {
                        "request": request,
                        "usuario": usuario_logado,
                        "cursos_qtdAlunos": lista_cursoQtdAlunos,
                    },
                )

        elif p == "usuario":
            resultado = obter_usuario_por_termo_paginado(termo, 1, 20)
            if resultado:
                return templates.TemplateResponse(
                    "admin/usuarios/usuarios.html",
                    {"request": request, "usuario": usuario_logado, "usuarios": resultado},
                )
            else:
                informar_erro(request, f"Termo não encontrado")
                return templates.TemplateResponse(
                    "admin/administrador.html",
                    {"request": request, "usuario": usuario_logado, "banners": banners}
                )

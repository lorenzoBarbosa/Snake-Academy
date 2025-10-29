from fastapi import APIRouter, Request, Query
from fastapi.templating import Jinja2Templates

from data.categoria import categoria_repo
from data.curso import curso_repo
from data.matricula import matricula_repo
from data.topico import topico_repo
from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/cursos")
@requer_autenticacao(["admin"])
async def get_curso_admin(
    request: Request,
    usuario_logado: dict = None,
    categoria: str = Query(default=""),
    topico: str = Query(default=""),
    alunos: str = Query(default="")
):
    categorias = categoria_repo.obter_categorias()
    topicos = topico_repo.obter_topicos()
    cursos = curso_repo.obter_todos_cursos()

    # 1. Filtro por categoria
    if categoria:
        topicos_categoria = [t.id for t in topicos if str(t.idCategoria) == categoria]
        cursos = [c for c in cursos if str(c.idTopico) in map(str, topicos_categoria)]

    # 2. Filtro por tópico
    if topico:
        cursos = [c for c in cursos if str(c.idTopico) == topico]

    # Monta lista com qtd de alunos
    lista_cursoQtdAlunos = []
    for c in cursos:
        qtdAlunos = len(matricula_repo.obter_matriculas_por_curso(c.nome))
        lista_cursoQtdAlunos.append({
            "curso": c,
            "qtdAlunos": qtdAlunos
        })

    # 3. Filtro por quantidade de alunos
    if alunos:
        if alunos == "0-50":
            lista_cursoQtdAlunos = [item for item in lista_cursoQtdAlunos if 0 <= item["qtdAlunos"] <= 50]
        elif alunos == "51-200":
            lista_cursoQtdAlunos = [item for item in lista_cursoQtdAlunos if 51 <= item["qtdAlunos"] <= 200]
        elif alunos == "201-500":
            lista_cursoQtdAlunos = [item for item in lista_cursoQtdAlunos if 201 <= item["qtdAlunos"] <= 500]
        elif alunos == "500+":
            lista_cursoQtdAlunos = [item for item in lista_cursoQtdAlunos if item["qtdAlunos"] > 500]
    return templates.TemplateResponse(
        "admin/curso/cursos.html",
        {
            "request": request,
            "usuario": usuario_logado,
            "categorias": categorias,
            "topicos": topicos,
            "cursos_qtdAlunos": lista_cursoQtdAlunos
        },
    )



@router.get("/admin/cursos/curso-admin/{curso_id}")
@requer_autenticacao(["admin"])
async def get_curso_admin(request: Request, usuario_logado: dict = None, curso_id: int = None):
    detalhes_curso = curso_repo.obter_curso_por_id(curso_id)
    response = templates.TemplateResponse("admin/curso/curso_admin.html", {"request": request, "usuario": usuario_logado, "detalhes_curso": detalhes_curso})
    return response
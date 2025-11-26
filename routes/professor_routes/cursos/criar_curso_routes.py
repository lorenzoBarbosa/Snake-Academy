from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.topico.topico_repo import obter_topicos
from util.auth_decorator import requer_autenticacao

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/criar-curso")
@requer_autenticacao(["professor"])
async def get_criar_curso(request: Request, usuario_logado: dict = None):
    usuario_logado["indentificacaoProfessor"] = True
    topicos = obter_topicos()
    response = templates.TemplateResponse("professor/cursos/criar_curso.html", {"request": request, "usuario": usuario_logado, "topicos": topicos})
    return response

async def post_criar_curso(request: Request,
                        usuario_logado: dict = None,
                        titulo: str = None,
                        custo: float = None,
                        descricao: str = None,
                        topico_id: int = None):
    # Lógica para processar o formulário de criação de curso
    pass

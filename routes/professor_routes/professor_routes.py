from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.cliente.cliente_repo import atualizar_identificacao_professor_por_id, obter_cliente_por_id
from util.auth_decorator import *

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor")
@requer_autenticacao(["professor", "admin", "cliente"])
async def get_professor(request: Request, usuario_logado: dict = None):
    cliente  = obter_cliente_por_id(usuario_logado['id'])
    cliente.indentificacaoProfessor = True
    resultado = atualizar_identificacao_professor_por_id(cliente.indentificacaoProfessor, cliente.id)
    usuario_logado['indentificacaoProfessor'] = cliente.indentificacaoProfessor
    response = templates.TemplateResponse("professor/professor.html", {"request": request, "usuario": usuario_logado})
    return response
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from data.categoria import categoria_repo
from util.auth_decorator import requer_autenticacao
from util.flash_messages import informar_sucesso

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias/excluir-categoria/{id}")
@requer_autenticacao(["admin"])
async def get_excluir_categoria(request: Request, id: int, usuario_logado: dict = None):
    categoria = categoria_repo.obter_categoria_por_id(id)
    response = templates.TemplateResponse("admin/categorias/excluir_categoria.html", {"request": request, "usuario": usuario_logado, "categoria": categoria
    })
    return response

@router.post("/admin/categorias/excluir-categoria/{id}")
@requer_autenticacao(["admin"])
async def post_excluir_categoria(request: Request, id: int, usuario_logado: dict = None):
    categoria_repo.excluir_categoria_por_id(id)
    informar_sucesso(request, f"Categoria excluída com sucesso.")
    return RedirectResponse(url="/admin/categorias", status_code=303)
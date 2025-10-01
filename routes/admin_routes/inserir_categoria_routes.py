from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

from data.categoria import categoria_repo
from data.categoria.categoria_model import Categoria
from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias/inserir-categoria")
@requer_autenticacao(["admin"])
async def get_inserir_categoria(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/categorias/inserir_categoria.html", {"request": request, "usuario": usuario_logado})
    return response

@router.post("/admin/categorias/inserir-categoria")
@requer_autenticacao(["admin"])
async def post_inserir_categoria(request: Request,
                                  usuario_logado: dict = None,
                                  nome: str = Form(...)):
    categoria = Categoria(id=0, nome=nome)
    try:
        categoria_repo.inserir_categoria(categoria)
    except Exception as e:
        return templates.TemplateResponse("admin/categorias/inserir_categoria.html", {"request": request, "erro": "Algo deu errado, tente novamente.", "usuario": usuario_logado})
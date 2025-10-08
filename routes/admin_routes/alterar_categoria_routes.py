from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from pydantic_core import ValidationError

from data.categoria import categoria_repo
from data.categoria.categoria_model import Categoria
from dtos.categorais_dto import AtualizarCategoriaDTO
from util.auth_decorator import requer_autenticacao
from util.flash_messages import informar_erro, informar_sucesso

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/categorias/alterar-categoria/{id}")
@requer_autenticacao(["admin"])
async def get_alterar_categoria(request: Request, id: int = None, usuario_logado: dict = None):
    categorias = categoria_repo.obter_categorias()
    categoria = categoria_repo.obter_categoria_por_id(id)
    response = templates.TemplateResponse("admin/categorias/alterar_categoria.html", {"request": request, "usuario": usuario_logado, "categorias": categorias, "categoria": categoria})
    return response

@router.post("/admin/categorias/alterar-categoria/{id}")
@requer_autenticacao(["admin"])
async def post_alterar_categoria(request: Request, id: int = None, usuario_logado: dict = None, nome: str = Form(...)):
    categorias = categoria_repo.obter_categorias()
    categoria = categoria_repo.obter_categoria_por_id(id)
    dados_originais = {"nome": nome}
    try:
        dados = AtualizarCategoriaDTO(id=id, nome=nome)
        nova_categoria = Categoria(id=dados.id, nome=dados.nome)
        categoria_repo.atualizar_categoria_por_id(nova_categoria.id, nova_categoria.nome)
        informar_sucesso(request, f"Categoria atualizada com sucesso.")
        return templates.TemplateResponse("admin/categorias/alterar_categoria.html", {"request": request, "usuario": usuario_logado, "categorias": categorias, "categoria": categoria})
    except ValidationError as e:
        erros = []
        for erro in e.errors():
            mensagem = erro['msg']
            if mensagem.startswith("Value error, ",):
                mensagem = mensagem.replace("Value error, ", "")
            erros.append(mensagem)
        erro_msg = " | ".join(erros)
        print(f"Erros de validação: {erro_msg}")
        informar_erro(request, f"Há erros no formulário")
        return templates.TemplateResponse("admin/categorias/alterar_categoria.html", {"request": request, "usuario": usuario_logado, "categorias": categorias, "categoria": categoria, "erro": erro_msg})
    except Exception as e:
        # logger.error(f"Erro ao processar cadastro: {e}")
        print(f"Erro ao processar cadastro: {e}")
        return templates.TemplateResponse("admin/categorias/alterar_categoria.html", {"request": request, "usuario": usuario_logado, "categorias": categorias, "categoria": categoria, "erro": "Erro ao processar cadastro. Tente novamente."})


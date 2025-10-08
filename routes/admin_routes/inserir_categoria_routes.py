from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError

from data.categoria import categoria_repo
from data.categoria.categoria_model import Categoria
from dtos.categorais_dto import InserirCategoriaDTO
from util.auth_decorator import requer_autenticacao
from util.flash_messages import informar_erro, informar_sucesso

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
    dados_originais = {"nome": nome}
    try:
        dados = InserirCategoriaDTO(nome=nome)
        nova_categoria = Categoria(nome=dados.nome)
        categoria_repo.inserir_categoria(nova_categoria)
        informar_sucesso(request, f"Categoria inserida com sucesso.")
        print("Categoria inserida com sucesso.")
        return RedirectResponse("/admin/categorias", status_code=303)
    except ValidationError as e:
        erros = []
        for erro in e.errors():
            mensagem = erro['msg']
            if mensagem.startswith("Value error, ",):
                mensagem = mensagem.replace("Value error, ", "")
            erros.append(mensagem)
        erro_msg = " | ".join(erros)
        informar_erro(request, f"Há erros no formulário")
        print(f"Erros de validação: {erro_msg}")
        return templates.TemplateResponse("admin/categorias/inserir_categoria.html", {
            "request": request,
            "erro": erro_msg,
            "dados": dados_originais  # Preservar dados digitados
        })
    except Exception as e:
        # logger.error(f"Erro ao processar cadastro: {e}")
        print(f"Erro ao processar cadastro: {e}")
        return templates.TemplateResponse("admin/categorias/inserir_categoria.html", {
            "request": request,
            "erro": "Erro ao processar cadastro. Tente novamente.",
            "dados": dados_originais
        })


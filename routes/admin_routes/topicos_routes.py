from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from pydantic_core import ValidationError as PydanticCoreValidationError
from typing import Optional

from data.topico import topico_repo
from data.categoria import categoria_repo
from data.topico.topico_model import Topico
from dtos.topicos_dto import InserirTopicoDTO, AtualizarTopicoDTO
from util.auth_decorator import requer_autenticacao
from util.flash_messages import informar_erro, informar_sucesso

router = APIRouter()
templates = Jinja2Templates(directory="templates")


# ==================== LISTAGEM DE TÓPICOS ====================
@router.get("/admin/topicos")
@requer_autenticacao(["admin"])
async def get_topicos(request: Request, categoria: Optional[int] = None, usuario_logado: dict = None):
    categorias = categoria_repo.obter_categorias()
    
    # Verifica se categoria foi passada e é válida
    if categoria is not None and categoria > 0:
        topicos = topico_repo.obter_topico_por_categoria_paginado(categoria, 1, 100)
        categoria_selecionada = categoria
    else:
        topicos = topico_repo.obter_topicos()
        categoria_selecionada = None
    
    response = templates.TemplateResponse(
        "admin/topicos/topicos.html",
        {
            "request": request,
            "usuario": usuario_logado,
            "topicos": topicos,
            "categorias": categorias,
            "categoria_selecionada": categoria_selecionada
        }
    )
    return response


@router.post("/admin/topicos")
@requer_autenticacao(["admin"])
async def post_topicos(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse(
        "admin/topicos/topicos.html",
        {"request": request, "usuario": usuario_logado}
    )
    return response


# ==================== INSERIR TÓPICO ====================
@router.get("/admin/topicos/inserir-topico")
@requer_autenticacao(["admin"])
async def get_inserir_topico(request: Request, usuario_logado: dict = None):
    categorias = categoria_repo.obter_categorias()
    response = templates.TemplateResponse(
        "admin/topicos/inserir_topico.html",
        {
            "request": request,
            "usuario": usuario_logado,
            "categorias": categorias
        }
    )
    return response


@router.post("/admin/topicos/inserir-topico")
@requer_autenticacao(["admin"])
async def post_inserir_topico(
    request: Request,
    usuario_logado: dict = None,
    nome: str = Form(...),
    idCategoria: int = Form(...)
):
    categorias = categoria_repo.obter_categorias()
    dados_originais = {"nome": nome, "idCategoria": idCategoria}
    
    try:
        dados = InserirTopicoDTO(nome=nome, idCategoria=idCategoria)
        novo_topico = Topico(id=0, nome=dados.nome, idCategoria=dados.idCategoria)
        topico_repo.inserir_topico(novo_topico)
        informar_sucesso(request, f"Tópico inserido com sucesso.")
        return RedirectResponse("/admin/topicos", status_code=303)
    except (ValidationError, PydanticCoreValidationError) as e:
        erros = []
        for erro in e.errors():
            mensagem = erro['msg']
            if mensagem.startswith("Value error, "):
                mensagem = mensagem.replace("Value error, ", "")
            erros.append(mensagem)
        erro_msg = " | ".join(erros)
        informar_erro(request, f"Há erros no formulário")
        return templates.TemplateResponse(
            "admin/topicos/inserir_topico.html",
            {
                "request": request,
                "erro": erro_msg,
                "dados": dados_originais,
                "categorias": categorias,
                "usuario": usuario_logado
            }
        )
    except Exception as e:
        print(f"Erro ao processar cadastro: {e}")
        return templates.TemplateResponse(
            "admin/topicos/inserir_topico.html",
            {
                "request": request,
                "erro": "Erro ao processar cadastro. Tente novamente.",
                "dados": dados_originais,
                "categorias": categorias,
                "usuario": usuario_logado
            }
        )


# ==================== ALTERAR TÓPICO ====================
@router.get("/admin/topicos/alterar-topico/{id}")
@requer_autenticacao(["admin"])
async def get_alterar_topico(request: Request, id: int = None, usuario_logado: dict = None):
    categorias = categoria_repo.obter_categorias()
    topico = topico_repo.obter_topico_por_id(id)
    response = templates.TemplateResponse(
        "admin/topicos/alterar_topico.html",
        {
            "request": request,
            "usuario": usuario_logado,
            "categorias": categorias,
            "topico": topico
        }
    )
    return response


@router.post("/admin/topicos/alterar-topico/{id}")
@requer_autenticacao(["admin"])
async def post_alterar_topico(
    request: Request,
    id: int = None,
    usuario_logado: dict = None,
    nome: str = Form(...),
    idCategoria: int = Form(...)
):
    categorias = categoria_repo.obter_categorias()
    topico = topico_repo.obter_topico_por_id(id)
    dados_originais = {"nome": nome, "idCategoria": idCategoria}
    
    try:
        dados = AtualizarTopicoDTO(nome=nome, idCategoria=idCategoria)
        topico_repo.atualizar_topico_por_id(id, dados.nome, dados.idCategoria)
        informar_sucesso(request, f"Tópico atualizado com sucesso.")
        return RedirectResponse(url="/admin/topicos", status_code=303)
    except (ValidationError, PydanticCoreValidationError) as e:
        erros = []
        for erro in e.errors():
            mensagem = erro['msg']
            if mensagem.startswith("Value error, "):
                mensagem = mensagem.replace("Value error, ", "")
            erros.append(mensagem)
        erro_msg = " | ".join(erros)
        print(f"Erros de validação: {erro_msg}")
        informar_erro(request, f"Há erros no formulário")
        return templates.TemplateResponse(
            "admin/topicos/alterar_topico.html",
            {
                "request": request,
                "usuario": usuario_logado,
                "categorias": categorias,
                "topico": topico,
                "erro": erro_msg
            }
        )
    except Exception as e:
        print(f"Erro ao processar cadastro: {e}")
        return templates.TemplateResponse(
            "admin/topicos/alterar_topico.html",
            {
                "request": request,
                "usuario": usuario_logado,
                "categorias": categorias,
                "topico": topico,
                "erro": "Erro ao processar cadastro. Tente novamente."
            }
        )


# ==================== EXCLUIR TÓPICO ====================
@router.get("/admin/topicos/excluir-topico/{id}")
@requer_autenticacao(["admin"])
async def get_excluir_topico(request: Request, id: int = None, usuario_logado: dict = None):
    topico = topico_repo.obter_topico_por_id(id)
    response = templates.TemplateResponse(
        "admin/topicos/excluir_topico.html",
        {
            "request": request,
            "usuario": usuario_logado,
            "topico": topico
        }
    )
    return response


@router.post("/admin/topicos/excluir-topico/{id}")
@requer_autenticacao(["admin"])
async def post_excluir_topico(request: Request, id: int = None, usuario_logado: dict = None):
    try:
        if topico_repo.excluir_topico_por_id(id):
            informar_sucesso(request, "Tópico excluído com sucesso.")
        else:
            informar_erro(request, "Erro ao excluir tópico.")
        return RedirectResponse(url="/admin/topicos", status_code=303)
    except Exception as e:
        print(f"Erro ao excluir tópico: {e}")
        informar_erro(request, "Erro ao excluir tópico. Tente novamente.")
        return RedirectResponse(url="/admin/topicos", status_code=303)
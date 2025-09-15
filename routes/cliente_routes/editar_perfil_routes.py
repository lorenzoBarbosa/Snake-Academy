from datetime import datetime
from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.usuario.usuario_repo import * 
from util.auth_decorator import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/editar-perfil")
@requer_autenticacao(["cliente"])
async def get_editar_perfil(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("cliente/editar_perfil.html", {"request": request, "usuario": usuario_logado})
    return response

@router.post("/cliente/editar-perfil")
@requer_autenticacao(["cliente"])
async def post_editar_perfil(request: Request,
                            usuario_logado: dict = None,
                            nome: str = Form(...),
                            email: str = Form(...),
                            telefone: str = Form(...),
                            data_nascimento: str = Form(...)):

    try:
        usuario = Usuario(
            id=0,
            nome=nome,
            email=email,
            senha=None,
            telefone=telefone,
            dataNascimento=data_nascimento,
            perfil='cliente',
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None
        )
        
        atualizar_usuario_por_email(usuario, usuario_logado.get("email"))
        cliente = cliente_repo.obter_cliente_por_id(usuario_logado.get("id"))
    
        cliente = Cliente(
            id=cliente.id,
            nome=cliente.nome,
            email=cliente.email,
            senha=None,
            telefone=cliente.telefone,
            dataNascimento=cliente.dataNascimento,
            perfil=usuario.perfil,
            token_redefinicao=cliente.token_redefinicao,
            data_token=cliente.data_token,
            data_cadastro=cliente.data_cadastro,
            dataUltimoAcesso=cliente.dataUltimoAcesso,
            statusConta=cliente.statusConta,
            historicoCursos= cliente.historicoCursos,
            indentificacaoProfessor= cliente.indentificacaoProfessor,
        )
        cliente_repo.atualizar_cliente_por_id(cliente, usuario.id)

        # Fazer login automático após cadastro
        usuario_dict = {
            "id": cliente.id,
            "nome": cliente.nome,
            "email": cliente.email,
            "telefone": cliente.telefone,
            "dataNascimento": cliente.dataNascimento,
            "perfil": 'cliente',
        }
        criar_sessao(request, usuario_dict)

        return RedirectResponse(f"/cliente", status.HTTP_303_SEE_OTHER)

    except Exception as e:
        return templates.TemplateResponse(
            "cliente/editar-perfil.html",
            {
                "request": request,
                "erro": f"Erro ao criar cadastro. Tente novamente. {e}",
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "dataNascimento": data_nascimento,
                "perfil": "cliente"
            }
        )

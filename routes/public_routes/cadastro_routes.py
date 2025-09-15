from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.util import get_connection

from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from datetime import datetime

from util.auth_decorator import *
from util.security import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cadastro")
async def get_cadastro(request: Request):
    if esta_logado(request):
        return RedirectResponse("/", status.HTTP_303_SEE_OTHER)

    return templates.TemplateResponse("publico/cadastro.html", {"request": request})

@router.post("/cadastro")
async def post_cadastro(
    request: Request,
    nome: str = Form(...), 
    email: str = Form(...), 
    senha: str = Form(...),  
    confirmar_senha: str = Form(...), 
    telefone: str = Form(...),
    dataNascimento: str = Form(...),
    perfil: str = Form("cliente")):

    if senha != confirmar_senha:
        return templates.TemplateResponse(
            "publico/cadastro.html",
            {
                "request": request,
                "erro": "As senhas não coincidem",
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "dataNascimento": dataNascimento,
                "perfil": perfil
            }
        )
    
    senha_valida, msg_erro = validar_forca_senha(senha)  
    if not senha_valida:
        return templates.TemplateResponse(
            "publico/cadastro.html",
            {
                "request": request,
                "erro": msg_erro,
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "dataNascimento": dataNascimento,
                "perfil": perfil
            }
        ) 
    
    if usuario_repo.obter_usuario_por_email(email):
        return templates.TemplateResponse(
            "publico/cadastro.html",
            {
                "request": request,
                "erro": "Este email já está cadastrado",
                "nome": nome,
                "telefone": telefone,
                "dataNascimento": dataNascimento,
                "perfil": perfil
            }
        )
    
    
    try:
        # Criar usuário com senha hash
        usuario = Usuario(
            id=0,
            nome=nome,
            email=email,
            senha=criar_hash_senha(senha),
            telefone=telefone,
            dataNascimento=dataNascimento,
            perfil='cliente',
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now().isoformat()
        )
        
        usuario_id = usuario_repo.inserir_usuario(usuario)
        
        # Inserir dados do cliente
        cliente = Cliente(
            id=usuario_id,
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            dataNascimento=dataNascimento,
            perfil='cliente',
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now().isoformat(),
            dataUltimoAcesso=None,
            statusConta='ativo',
            historicoCursos= [],
            indentificacaoProfessor= False,
        )
        cliente_repo.inserir_cliente(cliente, usuario_id)

        # Fazer login automático após cadastro
        usuario_dict = {
            "id": usuario_id,
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "dataNascimento": dataNascimento,
            "perfil": 'cliente',
        }
        criar_sessao(request, usuario_dict)

        return RedirectResponse(f"/cliente/editar-perfil", status.HTTP_303_SEE_OTHER)

    except Exception as e:
        return templates.TemplateResponse(
            "publico/cadastro.html",
            {
                "request": request,
                "erro": f"Erro ao criar cadastro. Tente novamente. {e}",
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "dataNascimento": dataNascimento,
                "perfil": perfil
            }
        )

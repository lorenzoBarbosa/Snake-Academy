from fastapi import APIRouter, Request, logger
from fastapi.params import Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic_core import ValidationError
from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.util import get_connection

from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from datetime import datetime

from dtos.cadastro_dto import CadastroDTO
from util.auth_decorator import *
from util.flash_messages import informar_sucesso
from util.security import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cadastro")
async def get_cadastro(request: Request):
    if esta_logado(request):
        return RedirectResponse("/", status.HTTP_303_SEE_OTHER)

    return templates.TemplateResponse("publico/cadastro.html", {"request": request, "dados": {}})

@router.post("/cadastro")
async def post_cadastro(
            request: Request,
            nome: str = Form(...), 
            email: str = Form(...), 
            senha: str = Form(...),  
            confirmar_senha: str = Form(...), 
            telefone: str = Form(...),
            data_nascimento: str = Form(...),
            perfil: str = Form("cliente")):
    
    dados_formulario = {
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "data_nascimento": data_nascimento,
    }

    # Verificar se email já existe
    if usuario_repo.obter_usuario_por_email(email):
        return templates.TemplateResponse(
            "publico/cadastro.html",
            {
                "request": request,
                "dados": dados_formulario,
                "erros": {"EMAIL": "E-mail já cadastrado"}
            }
        )
    try:
        cadastro_dto = CadastroDTO(
            nome=nome,
            email=email,
            senha=senha,
            confirmar_senha=confirmar_senha,
            telefone=telefone,
            data_nascimento=data_nascimento
        )

        # Criar usuário com senha hash
        usuario = Usuario(
            id=0,
            nome=cadastro_dto.nome,
            email=cadastro_dto.email,
            senha=criar_hash_senha(cadastro_dto.senha),
            telefone=cadastro_dto.telefone,
            dataNascimento=cadastro_dto.data_nascimento,
            perfil='cliente',
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now().isoformat(),
            foto=None
        )
        
        usuario_id = usuario_repo.inserir_usuario(usuario)
        
        # Inserir dados do cliente
        cliente = Cliente(
            id=usuario_id,
            nome=nome,
            email=email,
            senha=senha,
            telefone=telefone,
            dataNascimento=data_nascimento,
            perfil='cliente',
            token_redefinicao=None,
            data_token=None,
            data_cadastro=datetime.now().isoformat(),
            foto = None,
            dataUltimoAcesso=None,
            statusConta='ativo',
            historicoCursos= [],
            indentificacaoProfessor= False,
        )
        cliente_repo.inserir_cliente(cliente, usuario_id)

        # Fazer login automático após cadastro
        usuario_dict = {
            "id": cliente.id,
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "dataNascimento": data_nascimento,
            "perfil": 'cliente',
            "foto": None
        }
        
         # Sucesso - Redirecionar com mensagem flash
        informar_sucesso(request, f"Cadastro realizado com sucesso! Bem-vindo(a), {nome}!")
        criar_sessao(request, usuario_dict)
        return RedirectResponse(f"/cliente/editar-perfil", status.HTTP_303_SEE_OTHER)
        
        
        
    except ValidationError as e:
        # Extrair mensagens de erro do Pydantic
        erros = dict()
        for erro in e.errors():
            campo = erro['loc'][0] if erro['loc'] else 'campo'
            mensagem = erro['msg']
            erros[campo.upper()] = mensagem.replace('Value error, ', '')

        #logger.warning(f"Erro de validação no cadastro: {erro_msg}")

        # Retornar template com dados preservados e erro
        print(f"Erro de validação: {e}")
        return templates.TemplateResponse("publico/cadastro.html", {
            "request": request,
            "erros": erros,
            "dados": dados_formulario  # Preservar dados digitados
        })

    except Exception as e:
        #logger.error(f"Erro ao processar cadastro: {e}")
        print(f"Algo deu errado: {e}")

        return templates.TemplateResponse("publico/cadastro.html", {
            "request": request,
            "erros": {"GERAL": "Erro ao processar cadastro. Tente novamente."},
            "dados": dados_formulario
        })

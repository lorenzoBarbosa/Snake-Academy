from datetime import datetime
from fastapi import APIRouter, File, Request, UploadFile
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.usuario import usuario_repo
from data.usuario.usuario_repo import * 
from util.auth_decorator import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cliente/editar-perfil")
@requer_autenticacao(["cliente", 'professor', 'admin'])
async def get_editar_perfil(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("cliente/editar_perfil.html", {"request": request, "usuario": usuario_logado})
    return response

@router.post("/cliente/editar-perfil")
@requer_autenticacao(["cliente", 'professor', 'admin'])
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
            data_cadastro=None,
            foto=None
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
            foto=usuario.foto,
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
            "foto": cliente.foto
        }
        criar_sessao(request, usuario_dict)

        return RedirectResponse(f"/cliente", status.HTTP_303_SEE_OTHER)

    except Exception as e:
        return templates.TemplateResponse(
            "cliente/editar_perfil.html",
            {
                "request": request,
                "usuario": usuario_logado,
                "erro": f"Erro ao editar perfil. Tente novamente. {e}",
                "nome": nome,
                "email": email,
                "telefone": telefone,
                "dataNascimento": data_nascimento,
                "perfil": "cliente"
            }
        )

@router.post("/cliente/editar-perfil/alterar-foto")
@requer_autenticacao(["cliente", 'professor', 'admin'])
async def alterar_foto(request: Request,
                    usuario_logado: dict = None,
                    foto: UploadFile = File(...)):
    # 1. Validar tipo de arquivo
    tipos_permitidos = ["image/jpeg", "image/png", "image/jpg"]
    if foto.content_type not in tipos_permitidos:
        return templates.TemplateResponse("cliente/editar_perfil.html",{"request": request, "usuario": usuario_logado, "erro": f"Erro ao salvar a foto. Tente novamente."})

    # 2. Criar diretório se não existir
    upload_dir = "static/uploads/usuarios"
    os.makedirs(upload_dir, exist_ok=True)

    # 3. Gerar nome único para evitar conflitos
    import secrets
    extensao = foto.filename.split(".")[-1]
    nome_arquivo = f"{usuario_logado['id']}_{secrets.token_hex(8)}.{extensao}"
    caminho_arquivo = os.path.join(upload_dir, nome_arquivo)

    # 4. Salvar arquivo no sistema
    try:
        conteudo = await foto.read()  # ← Lê conteúdo do arquivo
        with open(caminho_arquivo, "wb") as f:
            f.write(conteudo)

        # 5. Salvar caminho no banco de dados
        caminho_relativo = f"/static/uploads/usuarios/{nome_arquivo}"
        usuario_repo.atualizar_foto(usuario_logado['id'], caminho_relativo)

        # 6. Atualizar sessão do usuário
        usuario_logado['foto'] = caminho_relativo
        usuario_dict = {
            "id": usuario_logado['id'],
            "nome": usuario_logado['nome'],
            "email": usuario_logado['email'],
            "perfil": usuario_logado['perfil'],
            "foto": usuario_logado['foto']
        }
        from util.auth_decorator import criar_sessao
        criar_sessao(request, usuario_dict)

    except Exception as e:
        return templates.TemplateResponse("cliente/editar_perfil.html",{"request": request, "usuario": usuario_logado, "erro": f"Erro ao salvar a foto. Tente novamente. {e}"})

    return templates.TemplateResponse("cliente/editar_perfil.html",{"request": request, "usuario": usuario_logado})

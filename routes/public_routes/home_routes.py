from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.admin.admin_repo import *
from data.banner.banner_repo import *
from data.cliente.cliente_repo import *
from data.usuario.usuario_repo import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")

criar_tabela_usuario()
criar_tabela_admin()
criar_tabela_banner()
criar_tabela_cliente()

quantidade_usuario = obter_quantidade_usuario()
if quantidade_usuario == 0:
    for u in range(3):
        usuario = Usuario(id=0, nome=f"Usuário {u}", email=f"usuario{u}@exemplo.com", senha="senha123", telefone="123456789", dataCriacao='2023-01-01')
        id = inserir_usuario(usuario)

    id_admin = inserir_admin(id=usuario.id, admin= Admin(id=usuario.id, nome= usuario.nome, email=usuario.email, senha=usuario.senha, telefone=usuario.telefone, dataCriacao=usuario.dataCriacao, nivelAcesso=1))

    for i in range(3):
        inserir_banner(Banner(id=0, idAdmin=id_admin, status="ativo"))



@router.get("/")
async def get_root():
    banners = obter_todos_banners()
    response = templates.TemplateResponse("publico/home.html", {"request": {}, "banners": banners})
    return response


    
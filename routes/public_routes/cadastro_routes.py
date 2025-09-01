from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cadastro")
async def get_cadastro():
    response = templates.TemplateResponse("publico/cadastro.html", {"request": {}})
    return response

@router.post("/cadastro")
async def post_cadastro(nome: str, email: str, senha: str,  confirmar_senha: str, telefone: str):
    if senha != confirmar_senha:
        data_criacao = datetime.now()
        usuario = Usuario(id=0,nome=nome,email=email,senha=senha,telefone=telefone,dataCriacao=data_criacao.strftime("%Y-%m-%d %H:%M:%S"))
        resultado = usuario_repo.inserir_usuario(usuario)
        if resultado is not None:
            response = templates.TemplateResponse("publico/cadastro.html", {"request": {}, "menssagem": "Usuário cadastrado com sucesso!"})
        else:
            response = templates.TemplateResponse("publico/cadastro.html", {"request": {}, "mensagem": "Erro ao cadastrar usuário."})
        return response
    else:
        response = templates.TemplateResponse("publico/cadastro.html", {"request": {}, "mensagem": "As senhas não coincidem."})
        return response
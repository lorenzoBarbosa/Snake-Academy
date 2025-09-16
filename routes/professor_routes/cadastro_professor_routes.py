from fastapi import APIRouter, Request
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

from data.cliente import cliente_repo
from data.professor import professor_repo
from data.professor.professor_model import Professor
from data.usuario import usuario_repo
from util.auth_decorator import *
from datetime import datetime

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cadastro-professor")
@requer_autenticacao(["cliente", "professor", "admin"])
async def get_cadastro_professor(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("professor/cadastro_professor.html", {"request": request, "usuario": usuario_logado})
    return response

@router.post("/professor/cadastro-professor")
@requer_autenticacao(["cliente", "professor", "admin"])
async def post_cadastro_professor(request: Request,
                                usuario_logado: dict = None,
                                descricao: str = Form(...)):
    try:
        cliente = cliente_repo.obter_cliente_por_id(usuario_logado.get("id"))
        usuario_repo.atualizar_perfil(usuario_logado.get("id"), perfil="professor")
        dataCriacaoProfessor = datetime.now().strftime("%d/%m/%Y %H:%M:%S") 
        professor = Professor(
            id= cliente.id,
            nome= cliente.nome,
            email= cliente.email,
            senha= cliente.senha ,
            telefone= cliente.telefone,
            dataNascimento= cliente.dataNascimento,
            perfil= "professor",
            token_redefinicao= None,
            data_token= None,
            data_cadastro= None,
            dataUltimoAcesso = None,
            statusConta = cliente.statusConta,
            historicoCursos= cliente.historicoCursos,
            indentificacaoProfessor= True,
            cursosPostados=[],
            quantidadeAlunos=0,
            dataCriacaoProfessor=dataCriacaoProfessor,
            descricaoProfessor=descricao
        )

        professor_repo.inserir_professor(professor, usuario_logado.get("id"))

        return RedirectResponse(f"/professor", status.HTTP_303_SEE_OTHER)

    except Exception as e:
        return templates.TemplateResponse(
            "professor/cadastro-professor.html",
            {
                "request": request,
                "erro": f"Algo deu errado... Tente novamente. {e}",
                "usuario": usuario_logado
            }
        )


    

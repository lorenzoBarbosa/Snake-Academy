from datetime import datetime
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic_core import ValidationError
from fastapi.params import Form
from data.curso.curso_model import Curso
from data.curso.curso_repo import inserir_curso
from data.topico.topico_repo import obter_topicos
from dtos.curso_dto import CursoDTO
from util.auth_decorator import requer_autenticacao
from util.flash_messages import informar_sucesso

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/professor/cursos/criar-curso")
@requer_autenticacao(["professor"])
async def get_criar_curso(request: Request, usuario_logado: dict = None):
    usuario_logado["indentificacaoProfessor"] = True
    topicos = obter_topicos()
    response = templates.TemplateResponse(
        "professor/cursos/criar_curso.html", 
        {
            "request": request, 
            "usuario": usuario_logado, 
            "topicos": topicos
        }
    )
    return response

@router.post("/professor/cursos/criar-curso")
@requer_autenticacao(["professor"])
async def post_criar_curso(
    request: Request,
    titulo: str = Form(...),
    custo: float = Form(...),
    descricao: str = Form(...),
    topico_id: int = Form(...),
    usuario_logado: dict = None
):
    dados_formulario = {
        "titulo": titulo,
        "custo": custo,
        "descricao": descricao,
        "topico_id": topico_id
    }

    try:
        # Validação usando DTO
        cursoDTO = CursoDTO(
            titulo=titulo,
            custo=custo,
            descricao=descricao,
            topico_id=topico_id
        )

        # Criar objeto Curso
        curso = Curso(
            id=0,
            idTopico=cursoDTO.topico_id,
            nome=cursoDTO.titulo,
            idProfessor=usuario_logado["id"],
            custo=cursoDTO.custo,
            descricaoCurso=cursoDTO.descricao,
            duracaoCurso=0,
            avaliacao="0",
            dataCriacao=datetime.now().isoformat(),
            statusCurso=True
        )

        # Inserir no banco
        inserir_curso(curso)
        
        # Mensagem de sucesso
        informar_sucesso(request, "Curso criado com sucesso!")
        
        # Redirecionar para lista de cursos ou página de sucesso
        return RedirectResponse(
            url="/professor/cursos",  # Ajuste para sua rota
            status_code=303
        )

    except ValidationError as e:
        erros = {}
        for err in e.errors():
            campo = err['loc'][0]
            mensagem = err['msg']
            erros[campo.upper()] = mensagem

        return templates.TemplateResponse(
            "professor/cursos/criar_curso.html",
            {
                "request": request,
                "usuario": usuario_logado,
                "topicos": obter_topicos(),
                "dados": dados_formulario,
                "erros": erros
            }
        )
    
    except Exception as e:
        print(f"Erro ao criar curso: {e}")
        return templates.TemplateResponse(
            "professor/cursos/criar_curso.html",
            {
                "request": request,
                "usuario": usuario_logado,
                "topicos": obter_topicos(),
                "dados": dados_formulario,
                "erros": {"GERAL": f"Ocorreu um erro ao criar o curso: {str(e)}"}
            }
        )
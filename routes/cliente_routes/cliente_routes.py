from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from data.banner import banner_repo
from data.categoria.categoria_repo import *
from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.curso.curso_repo import *
from data.topico.topico_repo import *
from util.auth_decorator import *

router = APIRouter()
templates = Jinja2Templates(directory="templates")
rotas_banners=[]

banners = banner_repo.obter_todos_banners()
for banner in banners:
        rota = get_image_filename("carrossel", banner.id)
        rotas_banners.append(rota)


topicos = obter_topicos()

categorias = obter_categorias()
cursos1 = obter_curso_por_topico(1)
cursos2 = obter_curso_por_topico(2)
cursos3 = obter_curso_por_topico(3)
cursos4 = obter_curso_por_topico(4)
cursos = obter_todos_cursos()

rotas_cursos = []
for curso in cursos:
    rota = get_image_filename("nossos_cursos", curso.id)
    rotas_cursos.append(rota)



@router.get("/cliente")
@requer_autenticacao(["cliente", "professor", "admin"])
async def get_cliente(request: Request, usuario_logado: dict = None):

    cliente = cliente_repo.obter_cliente_por_id(usuario_logado.get("id"))
    lista_historico = []
    if cliente.historicoCursos:
        for curso_id in cliente.historicoCursos:
            curso = obter_curso_por_id(curso_id)
            if curso:
                lista_historico.append(curso)

    print(usuario_logado.get("foto"))
    return templates.TemplateResponse("cliente/cliente.html", {"request": request,                                      
                                                                "usuario":usuario_logado,
                                                                "categorias": categorias, 
                                                                "cursos1": cursos1, 
                                                                "cursos2": cursos2, 
                                                                "cursos3": cursos3, 
                                                                "cursos4": cursos4, 
                                                                "cursos": cursos,
                                                                "imagem_cursos": rotas_cursos,
                                                                "rotas": rotas_banners,
                                                                "cliente": cliente,
                                                                "lista_historico": lista_historico})

@router.get("/cliente/logout")
@requer_autenticacao(["cliente", "professor", "admin"])
async def get_logout(request: Request, usuario_logado: dict = None):
    destruir_sessao(request)
    return RedirectResponse(f"/", status.HTTP_303_SEE_OTHER)
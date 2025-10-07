from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.admin.admin_repo import *
from data.banner.banner_repo import *
from data.categoria.categoria_repo import *
from data.cliente.cliente_repo import *
from data.curso.curso_repo import *
from data.professor.professor_repo import *
from data.topico.topico_repo import *
from data.usuario import usuario_repo
from data.usuario.usuario_repo import *

import os

from util.auth_decorator import get_image_filename
from util.criar_admin import criar_admin_padrao
from util.criar_dados import criar_dados_iniciais

router = APIRouter()
templates = Jinja2Templates(directory="templates")

qtd = usuario_repo.obter_quantidade_usuario()
criar_dados_iniciais(qtd=qtd)

@router.get("/")
async def get_root():
    categorias = obter_categorias()
    cursos1 = obter_curso_por_topico(1)
    cursos2 = obter_curso_por_topico(2)
    cursos3 = obter_curso_por_topico(3)
    cursos4 = obter_curso_por_topico(4)
    cursos = obter_todos_cursos()
    banners = obter_todos_banners()

    rotas_cursos = []
    for curso in cursos:
        rota = get_image_filename("nossos_cursos", curso.id)
        rotas_cursos.append(rota)
    response = templates.TemplateResponse("publico/home.html", {"request": {},
                                                                "banners": banners, 
                                                                "categorias": categorias, 
                                                                "cursos1": cursos1, 
                                                                "cursos2": cursos2, 
                                                                "cursos3": cursos3, 
                                                                "cursos4": cursos4, 
                                                                "cursos": cursos,
                                                                "imagem_cursos": rotas_cursos})
    return response


    
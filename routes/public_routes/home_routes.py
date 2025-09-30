from fastapi import APIRouter
from fastapi.templating import Jinja2Templates

from data.admin.admin_repo import *
from data.banner.banner_repo import *
from data.categoria.categoria_repo import *
from data.cliente.cliente_repo import *
from data.curso.curso_repo import *
from data.professor.professor_repo import *
from data.topico.topico_repo import *
from data.usuario.usuario_repo import *

import os

from util.auth_decorator import get_image_filename
from util.criar_admin import criar_admin_padrao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

criar_tabela_usuario()
criar_tabela_admin()
criar_tabela_banner()
criar_tabela_cliente()
criar_tabela_professor()
criar_tabela_categoria()
criar_tabela_topico()
criar_tabela_curso()

quantidade_usuario = obter_quantidade_usuario()
if quantidade_usuario == 0:
    criar_admin_padrao()
    usuarios = obter_todos_usuarios()
    for usuario in usuarios:
        if usuario.perfil == "admin":
            admin = inserir_admin(Admin(id=0, nome=usuario.nome, email=usuario.email, senha=usuario.senha, telefone=usuario.telefone, dataNascimento=usuario.dataNascimento, perfil="admin", token_redefinicao=None, data_token=None, data_cadastro=None, foto=None, nivelAcesso=3), 1)
    
    for i in range(3):
        inserir_banner(Banner(id=0, idAdmin=admin, status=True))

    inserir_categoria(Categoria(id=0, nome="Ciência de Dados"))
    inserir_categoria(Categoria(id=0, nome="Gestão de Redes"))
    inserir_categoria(Categoria(id=0, nome="Desenvolvimento Web"))
    inserir_categoria(Categoria(id=0, nome="Inteligência Artificial"))

    inserir_topico(Topico(id=0, idCategoria=1, nome="Python"))
    inserir_topico(Topico(id=0, idCategoria=1, nome="R"))
    inserir_topico(Topico(id=0, idCategoria=2, nome="Redes de Computadores"))
    inserir_topico(Topico(id=0, idCategoria=3, nome="HTML e CSS"))
    inserir_topico(Topico(id=0, idCategoria=3, nome="JavaScript"))
    inserir_topico(Topico(id=0, idCategoria=4, nome="Machine Learning"))
    inserir_topico(Topico(id=0, idCategoria=4, nome="Deep Learning"))

    id_cliente = inserir_cliente(Cliente(id=0, nome="João Souza", email="joao.souza@exemplo.com", senha="senha123", telefone="123456789", dataNascimento='2023-01-01', perfil="cliente", token_redefinicao=None, data_token=None, data_cadastro=None, foto=None, dataUltimoAcesso=None, statusConta="ativo", historicoCursos=[], indentificacaoProfessor="sim"), usuario.id)
    cliente = obter_cliente_por_id(id_cliente)

    inserir_professor(Professor(id=cliente.id, nome=cliente.nome, email=cliente.email, senha=cliente.senha, telefone=cliente.telefone, dataNascimento=cliente.dataNascimento, perfil=cliente.perfil, token_redefinicao=cliente.token_redefinicao, data_token=cliente.data_token, data_cadastro=cliente.data_cadastro, foto=None, statusConta=cliente.statusConta, historicoCursos=cliente.historicoCursos, indentificacaoProfessor=cliente.indentificacaoProfessor, dataUltimoAcesso=None, cursosPostados=[], quantidadeAlunos=0, dataCriacaoProfessor='2023-01-01', descricaoProfessor="Professor de python que sabe demais, muito muito muito muito muito muito muito muito muio mesmo!"), id_cliente)

    for c in range(8):
        inserir_curso(Curso(id=0,
                        idTopico=1,
                        nome="Introdução ao Python",
                        idProfessor=1, 
                        custo=199.99,
                        descricaoCurso="Aprenda os fundamentos do Python jiPIWEHHHHHHGaldhifÇDHIOhdfhIWDHGIWHGOHighiohgiohdigsiiohgiowhfgóhwfguahfguSHPFGDbspfgobWFBG.",
                        duracaoCurso="4 semanas",
                        avaliacao=4.5, 
                        dataCriacao='2023-01-01', 
                        statusCurso="ativo"))
    
    for c2 in range(8):
        inserir_curso(Curso(id=0,
                        idTopico=3,
                        nome="Gestão maluca de Projetos",
                        idProfessor=1, 
                        custo=199.99,
                        descricaoCurso="Aprenda os fundamentos da gestão sem sentido. njfdnwiojenvijenfvio efjnviodjen vjien vijndf voiadjnfvj abjv bai nfji avoida bfvui badif vbioabdvi bdaifh vba",
                        duracaoCurso="4 semanas",
                        avaliacao=4.5, 
                        dataCriacao='2023-01-01', 
                        statusCurso="ativo"))
    
    for c3 in range(8):
        inserir_curso(Curso(id=0,
                        idTopico=5,
                        nome="HTML e CSS para Iniciantes",
                        idProfessor=1, 
                        custo=199.99,
                        descricaoCurso="Aprenda os fundamentos do HTML e CSS  niashdvahf vuia fhviua fvuia dfuivuiadf viuas dfvbsuid vsbdv sv saivdb saui vbSH V.",
                        duracaoCurso="4 semanas",
                        avaliacao=4.5, 
                        dataCriacao='2023-01-01', 
                        statusCurso="ativo"))
        
    for c4 in range(8):
        inserir_curso(Curso(id=0,
                        idTopico=6,
                        nome="Machine Learning para Iniciantes",
                        idProfessor=1, 
                        custo=199.99,
                        descricaoCurso="Aprenda os fundamentos do Machine Learning.",
                        duracaoCurso="4 semanas", 
                        avaliacao=4.5, 
                        dataCriacao='2023-01-01', 
                        statusCurso="ativo"))

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

@router.get("/")
async def get_root():
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


    
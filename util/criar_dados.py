from data.admin import admin_repo
from data.aula import aula_repo
from data.banner import banner_repo
from data.categoria import categoria_repo
from data.categoria.categoria_model import Categoria
from data.categoria.categoria_repo import inserir_categoria
from data.chamado import chamado_repo
from data.cliente import cliente_repo
from data.cliente.cliente_model import Cliente
from data.cliente.cliente_repo import inserir_cliente, obter_cliente_por_id
from data.comentario_curso import comentario_curso_repo
from data.comunidade import comunidade_repo
from data.curso import curso_repo
from data.curso.curso_model import Curso
from data.curso.curso_repo import inserir_curso
from data.matricula import matricula_repo
from data.mensagem import mensagem_repo
from data.mensagem_comunidade import mensagem_comunidade_repo
from data.modulo import modulo_repo
from data.professor import professor_repo
from data.professor.professor_model import Professor
from data.professor.professor_repo import inserir_professor
from data.progresso import progresso_repo
from data.resposta_chamado import resposta_chamado_repo
from data.topico import topico_repo
from data.topico.topico_model import Topico
from data.topico.topico_repo import inserir_topico
from data.usuario import usuario_repo
from data.usuario.usuario_repo import obter_usuario_por_id
from util.criar_admin import criar_admin_padrao


def criar_dados_iniciais(qtd: int = None) -> bool:
    """Cria dados iniciais no banco de dados"""

    if qtd == 0 or qtd is None:
        try:
            admin_repo.criar_tabela_admin()
            aula_repo.criar_tabela_aula()
            banner_repo.criar_tabela_banner()
            categoria_repo.criar_tabela_categoria()
            chamado_repo.criar_tabela_chamado()
            cliente_repo.criar_tabela_cliente()
            comentario_curso_repo.criar_tabela_comentario_curso()
            comunidade_repo.criar_tabela_comunidade()
            curso_repo.criar_tabela_curso()
            matricula_repo.criar_tabela_matricula()
            mensagem_repo.criar_tabela_mensagem()
            mensagem_comunidade_repo.criar_tabela_mensagem_comunidade()
            modulo_repo.criar_tabela_modulo()
            professor_repo.criar_tabela_professor()
            progresso_repo.criar_tabela_progresso()
            resposta_chamado_repo.criar_tabela_rchamado()
            topico_repo.criar_tabela_topico()
            usuario_repo.criar_tabela_usuario()


            criar_admin_padrao()
            usuario = obter_usuario_por_id(1)
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

            print("Dados iniciais criados com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao criar dados iniciais: {e}")
            return False
    else:
        return True
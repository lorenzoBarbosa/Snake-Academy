import sys
import os
from data.comentario_curso.comentario_curso_repo import *
from data.admin.admin_repo import * 
from data.matricula.matricula_repo import *
from data.curso.curso_repo import *
from data.usuario.usuario_repo import *
from data.cliente.cliente_repo import *
from data.professor.professor_repo import *
from data.categoria.categoria_repo import *
from data.topico.topico_repo import *

class TestComentarioCursoRepo:
    def test_criar_tabela_comentario_curso(self, test_db):
        # Arrange
        criar_tabela_admin()
        criar_tabela_usuario()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_cliente()
        criar_tabela_matricula()
        # Act
        resultado = criar_tabela_comentario_curso()
        # Assert
        assert resultado == True, "A criação da tabela de comentários de curso deveria retornar True"

    def test_gerar_comentario_curso(self, test_db):
        # Arrange
        criar_tabela_admin()
        criar_tabela_usuario()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_comentario_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        usuario2 = Usuario(0, "jose", "jose@g", "123", "1234", "12-06-2025")
        usuario2_inserido = inserir_usuario(usuario2)
        admin= Admin(0,"", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario2_inserido)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, f"Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0,cliente_inserido, curso_inserido, "Bom", "Bom", "Completa", "01/02/2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        #Act
        comentario_curso = comentarioCurso(0, admin_inserido, matricula_inserida, "Curso horroroso", "12/07/2025", "13/07/2025")
        comentario_id = gerar_comentario_curso(comentario_curso)
        comentario_db = obter_comentario_curso_por_id(comentario_id)
        #Assert
        assert comentario_db is not None, "O comentário não deveria estar vazio"
        assert comentario_db.idAdmin == admin_inserido, "O ID do admin está incorreto"
        assert comentario_db.idMatricula == matricula_inserida, "O ID da matrícula está incorreto"
        assert comentario_db.conteudo == "Curso horroroso", "O conteúdo do comentário está incorreto"
        assert comentario_db.dataEnvio == "12/07/2025", "A data do comentário está incorreta"
        assert comentario_db.dataSupervisaoAdmin == "13/07/2025", "A data da resposta está incorreta"
    
    def test_obter_comentario_curso_por_id(self, test_db):
        # Arrange
        criar_tabela_admin()
        criar_tabela_usuario()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_comentario_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        usuario2 = Usuario(0, "jose", "jose@g", "123", "1234", "12-06-2025")
        usuario2_inserido = inserir_usuario(usuario2)
        admin= Admin(0,"", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario2_inserido)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, f"Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0,cliente_inserido, curso_inserido, "Bom", "Bom", "Completa", "01/02/2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        comentario_curso = comentarioCurso(0, admin_inserido, matricula_inserida, "Curso horroroso", "12/07/2025", "13/07/2025")
        # Act
        comentario_id = gerar_comentario_curso(comentario_curso)
        comentario_db = obter_comentario_curso_por_id(comentario_id)
        #Assert 
        assert comentario_db is not None, "O comentário não foi obtido"

    def test_obter_comentario_curso(self, test_db):
        # Arrange
        criar_tabela_admin()
        criar_tabela_usuario()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_comentario_curso()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        usuario2 = Usuario(0, "jose", "jose@g", "123", "1234", "12-06-2025")
        usuario2_inserido = inserir_usuario(usuario2)
        admin = Admin(0, "", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario2_inserido)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        inserir_professor(professor, cliente_inserido)
        curso = Curso(0, "Python", 1, 12.99, "", "12:56", "", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        matricula = Matricula(0, cliente_inserido, curso_inserido, "", "", "", "01/02/2025")
        matricula_inserida = inserir_matricula(matricula)
        for i in range(5):
            comentario = comentarioCurso(0, admin_inserido, matricula_inserida, f"Coment {i}", "01/01/2025", "01/02/2025")
            gerar_comentario_curso(comentario)
        # Act
        comentarios = obter_comentario_curso()
        # Assert
        assert comentarios is not None, "A lista de comentários não deveria ser None"
        assert len(comentarios) == 5, "Deveria haver 5 comentários cadastrados"

    def test_excluir_comentario_curso_por_id(self, test_db):
        # Arrange
        criar_tabela_admin()
        criar_tabela_usuario()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_comentario_curso()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        usuario2 = Usuario(0, "jose", "jose@g", "123", "1234", "12-06-2025")
        usuario2_inserido = inserir_usuario(usuario2)
        admin = Admin(0, "", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario2_inserido)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        inserir_professor(professor, cliente_inserido)
        curso = Curso(0, "Python", 1, 12.99, "", "12:56", "", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        matricula = Matricula(0, cliente_inserido, curso_inserido, "", "", "", "01/02/2025")
        matricula_inserida = inserir_matricula(matricula)
        comentario = comentarioCurso(0, admin_inserido, matricula_inserida, "Coment deletar", "01/01/2025", "01/02/2025")
        comentario_id = gerar_comentario_curso(comentario)
        # Act
        excluir_comentario_curso_por_id(comentario_id)
        comentario_excluido = obter_comentario_curso_por_id(comentario_id)
        # Assert
        assert comentario_excluido is None, "O comentário deveria ter sido excluído"




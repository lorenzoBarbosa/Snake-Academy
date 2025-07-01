import sys
import os
from data.comentario_curso.comentario_curso_repo import *
from data.admin.admin_repo import * 
from data.matricula.matricula_repo import *
from data.curso.curso_repo import *
from data.usuario.usuario_repo import *
from data.cliente.cliente_repo import *
from data.professor.professor_repo import *

class TestComentarioCursoRepo:
    def test_criar_tabela_comentario_curso(self, test_db):
        # Arrange
        criar_tabela_admin()
        criar_tabela_usuario()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_cliente()
        criar_tabela_matricula()
        # Act
        resultado = criar_tabela_comentario_curso()
        # Assert
        assert resultado == True, "A criação da tabela de comentários de curso deveria retornar True"

    # def test_gerar_comentario_curso(self, test_db):
    #     # Arrange
    #     criar_tabela_admin()
    #     criar_tabela_usuario()
    #     criar_tabela_professor()
    #     criar_tabela_curso()
    #     criar_tabela_cliente()
    #     criar_tabela_matricula()
    #     criar_tabela_comentario_curso()

    #     admin = Admin(0, "admin", "email.admin@example.com", "senha123", "123456789", "2023-01-01")
    #     admin_id = inserir_admin(admin)
    #     usuario = Usuario(0, "usuario", "email.usuario@example.com", "senha123", "987654321", "2023-01-01")
    #     usuario_id = inserir_usuario(usuario)
    #     curso = Curso(0, "Curso Teste", "Descrição do curso", "2023-01-01", "2023-12-31")
    #     curso_id = inserir_curso(curso)
    #     comentario_curso = comentarioCurso(0, "Comentário de teste", 5, curso_id, usuario_id)
    #     comentario_id = inserir_comentario_curso(comentario)

    #ficou meio complicado, mas o teste de gerar comentário de curso deve ser feito aqui
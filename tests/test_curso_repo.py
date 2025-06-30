import sys
import os

from data.cliente.cliente_repo import *
from data.curso.curso_repo import *
from data.professor.professor_repo import *
from data.usuario.usuario_repo import *

class TestCursoRepo:
    def test_criar_tabela_curso(self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        # Act
        resultado = criar_tabela_curso()
        # Assert 
        assert resultado is True, "A tabela curso não foi criada"
    
    def test_inserir_curso(self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        # Act
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        curso = obter_curso_por_id(curso_inserido)
        nomeProfessor = curso.nomeProfessor
        curso_db = curso.curso
        # Asserts
        assert curso_db is not None, "Não deveria ser vazio"
        assert curso_db.id == curso_inserido, "O id do curso está incorreto"
        assert curso_db.nome == "Python", "O nome do curso está incorreto"
        assert curso_db.idProfessor == 1, "O id do professor está incorreto"
        assert curso_db.custo == 12.99, "O preço do curso está incorreto"
        assert curso_db.descricaoCurso == "não sei", "A descrição do curso está incorreta"
        assert curso_db.duracaoCurso == "12:56", "A duração do curso está incorreta"
        assert curso_db.avaliacao == "Bom", "A avalição do curso está incorreta"
        assert curso_db.dataCriacao == "12-06-2025", "A data de criação do curso está incorreta"
        assert curso_db.statusCurso == True, "O status do curso está incorreto"
    
    def test_obter_todos_cursos(self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_obj1 = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        curso_inserido1 = inserir_curso(curso_obj1)
        # Act
        cursos = obter_todos_cursos()
        # Asserts
        assert len(cursos) == 2, "A quantidade de cursos deveria ser de apenas 2"
    
    def test_obter_cursos_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        for c in range(10):
            curso_obj = Curso(0, f"Python{c+1}", 1, 12.99 + c, "não sei", "12:56", "Bom", "12-06-2025", True)
            curso_inserido = inserir_curso(curso_obj)
        # Act
        cursos1 = obter_cursos_paginado(1, 4)
        cursos2 = obter_cursos_paginado(2, 4)
        cursos3 = obter_cursos_paginado(3, 4)
        # Assert
        assert len(cursos1) == 4, "A primeira página deveria conter 4 cursos"
        assert len(cursos2) == 4, "A segunda página deveria conter 4 cursos"
        curso = obter_curso_por_id(9)
        curso_db = curso.curso
        curso_pagina = cursos3[0].curso
        assert curso_db.id == curso_pagina.id, "O id do curso obtido está incorreto"
    
    def test_obter_curso_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        for c in range(10):
            curso_obj = Curso(0, f"Python{c+1}", 1, 12.99 + c, "não sei", "12:56", "Bom", "12-06-2025", True)
            curso_inserido = inserir_curso(curso_obj)
        # Act
        curso = obter_curso_por_id(2)
        curso_db= curso.curso
        # Assert
        assert curso_db is not None, "O curso não foi obtido"
        assert curso_db.id == 2, "O id obtido deveria ser 2"
    
    def test_obter_cursos_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        for c in range(10):
            curso_obj = Curso(0, f"Python{c+1}", 1, 12.99 + c, "não sei", "12:56", "Bom", "12-06-2025", True)
            curso_inserido = inserir_curso(curso_obj)
        # Act
        cursos1 = obter_cursos_paginado(1, 4)
        cursos2 = obter_cursos_paginado(2, 4)
        cursos3= obter_cursos_paginado(3, 4)
        # Asserts
        assert len(cursos1) == 4, "A quantidade de cursos na primeira página teria que ser 4."
        assert len(cursos2) == 4, "A quantidade de cursos na segunda página teria que ser 4."
        curso_db= cursos3[0]
        curso = curso_db.curso
        assert curso.id == 9, "O id da primeira página deveria ser 9"

    def test_obter_curso_por_termo_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        for c in range(10):
            curso_obj = Curso(0, f"Python{c+1}", 1, 12.99 + c, "não sei", "12:56", "Bom", "12-06-2025", True)
            curso_inserido = inserir_curso(curso_obj)
        # Act
        cursos1 = obter_curso_por_termo_paginado("ython", 1, 4)
        cursos2 = obter_curso_por_termo_paginado("ython", 2, 4)
        cursos3= obter_curso_por_termo_paginado("ython", 3, 4)
        # Asserts
        assert len(cursos1) == 4, "A quantidade de cursos na primeira página teria que ser 4."
        assert len(cursos2) == 4, "A quantidade de cursos na segunda página teria que ser 4."
        curso_db= cursos3[0]
        curso = curso_db.curso
        assert curso.id == 9, "O id da primeira página deveria ser 9"




        

    











    
import sys
import os

from data.cliente.cliente_repo import *
from data.curso.curso_repo import *
from data.professor.professor_repo import *
from data.usuario.usuario_repo import *
from data.categoria.categoria_repo import *
from data.topico.topico_repo import *

class TestCursoRepo:
    def test_criar_tabela_curso(self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        # Act
        resultado = criar_tabela_curso()
        # Assert 
        assert resultado is True, "A tabela curso não foi criada"
    
    def test_inserir_curso(self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        professor_db = obter_professor_por_id(professor_inserido)
        categoria = Categoria(0, "Categoria de cursos de programação")
        categoria_inserida = inserir_categoria(categoria)
        categoria_db = obter_categoria_por_id(categoria_inserida)
        topico = Topico(0, "Python", categoria_db.id)
        topico_inserido = inserir_topico(topico)
        topico_db = obter_topico_por_id(topico_inserido)
        # Act
        curso_obj = Curso(0, topico_db.id, "Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True, )
        curso_inserido = inserir_curso(curso_obj)
        curso_db = obter_curso_por_id(curso_inserido)
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
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        professor_db = obter_professor_por_id(professor_inserido)
        categoria = Categoria(0, "Categoria de cursos de programação")
        categoria_inserida = inserir_categoria(categoria)
        categoria_db = obter_categoria_por_id(categoria_inserida)
        topico1 = Topico(0, "Python", categoria_db.id)
        topico_inserido1 = inserir_topico(topico1)
        topico_db1 = obter_topico_por_id(topico_inserido1)
        topico2 = Topico(0, "Python", categoria_db.id)
        topico_inserido2 = inserir_topico(topico2)
        topico_db2 = obter_topico_por_id(topico_inserido2)
        # Act
        curso_obj1 = Curso(0, topico_db1.id, "Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True, )
        curso_obj2 = Curso(1, topico_db2.id, "Python", professor_db.id, 15.99, "saberemos", "13:56", "Muito Bom", "12-07-2025", True, )
        curso_inserido = inserir_curso(curso_obj1)
        curso_inserido2 = inserir_curso(curso_obj2)
        # Act
        cursos = obter_todos_cursos()
        # Asserts
        assert len(cursos) == 2, "A quantidade de cursos deveria ser de apenas 2"
    
    def test_obter_cursos_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        professor_db = obter_professor_por_id(professor_inserido)
        categoria = Categoria(0, "Categoria de cursos de programação")
        categoria_inserida = inserir_categoria(categoria)
        categoria_db = obter_categoria_por_id(categoria_inserida)
        topico = Topico(0, "Python", categoria_db.id)
        topico_inserido = inserir_topico(topico)
        topico_db = obter_topico_por_id(topico_inserido)
        for c in range(10):
            curso_obj = Curso(0, topico_db.id,f"Python{c+1}", professor_db.id, 12.99 + c, "não sei", "12:56", "Bom", "12-06-2025", True)
            curso_inserido = inserir_curso(curso_obj)
        # Act
        cursos1 = obter_cursos_paginado(1, 4)
        cursos2 = obter_cursos_paginado(2, 4)
        cursos3 = obter_cursos_paginado(3, 4)
        # Assert
        assert len(cursos1) == 4, "A primeira página deveria conter 4 cursos"
        assert len(cursos2) == 4, "A segunda página deveria conter 4 cursos"
        curso = obter_curso_por_id(9)
        assert curso.id == 9, "O id do curso obtido está incorreto"
    
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
        # Assert
        assert curso is not None, "O curso não foi obtido"
        assert curso.id == 2, "O id obtido deveria ser 2"

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
        assert curso_db.id == 9, "O id da primeira página deveria ser 9"

    def test_obter_quantidade_cursos(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)

        for _ in range(5):
            curso = Curso(0, "Python", professor_id, 10.0, "Desc", "10h", "Bom", "01-01-2025", True)
            inserir_curso(curso)

        quantidade = obter_quantidade_cursos()
        assert quantidade == 5, "A quantidade total de cursos deveria ser 5"
    
    def test_obter_quantidade_cursos_por_nome_professor(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario = Usuario(0, "João da Silva", "joao@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "João da Silva", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)

        for _ in range(3):
            curso = Curso(0, "JavaScript", professor_id, 25.0, "Curso", "5h", "Excelente", "02-02-2025", True)
            inserir_curso(curso)

        qtd = obter_quantidade_cursos_por_nome_professor("João da Silva")
        assert qtd == 3, "Deveria haver 3 cursos do professor João da Silva"

    def test_atualizar_curso_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario = Usuario(0, "Maria", "maria@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "Maria", "", "", "", "", "", True, [], True, ["java"], 10, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        curso = Curso(0, "Curso Antigo", professor_id, 100.0, "Antigo", "10h", "Médio", "01-01-2024", True)
        curso_id = inserir_curso(curso)
        curso_db = obter_curso_por_id(curso_id)
        # Act
        curso_db.nome = "Curso Atualizado"
        curso_db.statusCurso = False
        atualizado = atualizar_curso_por_id(curso_db, curso_id)
        curso_atualizado = obter_curso_por_id(curso_id)
        assert atualizado is True, "A atualização do curso deveria retornar True"
        assert curso_atualizado.nome == "Curso Atualizado", "O nome não foi atualizado corretamente"
        assert curso_atualizado.statusCurso == 0, "O status não foi atualizado corretamente"

    def test_excluir_curso_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        usuario = Usuario(0, "Carlos", "carlos@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "Carlos", "", "", "", "", "", True, [], True, ["sql"], 15, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)

        curso = Curso(0, "Curso para Excluir", professor_id, 150.0, "Será excluído", "8h", "Boa", "01-03-2025", True)
        curso_id = inserir_curso(curso)

        resultado = excluir_curso_por_id(curso_id)
        curso_excluido = obter_curso_por_id(curso_id)

        assert resultado is True, "A exclusão deveria retornar True"
        assert curso_excluido is None, "O curso deveria ter sido excluído do banco"








                

            











            
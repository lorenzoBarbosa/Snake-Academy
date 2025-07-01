import sys
import os

from data.cliente.cliente_repo import *
from data.matricula.matricula_repo import *
from data.professor.professor_repo import *
from data.usuario.usuario_repo import *
from data.curso.curso_repo import *


class TestMatriculaRepo:
    def test_criar_tabela_matricula(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_curso()
        #Act
        resultado = criar_tabela_matricula()
        #Asserts
        assert resultado == True, "A tabela não foi criada"
    
    def test_inserir_matricula(self, test_db):
        # Arrange 
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        # Act
        matricula_obj = Matricula( 0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        matricula = obter_matricula_por_id(matricula_inserida)
        # Asserts
        assert matricula is not None, "A matrícula não foi inserida corretamente"
        assert matricula.idMatricula == matricula_inserida, "O id da matrícula está incorreto"
        assert matricula.idCliente == 1, "O id do cliente está incorreto"
        assert matricula.idCurso == 1, "O id do curso está incorreto"
        assert matricula.statusMatricula == "Bom", "O status da matrícula está incorreto"
        assert matricula.desempenho == "Bom", "O desempenho da matrícula está incorreto"
        assert matricula.frequencia == "Bom", "A frequência da matrícula está incorreta"
        assert matricula.dataMatricula == "12-06-2025", "A data da matrícula está incorreta"
        assert matricula.curso is not None, "O curso não foi carregado corretamente"    
        assert matricula.curso.nome == "Python", "O nome do curso na matrícula está incorreto"
        assert matricula.usuario is not None, "O usuário não foi carregado corretamente"        
        assert matricula.usuario.id == 1, "O id do usuário na matrícula está incorreto"
        assert matricula.usuario.nome == "claudio", "O nome do usuário na matrícula está incorreto"

    def test_obter_todas_matriculas(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        # Act
        matriculas = obter_todas_matriculas()
        # Asserts
        assert len(matriculas) > 0, "Não deveria ser vazio"

    def test_obter_matriculas_paginadas(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "2025-06-12")
        id_usuario = inserir_usuario(usuario)

        cliente = Cliente(0, "", "", "", "", "", "2025-06-12", True, [], True)
        id_cliente = inserir_cliente(cliente, id_usuario)

        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "2025-06-12")
        id_professor = inserir_professor(professor, id_cliente)

        curso_obj = Curso(0, "Python", id_professor, 12.99, "não sei", "12:56", "Bom", "2025-06-12", True)
        id_curso = inserir_curso(curso_obj)

        # Inserir múltiplas matrículas
        for _ in range(7):
            matricula_obj = Matricula(0, id_cliente, id_curso, "Bom", "Bom", "Bom", "2025-06-12")
            inserir_matricula(matricula_obj)

        # Act
        page1 = obter_matriculas_paginadas(1, 3)
        page2 = obter_matriculas_paginadas(2, 3)
        page3 = obter_matriculas_paginadas(3, 3)

        # Assert
        assert len(page1) == 3, "Página 1 deveria conter 3 matrículas"
        assert len(page2) == 3, "Página 2 deveria conter 3 matrículas"
        assert len(page3) == 1, "Página 3 deveria conter 1 matrícula"

    def test_obter_matricula_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        # Act
        matricula = obter_matricula_por_id(matricula_inserida)
        # Asserts
        assert matricula is not None, "A matrícula não foi encontrada"
        assert matricula.idMatricula == matricula_inserida, "O id da matrícula está incorreto"
        assert matricula.idCliente == 1, "O id do cliente está incorreto"
        assert matricula.idCurso == 1, "O id do curso está incorreto"
        assert matricula.statusMatricula == "Bom", "O status da matrícula está incorreto"
        assert matricula.desempenho == "Bom", "O desempenho da matrícula está incorreto"
        assert matricula.frequencia == "Bom", "A frequência da matrícula está incorreta"
        assert matricula.dataMatricula == "12-06-2025", "A data da matrícula está incorreta"
        assert matricula.curso is not None, "O curso não foi carregado corretamente"
        assert matricula.curso.id == 1, "O id do curso na matrícula está incorreto"
        assert matricula.usuario is not None, "O usuário não foi carregado corretamente"
        assert matricula.usuario.id == 1, "O id do usuário na matrícula está incorreto"
        assert matricula.usuario.nome == "claudio", "O nome do usuário na matrícula está incorreto"
    
    def test_obter_matriculas_por_nome(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "2025-06-12")
        id_usuario = inserir_usuario(usuario)

        cliente = Cliente(0, "", "", "", "", "", "2025-06-12", True, [], True)
        id_cliente = inserir_cliente(cliente, id_usuario)

        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "2025-06-12")
        id_professor = inserir_professor(professor, id_cliente)

        curso_obj = Curso(0, "Python", id_professor, 12.99, "não sei", "12:56", "Bom", "2025-06-12", True)
        id_curso = inserir_curso(curso_obj)

        matricula_obj = Matricula(0, id_cliente, id_curso, "Bom", "Bom", "Bom", "2025-06-12")
        inserir_matricula(matricula_obj)

        # Act
        matriculas_por_nome = obter_matriculas_por_nome("claudio")

        # Assert
        assert len(matriculas_por_nome) > 0, "Não deveria ser vazio"
        assert matriculas_por_nome[0].usuario.nome == "claudio", "O nome do usuário na matrícula está incorreto"



    def test_obter_matriculas_por_curso(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        # Act
        matriculas_por_curso = obter_matriculas_por_curso("Python")
        # Asserts
        assert len(matriculas_por_curso) > 0, "Não deveria ser vazio"

    def test_obter_matriculas_por_cliente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        # Act
        matriculas_por_cliente = obter_matriculas_por_cliente(cliente_inserido)
        # Asserts
        assert len(matriculas_por_cliente) > 0, "Não deveria ser vazio"

    def test_obter_quantidade_matriculas_por_curso(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "2025-06-12")
        id_usuario = inserir_usuario(usuario)

        cliente = Cliente(0, "", "", "", "", "", "2025-06-12", True, [], True)
        id_cliente = inserir_cliente(cliente, id_usuario)

        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "2025-06-12")
        id_professor = inserir_professor(professor, id_cliente)

        curso_obj = Curso(0, "Python", id_professor, 12.99, "não sei", "12:56", "Bom", "2025-06-12", True)
        id_curso = inserir_curso(curso_obj)

        matricula_obj = Matricula(0, id_cliente, id_curso, "Bom", "Bom", "Bom", "2025-06-12")
        inserir_matricula(matricula_obj)

        # Act
        quantidade_matriculas = obter_quantidade_matriculas_por_curso("Python")

        # Assert
        assert quantidade_matriculas > 0, "A quantidade de matrículas deveria ser maior que zero"



    def test_obter_quantidade_matriculas_por_cliente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        # Act
        quantidade_matriculas = obter_quantidade_matriculas_por_cliente(cliente_inserido)
        # Asserts
        assert quantidade_matriculas > 0, "A quantidade de matrículas deveria ser maior que zero"

    def test_obter_quantidade_matriculas(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        # Act
        quantidade_matriculas = obter_quantidade_matriculas()
        # Asserts
        assert quantidade_matriculas > 0, "A quantidade de matrículas deveria ser maior que zero"

    def test_atualizar_matricula(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "2025-06-12")
        id_usuario = inserir_usuario(usuario)

        cliente = Cliente(0, "", "", "", "", "", "2025-06-12", True, [], True)
        id_cliente = inserir_cliente(cliente, id_usuario)

        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "2025-06-12")
        id_professor = inserir_professor(professor, id_cliente)

        curso_obj = Curso(0, "Python", id_professor, 12.99, "não sei", "12:56", "Bom", "2025-06-12", True)
        id_curso = inserir_curso(curso_obj)

        matricula_obj = Matricula(0, id_cliente, id_curso, "Bom", "Bom", "Bom", "2025-06-12")
        inserir_matricula(matricula_obj)

        # Atualizar valor
        matricula_obj.statusMatricula = "Atualizado"
        resultado_atualizacao = atualizar_matricula(1, matricula_obj)  # Use o ID correto aqui (1 ou retornado)

        # Obter a matrícula atualizada
        matricula_atualizada = obter_matricula_por_id(1)

        # Asserts
        assert resultado_atualizacao is True, "A atualização da matrícula falhou"
        assert matricula_atualizada.statusMatricula == "Atualizado", "O status da matrícula não foi atualizado corretamente"
  

    def test_excluir_matricula(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_matricula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        matricula_obj = Matricula(0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)

        # Act
        resultado_delecao = excluir_matricula(matricula_inserida)

        # Asserts
        assert resultado_delecao == True, "A deleção da matrícula falhou"
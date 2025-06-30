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

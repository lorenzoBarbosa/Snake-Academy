import sys
import os

from data.cliente.cliente_repo import *
from data.comunidade.comunidade_repo import *
from data.curso.curso_model import Curso
from data.curso.curso_repo import *
from data.professor.professor_repo import *
from data.usuario.usuario_repo import *


class TestComunidadeRepo:
    def test_criar_tabela_comunidade(self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        # Act
        resultado = criar_tabela_comunidade()
        # Assert 
        assert resultado is True, "A tabela curso não foi criada"
    
    def test_inserir_comunidade(self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_db = obter_curso_por_id(curso_inserido)
        # Act
        comunidade_obj = Comunidade(0,curso_db,"Neymar", 0, [])
        comunidade_inserido = inserir_comunidade(comunidade_obj)
        comunidade_db = obter_comunidade_por_id(comunidade_inserido)
        # Assert
        assert comunidade_db is not None, "A comunidade não foi inserida"
        assert comunidade_db.id == comunidade_inserido, "O ID da comunidade inserida não corresponde ao esperado"
        assert comunidade_db.nome == comunidade_obj.nome, "O nome da comunidade inserida não corresponde ao esperado"
        assert comunidade_db.quantidadeParticipantes == comunidade_obj.quantidadeParticipantes, "A quantidade de participantes da comunidade inserida não corresponde ao esperado"
        assert comunidade_db.listaParticipantes == comunidade_obj.listaParticipantes, "A lista de participantes da comunidade inserida não corresponde ao esperado"

    def test_atualizar_comunidade (self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso = Curso(0, "Python", 1, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_db = obter_curso_por_id(curso_inserido)
        # Act
        comunidade_obj = Comunidade(0, curso_db,"", 0, [])
        comunidade_inserido = inserir_comunidade(comunidade_obj)
        comunidade_db = obter_comunidade_por_id(comunidade_inserido)
        
        comunidade_db.nome = "Nova Comunidade"
        comunidade_db.quantidadeParticipantes = 10
        comunidade_db.listaParticipantes.append("Novo Participante")
        atualizar_comunidade(comunidade_inserido, comunidade_db)
        
        comunidade_atualizada = obter_comunidade_por_id(comunidade_inserido)
        
        # Assert
        assert comunidade_atualizada is not None, "A comunidade não foi atualizada"
        assert comunidade_atualizada.nome == "Nova Comunidade", "O nome da comunidade atualizada não corresponde ao esperado"
        assert comunidade_atualizada.quantidadeParticipantes == 10, "A quantidade de participantes da comunidade atualizada não corresponde ao esperado"
        assert "Novo Participante" in comunidade_atualizada.listaParticipantes, "A lista de participantes da comunidade atualizada não corresponde ao esperado"

    def test_obter_comunidade_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()

        usuario = Usuario(0, "ana", "ana@g", "123", "1234", "01-01-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "01-01-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["JS"], 10, "01-01-2025")
        inserir_professor(professor, cliente_id)
        curso = Curso(0, "JS", 1, 20.0, "aula", "10:00", "legal", "01-01-2025", True)
        curso_id = inserir_curso(curso)
        curso_obj = obter_curso_por_id(curso_id)

        comunidade = Comunidade(0, curso_obj, "Comunidade JS", 3, ["a", "b", "c"])
        comunidade_id = inserir_comunidade(comunidade)

        resultado = obter_comunidade_por_id(comunidade_id)
        assert resultado is not None
        assert resultado.nome == "Comunidade JS"

    def test_obter_comunidades_paginado(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()

        usuario = Usuario(0, "maria", "maria@g", "123", "1234", "01-01-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "01-01-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["Java"], 10, "01-01-2025")
        inserir_professor(professor, cliente_id)
        curso = Curso(0, "Java", 1, 30.0, "aula", "11:00", "ótimo", "01-01-2025", True)
        curso_id = inserir_curso(curso)
        curso_obj = obter_curso_por_id(curso_id)

        comunidade = Comunidade(0, curso_obj, "Comunidade Java", 2, ["user1", "user2"])
        inserir_comunidade(comunidade)

        resultado = obter_comunidades_paginado(1, 10)
        assert isinstance(resultado, list)
        assert any(c.nome == "Comunidade Java" for c in resultado)

    def test_obter_comunidade_por_nome_curso(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()

        usuario = Usuario(0, "jose", "jose@g", "123", "1234", "01-01-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "01-01-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["HTML"], 10, "01-01-2025")
        inserir_professor(professor, cliente_id)
        curso = Curso(0, "HTML", 1, 15.0, "aula", "12:00", "bom", "01-01-2025", True)
        curso_id = inserir_curso(curso)
        curso_obj = obter_curso_por_id(curso_id)

        comunidade = Comunidade(0, curso_obj, "Comunidade HTML", 1, ["x"])
        inserir_comunidade(comunidade)

        resultado = obter_comunidade_por_nome_curso("HTML")
        assert isinstance(resultado, list)
        assert any(c.nome == "Comunidade HTML" for c in resultado)

    def test_obter_todas_comunidades(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()

        usuario = Usuario(0, "carlos", "carlos@g", "123", "1234", "01-01-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "01-01-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["React"], 10, "01-01-2025")
        inserir_professor(professor, cliente_id)
        curso = Curso(0, "React", 1, 40.0, "aula", "13:00", "excelente", "01-01-2025", True)
        curso_id = inserir_curso(curso)
        curso_obj = obter_curso_por_id(curso_id)

        comunidade = Comunidade(0, curso_obj, "Comunidade React", 5, ["a", "b", "c", "d", "e"])
        inserir_comunidade(comunidade)

        resultado = obter_todas_comunidades()
        assert isinstance(resultado, list)
        assert any(c.nome == "Comunidade React" for c in resultado)

    def test_obter_comunidade_por_termo_paginado(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()

        usuario = Usuario(0, "joana", "joana@g", "123", "1234", "01-01-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "01-01-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["CSS"], 10, "01-01-2025")
        inserir_professor(professor, cliente_id)
        curso = Curso(0, "CSS", 1, 25.0, "aula", "14:00", "bom", "01-01-2025", True)
        curso_id = inserir_curso(curso)
        curso_obj = obter_curso_por_id(curso_id)

        comunidade = Comunidade(0, curso_obj, "Comunidade CSS", 3, ["joana"])
        inserir_comunidade(comunidade)

        resultado = obter_comunidade_por_termo_paginado("CSS", 1, 10)
        assert isinstance(resultado, list)
        assert any("CSS" in c.nome or "CSS" in c.nomeCurso.nome for c in resultado)

    def test_obter_quantidade_comunidades(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()

        usuario = Usuario(0, "bruno", "bruno@g", "123", "1234", "01-01-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "01-01-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["SQL"], 10, "01-01-2025")
        inserir_professor(professor, cliente_id)
        curso = Curso(0, "SQL", 1, 35.0, "aula", "15:00", "ok", "01-01-2025", True)
        curso_id = inserir_curso(curso)
        curso_obj = obter_curso_por_id(curso_id)

        comunidade = Comunidade(0, curso_obj, "Comunidade SQL", 1, ["aluno"])
        inserir_comunidade(comunidade)

        quantidade = obter_quantidade_comunidades()
        assert isinstance(quantidade, int)
        assert quantidade >= 1

    def test_obter_quantidade_comunidades_por_nome_curso(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()

        usuario = Usuario(0, "gustavo", "gustavo@g", "123", "1234", "01-01-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "01-01-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["C#"], 10, "01-01-2025")
        inserir_professor(professor, cliente_id)
        curso = Curso(0, "C#", 1, 22.0, "aula", "16:00", "bom", "01-01-2025", True)
        curso_id = inserir_curso(curso)
        curso_obj = obter_curso_por_id(curso_id)

        comunidade = Comunidade(0, curso_obj, "Comunidade C#", 2, ["u1", "u2"])
        inserir_comunidade(comunidade)

        quantidade = obter_quantidade_comunidades_por_nome_curso("C#")
        assert isinstance(quantidade, int)
        assert quantidade >= 1

    def test_excluir_comunidade_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()

        usuario = Usuario(0, "lucas", "lucas@g", "123", "1234", "01-01-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "01-01-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["Go"], 10, "01-01-2025")
        inserir_professor(professor, cliente_id)
        curso = Curso(0, "Go", 1, 18.0, "aula", "17:00", "legal", "01-01-2025", True)
        curso_id = inserir_curso(curso)
        curso_obj = obter_curso_por_id(curso_id)

        comunidade = Comunidade(0, curso_obj, "Comunidade Go", 1, ["lucas"])
        comunidade_id = inserir_comunidade(comunidade)

        excluir_comunidade_por_id(comunidade_id)
        resultado = obter_comunidade_por_id(comunidade_id)
        assert resultado is None

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
        comunidade_obj = Comunidade(curso_inserido,"", 0, [])
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
        comunidade_obj = Comunidade(curso_inserido,"", 0, [])
        comunidade_inserido = inserir_comunidade(comunidade_obj)
        comunidade_db = obter_comunidade_por_id(comunidade_inserido)
        
        comunidade_db.nome = "Nova Comunidade"
        comunidade_db.quantidadeParticipantes = 10
        comunidade_db.listaParticipantes.append("Novo Participante")
        atualizar_comunidade(comunidade_db)
        
        comunidade_atualizada = obter_comunidade_por_id(comunidade_inserido)
        
        # Assert
        assert comunidade_atualizada is not None, "A comunidade não foi atualizada"
        assert comunidade_atualizada.nome == "Nova Comunidade", "O nome da comunidade atualizada não corresponde ao esperado"
        assert comunidade_atualizada.quantidadeParticipantes == 10, "A quantidade de participantes da comunidade atualizada não corresponde ao esperado"
        assert "Novo Participante" in comunidade_atualizada.listaParticipantes, "A lista de participantes da comunidade atualizada não corresponde ao esperado"

import os
import sys
import json
from data.professor.professor_repo import *
from data.cliente.cliente_repo import *
from data.usuario.usuario_repo import *

class TestProfessorRepo:
    def test_criar_tabela_professor(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        # Act
        resultado = criar_tabela_professor()
        # Assert
        assert resultado is True, "A tabela não foi criada"

    def test_inserir_professor(self, test_db):
    # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()

    # Act
        usuario = Usuario(
            id=None, 
            nome="Professor Teste",
            email="professor.teste@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
        )
        id_usuario = inserir_usuario(usuario)

        cliente = Cliente(
            id=None,
            nome="Cliente Teste",
            email="cliente@example.com",
            senha="senha123",
            telefone="888888888",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123"
        )
        id_cliente = inserir_cliente(cliente, id_usuario)

        professor = Professor(
            id=id_cliente,
            nome="Professor Teste",
            email="professor.teste@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
            cursosPostados="[]",
            quantidadeAlunos=0,
            dataCriacaoProfessor="2023-01-01"
        )
        professor_inserido = inserir_professor(professor, id_cliente)
        professor_db = obter_professor_por_id(professor_inserido)

        # Assert
        assert professor_db is not None, "O professor não foi inserido"
        assert professor_db.id == id_cliente, "O id do professor deveria ser outro"
        assert professor_db.nome == usuario.nome, "O nome do professor está incorreto"
        assert professor_db.email == usuario.email, "O email do professor está incorreto"
        assert professor_db.senha == usuario.senha, "A senha do professor está incorreta"
        assert professor_db.telefone == usuario.telefone, "O telefone do professor está incorreto"
        assert professor_db.dataCriacao == usuario.dataCriacao, "A data de criação do professor está incorreta"
        assert professor_db.dataUltimoAcesso == cliente.dataUltimoAcesso, "A data do último acesso do professor está incorreta"
        assert professor_db.statusConta == cliente.statusConta, "O status da conta do professor está incorreto"
        assert professor_db.historicoCursos == cliente.historicoCursos, "O histórico de cursos do professor está incorreto"
        assert professor_db.indentificacaoProfessor == cliente.indentificacaoProfessor, "A identificação do professor está incorreta"
        assert professor_db.cursosPostados == professor.cursosPostados, "Os cursos postados do professor estão incorretos"
        assert professor_db.quantidadeAlunos == professor.quantidadeAlunos, "A quantidade de alunos do professor está incorreta"
        assert professor_db.dataCriacaoProfessor == professor.dataCriacaoProfessor, "A data de criação do professor está incorreta"

    def test_obter_todos_professors(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()

        usuario1 = Usuario(
            id=None, 
            nome="Professor Teste 1",
            email="professor.teste1@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
        )
        id_usuario1 = inserir_usuario(usuario1)

        usuario2 = Usuario(
            id=None, 
            nome="Professor Teste 2",
            email="professor.teste2@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
        )
        id_usuario2 = inserir_usuario(usuario2)
        cliente1 = Cliente(
            id=None,
            nome="Cliente Teste 1",
            email="cliente.teste1@example.com",
            senha="senha123",
            telefone="888888888",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123"
        )
        id_cliente1 = inserir_cliente(cliente1, id_usuario1)

        cliente2 = Cliente(
            id=None,
            nome="Cliente Teste 2",
            email="cliente.teste2@example.com",
            senha="senha123",
            telefone="888888888",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123"
        )
        id_cliente2 = inserir_cliente(cliente2, id_usuario2)
        professor1 = Professor(
            id=id_cliente1,
            nome="Professor Teste 1",
            email="professor.teste1@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
            cursosPostados="[]",
            quantidadeAlunos=0,
            dataCriacaoProfessor="2023-01-01",
        )
        inserir_professor(professor1, id_cliente1)

        professor2 = Professor(
            id=id_cliente2,
            nome="Professor Teste 2",
            email="professor.teste2@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
            cursosPostados="[]",
            quantidadeAlunos=0,
            dataCriacaoProfessor="2023-01-01",
        )
        inserir_professor(professor2, id_cliente2)
        # Act
        professors_db = obter_todos_professors()
        # Assert
        assert len(professors_db) == 2, "Deveriam existir dois professores"
        assert professors_db[0].id == id_cliente1, "O id do primeiro professor está incorreto"
        assert professors_db[0].nome == usuario1.nome, "O nome do primeiro professor está incorreto"
        assert professors_db[0].email == usuario1.email, "O email do primeiro professor está incorreto"
        assert professors_db[0].senha == usuario1.senha, "A senha do primeiro professor está incorreta"

    def test_obter_professor_por_email(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()

        usuario = Usuario(
            id=None, 
            nome="Professor Teste",
            email="professor.teste@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
        )
        id_usuario = inserir_usuario(usuario)
        cliente = Cliente(
            id=None,
            nome="Cliente Teste",
            email="usuario.teste@examplo.com",
            senha="senha123",
            telefone="888888888",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
        )
        id_cliente = inserir_cliente(cliente, id_usuario)
        professor = Professor(
            id=id_cliente,
            nome="Professor Teste",
            email="professor.teste@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
            cursosPostados="[]",
            quantidadeAlunos=0,
            dataCriacaoProfessor="2023-01-01",
        )
        inserir_professor(professor, id_cliente)
        # Act
        professor_db = obter_professor_por_email(usuario.email)
        # Assert
        assert professor_db is not None, "O professor não foi encontrado"
        assert professor_db.id == id_cliente, "O id do professor está incorreto"
        assert professor_db.nome == usuario.nome, "O nome do professor está incorreto"
        assert professor_db.email == usuario.email, "O email do professor está incorreto"
        assert professor_db.senha == usuario.senha, "A senha do professor está incorreta"
        assert professor_db.telefone == usuario.telefone, "O telefone do professor está incorreto"
        assert professor_db.dataCriacao == usuario.dataCriacao, "A data de criação do professor está incorreta"
        assert professor_db.dataUltimoAcesso == cliente.dataUltimoAcesso, "A data do último acesso do professor está incorreta"
        assert professor_db.statusConta == cliente.statusConta, "O status da conta do professor está incorreto"
        assert professor_db.historicoCursos == cliente.historicoCursos, "O histórico de cursos do professor está incorreto"
        assert professor_db.indentificacaoProfessor == cliente.indentificacaoProfessor, "A identificação do professor está incorreta"
        assert professor_db.cursosPostados == professor.cursosPostados, "Os cursos postados do professor estão incorretos"
        assert professor_db.quantidadeAlunos == professor.quantidadeAlunos, "A quantidade de alunos do professor está incorreta"
        assert professor_db.dataCriacaoProfessor == professor.dataCriacaoProfessor, "A data de criação do professor está incorreta"
        assert professor_db.dataUltimoAcesso == professor.dataUltimoAcesso, "A data do último acesso do professor está incorreta"

    def test_obter_professor_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()

        usuario = Usuario(
            id=None, 
            nome="Professor Teste",
            email="professor.teste@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
        )
        id_usuario = inserir_usuario(usuario)
        cliente = Cliente(
            id=None,
            nome="Cliente Teste",
            email="usuario.teste@example.com",
            senha="senha123",
            telefone="888888888",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
        )
        id_cliente = inserir_cliente(cliente, id_usuario)
        professor = Professor(
            id=id_cliente,
            nome="Professor Teste",
            email="professor.teste@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
            cursosPostados="[]",
            quantidadeAlunos=0,
            dataCriacaoProfessor="2023-01-01",
        )
        inserir_professor(professor, id_cliente)
        # Act
        professor_db = obter_professor_por_id(id_cliente)
        # Assert
        assert professor_db is not None, "O professor não foi encontrado"
        assert professor_db.id == id_cliente, "O id do professor está incorreto"
        assert professor_db.nome == usuario.nome, "O nome do professor está incorreto"
        assert professor_db.email == usuario.email, "O email do professor está incorreto"
        assert professor_db.senha == usuario.senha, "A senha do professor está incorreta"
        assert professor_db.telefone == usuario.telefone, "O telefone do professor está incorreto"
        assert professor_db.dataCriacao == usuario.dataCriacao, "A data de criação do professor está incorreta"
        assert professor_db.dataUltimoAcesso == cliente.dataUltimoAcesso, "A data do último acesso do professor está incorreta"
        assert professor_db.statusConta == cliente.statusConta, "O status da conta do professor está incorreto"
        assert professor_db.historicoCursos == cliente.historicoCursos, "O histórico de cursos do professor está incorreto"
        assert professor_db.indentificacaoProfessor == cliente.indentificacaoProfessor, "A identificação do professor está incorreta"
        assert professor_db.cursosPostados == professor.cursosPostados, "Os cursos postados do professor estão incorretos"
        assert professor_db.quantidadeAlunos == professor.quantidadeAlunos, "A quantidade de alunos do professor está incorreta"
        assert professor_db.dataCriacaoProfessor == professor.dataCriacaoProfessor, "A data de criação do professor está incorreta"
        assert professor_db.dataUltimoAcesso == professor.dataUltimoAcesso, "A data do último acesso do professor está incorreta"

    def test_atualizar_professor_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()

        usuario = Usuario(
            id=None, 
            nome="Professor Original",
            email="professor.original@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
        )
        id_usuario = inserir_usuario(usuario)
        cliente = Cliente(
            id=None,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone= usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            dataUltimoAcesso="2023-01-01",
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
        )
        id_cliente = inserir_cliente(cliente, id_usuario)
        professor = Professor(
            id=id_cliente,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            dataUltimoAcesso=cliente.dataUltimoAcesso,
            statusConta=cliente.statusConta,
            historicoCursos= cliente.historicoCursos,
            indentificacaoProfessor=cliente.indentificacaoProfessor,
            cursosPostados="[]",
            quantidadeAlunos=0,
            dataCriacaoProfessor="2023-01-01",
        )
        inserir_professor(professor, id_cliente)
        
        # Act(atualizei só alguns campos simulando uma atualização parcial)
        professor.nome = "Professor Atualizado"
        professor.email = "professor.atualizado@example.com"
        professor.telefone = "987654321"
        professor.dataUltimoAcesso = "2023-01-02"
        professor.historicoCursos = json.dumps("[\"Curso 1\", \"Curso 2\"]")
        professor.indentificacaoProfessor = "ID456"
        professor.cursosPostados = json.dumps("[\"Curso 3\"]")
        professor.quantidadeAlunos = 10
        atualizar_professor_por_id(professor, id_cliente) #executa a atualização no banco de dados

        professor_db = obter_professor_por_id(id_cliente) #isso busca o professor atualizado no banco de dados

        # Assert
        assert professor_db is not None, "O professor não foi atualizado"
        assert professor_db.nome == "Professor Atualizado", "O nome do professor atualizado está incorreto"
        assert professor_db.email == "professor.atualizado@example.com", "O email do professor atualizado está incorreto"
        assert professor_db.telefone == "987654321", "O telefone do professor atualizado está incorreto"
        assert professor_db.dataUltimoAcesso == "2023-01-02", "A data do último acesso do professor atualizado está incorreta"
        assert professor_db.historicoCursos == "[\"Curso 1\", \"Curso 2\"]", "O histórico de cursos do professor atualizado está incorreto"
        assert professor_db.indentificacaoProfessor == "ID456", "A identificação do professor atualizado está incorreta"
        assert professor_db.cursosPostados == "[\"Curso 3\"]", "Os cursos postados do professor atualizado estão incorretos"
        assert professor_db.quantidadeAlunos == 10, "A quantidade de alunos do professor atualizado está incorreta"


    def test_atualizar_professor_por_email(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()

        usuario = Usuario(
            id=None, 
            nome="Professor Original",
            email="professor.original@example.com",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01",
        )
        id_usuario = inserir_usuario(usuario)
        cliente = Cliente(
            id=None,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            dataUltimoAcesso=usuario.dataCriacao,
            statusConta="ativo",
            historicoCursos="[]",
            indentificacaoProfessor="ID123",
        )
        id_cliente = inserir_cliente(cliente, id_usuario)
        professor = Professor(
            id=id_cliente,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            dataUltimoAcesso=cliente.dataUltimoAcesso,
            statusConta=cliente.statusConta,
            historicoCursos=cliente.historicoCursos,
            indentificacaoProfessor=cliente.indentificacaoProfessor,
            cursosPostados="[]",
            quantidadeAlunos=0,
            dataCriacaoProfessor="2023-01-01",
        )
        inserir_professor(professor, id_cliente)

        # Act(atualizei só alguns campos simulando uma atualização parcial)
        professor.nome = "Professor Atualizado"
        professor.email = "professor.atualizado@example.com"
        professor.historicoCursos = json.dumps("[\"Curso 2\", \"Curso 3\"]")
        professor.indentificacaoProfessor = "ID456"
        professor.cursosPostados = json.dumps("[\"Curso 4\"]")
        professor.quantidadeAlunos = 15
        atualizar_professor_por_email(professor, usuario.email) #executa a atualização no banco de dados

        professor_db = obter_professor_por_email(professor.email) #isso busca o professor atualizado no banco de dados

        # Assert
        assert obter_professor_por_email(usuario.email) is None, "O professor original não deveria ser encontrado pelo email antigo" #vê se o professor antigo não existe mais
        assert professor_db is not None, "O professor não foi atualizado"
        assert professor_db.nome == "Professor Atualizado", "O nome do professor atualizado está incorreto"
        assert professor_db.email == "professor.atualizado@example.com", "O email do professor atualizado está incorreto"
        assert professor_db.historicoCursos == "[\"Curso 2\", \"Curso 3\"]", "O histórico de cursos do professor atualizado está incorreto"
        assert professor_db.indentificacaoProfessor == "ID456", "A identificação do professor atualizado está incorreta"
        assert professor_db.cursosPostados == "[\"Curso 4\"]", "Os cursos postados do professor atualizado estão incorretos"
        assert professor_db.quantidadeAlunos == 15, "A quantidade de alunos do professor atualizado está incorreta"

    def test_excluir_professor_por_id(self, test_db):
        # Arrange
            criar_tabela_usuario()
            criar_tabela_cliente()
            criar_tabela_professor()
            usuario = Usuario(
                id=None, 
                nome="Professor Teste",
                email="professor.original@example.com",
                senha="senha123",
                telefone="123456789",
                dataCriacao="2023-01-01",
            )
            id_usuario = inserir_usuario(usuario)
            cliente = Cliente(
                id=None,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataCriacao=usuario.dataCriacao,
                dataUltimoAcesso="2023-01-01",
                statusConta="ativo",
                historicoCursos="[]",
                indentificacaoProfessor="ID123",
            )
            id_cliente = inserir_cliente(cliente, id_usuario)
            professor = Professor(
                id=id_cliente,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataCriacao=usuario.dataCriacao,
                dataUltimoAcesso=cliente.dataUltimoAcesso,
                statusConta=cliente.statusConta,
                historicoCursos=cliente.historicoCursos,
                indentificacaoProfessor=cliente.indentificacaoProfessor,
                cursosPostados="[]",
                quantidadeAlunos=0,
                dataCriacaoProfessor="2023-01-01",
            )
            professor_inserido = inserir_professor(professor, id_cliente)
            professor_db = obter_professor_por_id(professor_inserido)
            #Act
            id_professor = professor_db.id
            resultado = excluir_professor_por_id(id_professor) #executa a exclusão no banco de dados
            #Assert
            assert resultado is not None, "A exclusão do professor falhou"
            assert obter_professor_por_id(id_professor) is None, "O professor não foi excluído corretamente"


    def test_excluir_professor_por_email(self, test_db):
        # Arrange
            criar_tabela_usuario()
            criar_tabela_cliente()
            criar_tabela_professor()      
            usuario = Usuario(
                id=None, 
                nome="Professor Teste",
                email="professor.original@example.com",
                senha="senha123",
                telefone="123456789",
                dataCriacao="2023-01-01",
            )
            id_usuario = inserir_usuario(usuario)
            cliente = Cliente(
                id=None,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataCriacao=usuario.dataCriacao,
                dataUltimoAcesso="2023-01-01",
                statusConta="ativo",
                historicoCursos="[]",
                indentificacaoProfessor="ID123",
            )
            id_cliente = inserir_cliente(cliente, id_usuario)
            professor = Professor(
                id=id_cliente,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataCriacao=usuario.dataCriacao,
                dataUltimoAcesso=cliente.dataUltimoAcesso,
                statusConta=cliente.statusConta,
                historicoCursos=cliente.historicoCursos,
                indentificacaoProfessor=cliente.indentificacaoProfessor,
                cursosPostados="[]",
                quantidadeAlunos=0,
                dataCriacaoProfessor="2023-01-01",
            )
            professor_inserido = inserir_professor(professor, id_cliente)
            professor_db = obter_professor_por_id(professor_inserido)
                # Act
            resultado = excluir_professor_por_email(professor_db.email)
                # Assert
            assert resultado is not None, "A exclusão do professor falhou"
            assert obter_professor_por_id(professor_inserido) is None, "O professor não foi excluído corretamente"
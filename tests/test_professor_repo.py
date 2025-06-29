import os
import sys
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

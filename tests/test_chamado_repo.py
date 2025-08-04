import sys
import os
from data.chamado.chamado_repo import *
from data.usuario.usuario_repo import *

class TestChamadoRepo:
    def test_criar_tabela_chamado(self, test_db):
        # Arrange
        criar_tabela_usuario
        # Act
        resultado = criar_tabela_chamado()
        # Assert
        assert resultado is True, "A criação da tabela deveria retornar True"

    def test_gerar_chamado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_chamado()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@example.com",
                "senha123",
                "123456789",
                "210109")
        usuario_inserido = inserir_usuario(usuario)
        chamado = Chamado(
                0,
                usuario_inserido,
                "Descrição do chamado",
                "210109",
                "12:00",
                False)
        chamado_gerado = gerar_chamado(chamado)
        chamado_db = obter_chamado_por_id(chamado_gerado)
        # Assert
        assert chamado_db is not None, "A inserção de dados não deveria retornar None"
        assert chamado_db.idUsuario == usuario_inserido, "O id do usuário inserido está incorreto"
        assert chamado_db.descricao == "Descrição do chamado", "A descrição do chamado inserida está incorreta"
        assert chamado_db.dataEnvio == "210109", "A data de envio do chamado inserida está incorreta"
        assert chamado_db.horaEnvio == "12:00", "A hora de envio do chamado inserida está incorreta"
        assert chamado_db.visualizacao is False, "A visualização do chamado inserida está incorreta"

    def test_obter_todos_chamados(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_chamado()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@example.com",
            "senha123",
            "123456789",
            "210109"
        )
        usuario_inserido = inserir_usuario(usuario)
        chamado = Chamado(
            0,
            usuario_inserido,
            "Descrição do chamado",
            "210109",
            "12:00",
            False
        )
        chamado_gerado = gerar_chamado(chamado)
        chamado_db = obter_chamado_por_id(chamado_gerado)
        # Assert
        assert chamado_db is not None, "A inserção de dados não deveria retornar None"
        assert chamado_db.idUsuario == usuario_inserido, "O id do usuário inserido está incorreto"
        assert chamado_db.descricao == "Descrição do chamado", "A descrição do chamado inserida está incorreta"
        assert chamado_db.dataEnvio == "210109", "A data de envio do chamado inserida está incorreta"
        assert chamado_db.horaEnvio == "12:00", "A hora de envio do chamado inserida está incorreta"
        assert chamado_db.visualizacao is False, "A visualização do chamado inserida está incorreta"

    def test_obter_chamado_por_id(self, test_db):

        # Arrange
        criar_tabela_usuario()
        criar_tabela_chamado()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@example.com",
            "senha123",
            "123456789",
            "210109"
        )
        usuario_inserido = inserir_usuario(usuario)
        chamado = Chamado(
            0,
            usuario_inserido,
            "Descrição do chamado",
            "210109",
            "12:00",
            False
        )
        chamado_gerado = gerar_chamado(chamado)
        chamado_db = obter_chamado_por_id(chamado_gerado)
        # Assert
        assert chamado_db is not None, "A inserção de dados não deveria retornar None"
        assert chamado_db.idUsuario == usuario_inserido, "O id do usuário inserido está incorreto"
        assert chamado_db.descricao == "Descrição do chamado", "A descrição do chamado inserida está incorreta"
        assert chamado_db.dataEnvio == "210109", "A data de envio do chamado inserida está incorreta"
        assert chamado_db.horaEnvio == "12:00", "A hora de envio do chamado inserida está incorreta"
        assert chamado_db.visualizacao is False, "A visualização do chamado inserida está incorreta"

    def test_obter_chamados_paginados(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_chamado()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@example.com",
            "senha123",
            "123456789",
            "210109"
        )
        usuario_inserido = inserir_usuario(usuario)
        chamado = Chamado(
            0,
            usuario_inserido,
            "Descrição do chamado",
            "210109",
            "12:00",
            False
        )
        chamado_gerado = gerar_chamado(chamado)
        # Act
        chamado_db = obter_chamado_por_id(chamado_gerado)
        # Assert
        assert chamado_db is not None, "A inserção de dados não deveria retornar None"
        assert chamado_db.idUsuario == usuario_inserido, "O id do usuário inserido está incorreto"
        assert chamado_db.descricao == "Descrição do chamado", "A descrição do chamado inserida está incorreta"
        assert chamado_db.dataEnvio == "210109", "A data de envio do chamado inserida está incorreta"
        assert chamado_db.horaEnvio == "12:00", "A hora de envio do chamado inserida está incorreta"
        assert chamado_db.visualizacao is False, "A visualização do chamado inserida está incorreta"

    def test_obter_chamado_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_chamado()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@example.com",
            "senha123",
            "123456789",
            "210109"
        )
        usuario_inserido = inserir_usuario(usuario)
        chamado = Chamado(
            0,
            usuario_inserido,
            "Descrição do chamado",
            "210109",
            "12:00",
            False
        )
        chamado_gerado = gerar_chamado(chamado)
        # Act
        chamado_db = obter_chamado_por_id(chamado_gerado)
        # Assert
        assert chamado_db is not None, "A inserção de dados não deveria retornar None"
        assert chamado_db.idUsuario == usuario_inserido, "O id do usuário inserido está incorreto"
        assert chamado_db.descricao == "Descrição do chamado", "A descrição do chamado inserida está incorreta"
        assert chamado_db.dataEnvio == "210109", "A data de envio do chamado inserida está incorreta"
        assert chamado_db.horaEnvio == "12:00", "A hora de envio do chamado inserida está incorreta"
        assert chamado_db.visualizacao is False, "A visualização do chamado inserida está incorreta"

    def test_obter_chamado_por_termo_paginado(self, test_db):

        # Arrange
        criar_tabela_usuario()
        criar_tabela_chamado()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@example.com",
            "senha123",
            "123456789",
            "210109"
        )
        usuario_inserido = inserir_usuario(usuario)
        chamado = Chamado(
            0,
            usuario_inserido,
            "Descrição do chamado",
            "210109",
            "12:00",
            False
        )
        chamado_gerado = gerar_chamado(chamado)
        # Act
        chamado_db = obter_chamado_por_id(chamado_gerado)
        # Assert
        assert chamado_db is not None, "A inserção de dados não deveria retornar None"
        assert chamado_db.idUsuario == usuario_inserido, "O id do usuário inserido está incorreto"
        assert chamado_db.descricao == "Descrição do chamado", "A descrição do chamado inserida está incorreta"
        assert chamado_db.dataEnvio == "210109", "A data de envio do chamado inserida está incorreta"
        assert chamado_db.horaEnvio == "12:00", "A hora de envio do chamado inserida está incorreta"
        assert chamado_db.visualizacao is False, "A visualização do chamado inserida está incorreta"

    def test_obter_quantidade_chamados(self, test_db): 
            
            # Arrange
            criar_tabela_usuario()
            criar_tabela_chamado()
            usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@example.com",
                "senha123",
                "123456789",
                "210109"
            )
            usuario_inserido = inserir_usuario(usuario)
            chamado = Chamado(
                0,
                usuario_inserido,
                "Descrição do chamado",
                "210109",
                "12:00",
                False
            )
            gerar_chamado(chamado)
            # Act
            quantidade = obter_quantidade_chamados()
            # Assert
            assert quantidade == 1, "A quantidade de chamados deveria ser 1"

    def obter_quantidade_chamados_por_nome_usuario(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_chamado()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@example.com",
            "senha123",
            "123456789",
            "210109"
        )
        usuario_inserido = inserir_usuario(usuario)
        chamado = Chamado(
            0,
            usuario_inserido,
            "Descrição do chamado",
            "210109",
            "12:00",
            False
        )
        gerar_chamado(chamado)
        # Act
        quantidade = obter_quantidade_chamados_por_nome_usuario("lorenzo")
        # Assert
        assert quantidade == 1, "A quantidade de chamados para o usuário 'lorenzo' deveria ser 1"

    def test_excluir_chamado_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_chamado()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@example.com",
            "senha123",
            "123456789",
            "210109"
        )
        usuario_inserido = inserir_usuario(usuario)
        chamado = Chamado(
            0,
            usuario_inserido,
            "Descrição do chamado",
            "210109",
            "12:00",
            False
        )
        chamado_gerado = gerar_chamado(chamado)
        chamado_db = obter_chamado_por_id(chamado_gerado)
        # Act
        resultado = excluir_chamado_por_id(chamado_db.id)
        # Assert
        assert resultado is True, "A exclusão do chamado deveria retornar True"
        assert obter_chamado_por_id(chamado_gerado) is None, "O chamado excluído deveria ser None"
        
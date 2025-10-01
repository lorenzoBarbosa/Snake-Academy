import sys
import os
from data.usuario.usuario_repo import *

class TestUsuarioRepo:
    def test_criar_tabela_usuario(self, test_db):
        # Arrange
        # Act
        resultado = criar_tabela_usuario()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"
    
    def test_inserir_usuario(self, test_db):
        #Arrange
        criar_tabela_usuario()
        #Act
        usuario = Usuario(
                id=None,
                nome="lorenzo",
                email="lorenzo@gmail.com",
                senha="hfevh",
                telefone="3175549-98",
                data_nascimento="210109",
                perfil="cliente",
                token_redefinicao="abc",
                data_token="20231010",
                data_cadastro="2023-12-09",
                foto=None)
        
        usuario_inserido = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_inserido)
        #Assert
        assert usuario_db is not None, "A inserção de dados não deveria retornar None"
        assert usuario_db.id == 1, "O id do usuário deveria ser 1"
        assert usuario_db.nome == "lorenzo", "O nome inserido está incorreto"
        assert usuario_db.email == "lorenzo@gmail.com", "O email inserido está incorreto"
        assert usuario_db.senha == "hfevh", "A senha inserida está incorreta"
        assert usuario_db.telefone == "3175549-98", "O telefone inserido está incorreto"
        assert usuario_db.data_nascimento == "210109", "A data de criação inserida está incorreta"
        assert usuario_db.perfil == "cliente", "O perfil inserido está incorreto"
    
    def test_obter_todos_usuarios(self, test_db):
        #Arrange
        criar_tabela_usuario()
        for i in range(10):
            usuario = Usuario(
                i+1,
                f"lorenzo{i+1}",
                f"lorenzo{i+1}@gmail.com",
                f"abc{i+1}",
                f"1234{i+1}",
                f"4321{i+1}")
            inserir_usuario(usuario)
        #Act
        usuarios = obter_todos_usuarios()
        #Arrange
        assert usuarios is not None, "A lista não deveria ser None"
        assert len(usuarios) == 10, "Na lista deveria ter 10 usuários"

    def test_obter_usuario_por_id(self, test_db):
        #Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario_inserido = inserir_usuario(usuario)
        #Act
        usuario_db = obter_usuario_por_id(usuario_inserido)
        # Asserts
        assert usuario_db is not None, "Não há usuários na tabela"
        assert usuario_db.id == usuario_inserido, "O usuário obtido não foi o mesmo que inserido"
        
    def test_obter_usuario_por_email(self, test_db):
        #Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario_inserido = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_inserido)
        # Act
        email = usuario_db.email
        usuario_email = obter_usuario_por_email(email)
        # Asserts
        assert usuario_email is not None, "Não há usuários na tabela"
        assert usuario_email.id == usuario_inserido, "O usuário obtido não foi o mesmo que inserido"
    
    def test_obter_quantidade_usuario(self, test_db):
        #Arrange
        criar_tabela_usuario()
        for i in range(10):
            usuario = Usuario(
                i+1,
                f"lorenzo{i+1}",
                f"lorenzo{i+1}@gmail.com",
                f"abc{i+1}",
                f"1234{i+1}",
                f"4321{i+1}")
            inserir_usuario(usuario)
        #Act
        usuarios = obter_quantidade_usuario()
        #Arrange
        assert usuarios is not None, "Não deveria ser None"
        assert usuarios == 10, "Na lista deveria ter 10 usuários"
    
    def test_obter_usuario_paginado(self, test_db):
        #Arrange
        criar_tabela_usuario()
        for i in range(10):
            usuario = Usuario(
                i+1,
                f"lorenzo{i+1}",
                f"lorenzo{i+1}@gmail.com",
                f"abc{i+1}",
                f"1234{i+1}",
                f"4321{i+1}")
            inserir_usuario(usuario)
        #Act
        usuarios1 = obter_usuario_paginado(1, 4)
        usuarios2 = obter_usuario_paginado(2, 4)
        usuarios3 = obter_usuario_paginado(3, 4)
        #Assert
        assert len(usuarios1) == 4, "Na primeira página deveria haver 4 usuários"
        assert len(usuarios2) == 4, "Na segunda página deveria haver 4 usuários"
        usuario3_pagina = usuarios3[0]
        assert usuario3_pagina.id == 9, "O primeiro id da terceira página deveria ser 9"
    
    def test_atualizar_usuario_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario_inserido = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_inserido)
        # act
        usuario_db.nome = "lorenzo2"
        usuario_db.email = "lorenzo@email.com"
        usuario_db.telefone = "123456"
        usuario_db.senha = "123"
        usuario_db.dataCriacao = "121212"
        resultado = atualizar_usuario_por_id(usuario_db)
        # assert
        assert resultado == True, "A alteração "
        assert usuario_db is not None, "A inserção de dados não deveria retornar None"
        assert usuario_db.nome == "lorenzo2", "O nome inserido está incorreto"
        assert usuario_db.email == "lorenzo@email.com", "O email inserido está incorreto"
        assert usuario_db.senha == "123", "A senha inserida está incorreta"
        assert usuario_db.telefone == "123456", "O telefone inserido está incorreto"
        assert usuario_db.dataCriacao =="121212", "A data de criação está correta"
    
    def test_atualizar_usuario_por_email(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario_inserido = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_inserido)
        # act
        usuario_db.nome = "lorenzo2"
        usuario_db.telefone = "123456"
        usuario_db.senha = "123"
        usuario_db.dataCriacao = "121212"
        resultado = atualizar_usuario_por_email(usuario_db)
        # assert
        assert resultado == True, "A alteração "
        assert usuario_db is not None, "A inserção de dados não deveria retornar None"
        assert usuario_db.nome == "lorenzo2", "O nome inserido está incorreto"
        assert usuario_db.senha == "123", "A senha inserida está incorreta"
        assert usuario_db.telefone == "123456", "O telefone inserido está incorreto"
        assert usuario_db.dataCriacao =="121212", "A data de criação está correta"

    def test_excluir_usuario_por_id(self, test_db):
        #Arrange
        criar_tabela_usuario()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@gmail.com",
            "hfevh",
            "3175549-98",
            "210109")
        usuario_inserido = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_inserido)
        #Act
        id = usuario_db.id
        resultado = excluir_usuario_por_id(id)
        #Assert
        assert resultado == True, "O usuário não foi excluído"
        usuario_excluido = obter_usuario_por_id(id)
        assert usuario_excluido is None, "O usuário excluído deveria ser None"
        
    def test_excluir_usuario_por_email(self, test_db):
        #Arrange
        criar_tabela_usuario()
        usuario = Usuario(
            0,
            "lorenzo",
            "lorenzo@gmail.com",
            "hfevh",
            "3175549-98",
            "210109")
        usuario_inserido = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_inserido)
        #Act
        email = usuario_db.email
        resultado = excluir_usuario_por_email(email)
        #Assert
        assert resultado is True, "O usuário não foi excluído"
        usuario_excluido = obter_usuario_por_email(email)
        assert usuario_excluido is None, "O usuário excluído deveria ser None"



    



        
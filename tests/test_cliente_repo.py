import sys
import os
from data.usuario.usuario_repo import *
from data.cliente.cliente_repo import *

class TestClienteRepo:
    def test_criar_tabela_cliente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        # Act
        resultado = criar_tabela_cliente()
        # Assert 
        assert resultado is True, "A tabela não foi criada"
    
    def test_inserir_cliente(self, test_db):
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
        criar_tabela_cliente()
        # Act
        cliente = Cliente(
                            0,                          
                            "lorenzo",                  
                            "lorenzo@gmail.com",        
                            "hfevh",                    
                            "3175549-98",               
                            "210109",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)

        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        cliente_db = obter_cliente_por_id(cliente_inserido)
        # Asserts
        assert cliente_db is not None, "O cliente não foi inserido"
        assert cliente_db.id == 1, "O id do cliente está incorreto"
        assert cliente_db.dataUltimoAcesso == "12-05-2025", "A data de criação está incorreta"
        assert cliente_db.statusConta == True, "O status da conta está incorreto"
    
    def test_atualizar_cliente_por_id(self, test_db):
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
        criar_tabela_cliente()
        cliente = Cliente(
                            0,                          
                            "lorenzo",                  
                            "lorenzo@gmail.com",        
                            "hfevh",                    
                            "3175549-98",               
                            "210109",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)

        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        cliente_db = obter_cliente_por_id(cliente_inserido)
        # Act
        cliente_db.dataUltimoAcesso = "13-06-2025"
        cliente_db.statusConta = False
        cliente_db.historicoCursos = ["Python", "Data web"]
        cliente_db.indentificacaoProfessor = True
        resultado = atualizar_cliente_por_id(cliente_db)
        cliente_db2 = obter_cliente_por_id(cliente_inserido)
        # Asserts
        assert resultado == True, "O cliente não foi alterado com sucesso"
        assert cliente_db2.dataUltimoAcesso == "13-06-2025", "A data do último acesso está incorreta"
        assert cliente_db2.statusConta == False, "O status da conta está incorreto"
        assert cliente_db2.indentificacaoProfessor == True, "A indentificação de professor está incorreta"

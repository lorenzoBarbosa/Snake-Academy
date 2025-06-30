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
    
    def test_obter_todos_clientes(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario2 = Usuario(
                0,
                "lorenzo2",
                "lorenzo2@gmail.com",
                "hfevh2",
                "3175549-982",
                "2101092")
        usuario_inserido = inserir_usuario(usuario)
        usuario_inserido2 = inserir_usuario(usuario2)
        criar_tabela_cliente()
        cliente = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)
        
        cliente2 = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "13-06-2025",               
                            False,                       
                            [],                         
                            True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        cliente_inserido2 = inserir_cliente(cliente2, usuario_inserido2)
        # Act
        clientes = obter_todos_clientes()
        # Asserts
        assert clientes is not None, "A lista não deveria estar vazia"
        assert len(clientes) == 2, "A lista deveria conter apenas 2 clientes"

    def test_obter_clientes_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario2 = Usuario(
                0,
                "lorenzo2",
                "lorenzo2@gmail.com",
                "hfevh2",
                "3175549-982",
                "2101092")
        usuario3 = Usuario(
                0,
                "lorenzo3",
                "lorenzo3@gmail.com",
                "hfevh3",
                "3175549-983",
                "2101093")
        usuario_inserido = inserir_usuario(usuario)
        usuario_inserido2 = inserir_usuario(usuario2)
        usuario_inserido3 = inserir_usuario(usuario3)
        criar_tabela_cliente()
        cliente = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)
        cliente2 = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "13-06-2025",               
                            False,                       
                            [],                         
                            True)
        cliente3 = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "14-06-2025",               
                            False,                       
                            [],                         
                            True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        cliente_inserido2 = inserir_cliente(cliente2, usuario_inserido2)
        cliente_inserido3 = inserir_cliente(cliente3, usuario_inserido3)
        # Act
        clientes = obter_cliente_paginado(1, 2)
        clientes2 = obter_cliente_paginado(2, 2)
        # Asserts
        assert len(clientes) == 2, "Na primeira página deveria haver 2 clientes"
        clientes2_pagina = clientes2[0]
        assert clientes2_pagina.id == 3, "O primeiro id da terceira página deveria ser 3"
    
    def test_obter_cliente_por_id(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(
                            0,                          
                            "",                  
                            "",        
                            "",                    
                            "",               
                            "",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)

        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        #Act
        cliente_db = obter_cliente_por_id(cliente_inserido)
        # Asserts
        assert cliente_db is not None, "Não há clientes na tabela"
        assert cliente_db.id == cliente_inserido, "O cliente obtido não foi o mesmo que inserido"
    
    def test_obter_cliente_por_email(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario_inserido = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_inserido)
        cliente = Cliente(
                            0,                          
                            "",                  
                            "",        
                            "",                    
                            "",               
                            "",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)

        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        #Act
        email = usuario_db.email
        cliente_db = obter_cliente_por_email(email)
        # Asserts
        assert cliente_db is not None, "Não há clientes na tabela"
        assert cliente_db.id == cliente_inserido, "O cliente obtido não foi o mesmo que inserido"

    def test_obter_cliente_por_termo_paginado(self, test_db):
         # Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario2 = Usuario(
                0,
                "lorenzo2",
                "lorenzo2@gmail.com",
                "hfevh2",
                "3175549-982",
                "2101092")
        usuario3 = Usuario(
                0,
                "lorenzo3",
                "lorenzo3@gmail.com",
                "hfevh3",
                "3175549-983",
                "2101093")
        usuario_inserido = inserir_usuario(usuario)
        usuario_inserido2 = inserir_usuario(usuario2)
        usuario_inserido3 = inserir_usuario(usuario3)
        criar_tabela_cliente()
        cliente = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)
        cliente2 = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "13-06-2025",               
                            False,                       
                            [],                         
                            True)
        cliente3 = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "14-06-2025",               
                            False,                       
                            [],                         
                            True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        cliente_inserido2 = inserir_cliente(cliente2, usuario_inserido2)
        cliente_inserido3 = inserir_cliente(cliente3, usuario_inserido3)
        # Act
        termo = "lorenzo"
        clientes1 = obter_cliente_por_termo_paginado(termo, 1, 2)
        clientes2 = obter_cliente_por_termo_paginado(termo, 2, 2)
        # Asserts
        assert len(clientes1) == 2, "Deveria haver dois clientes na lista"
        cliente_pagina = clientes2[0]
        assert cliente_pagina.id == 3, "O id do primeiro cliente da segunda página deveria ser 3"

    def test_obter_quantidade_clientes(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario2 = Usuario(
                0,
                "lorenzo2",
                "lorenzo2@gmail.com",
                "hfevh2",
                "3175549-982",
                "2101092")
        usuario_inserido = inserir_usuario(usuario)
        usuario_inserido2 = inserir_usuario(usuario2)
        criar_tabela_cliente()
        cliente = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)
        
        cliente2 = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "13-06-2025",               
                            False,                       
                            [],                         
                            True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        cliente_inserido2 = inserir_cliente(cliente2, usuario_inserido2)
        # Act
        resultado = obter_quantidade_clientes()
        # Asserts
        assert resultado == 2, "Deveria haver apenas dois clientes na tabela"

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
                            "",                  
                            "",        
                            "",                    
                            "",               
                            "",                   
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

    def test_atualizar_cliente_por_email(self, test_db):
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
                            "",                  
                            "",        
                            "",                    
                            "",               
                            "",                   
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
        resultado = atualizar_cliente_por_email(cliente_db.email, cliente_db)
        cliente_db2 = obter_cliente_por_id(cliente_inserido)
        # Asserts
        assert resultado == True, "O cliente não foi alterado com sucesso"
        assert cliente_db2.dataUltimoAcesso == "13-06-2025", "A data do último acesso está incorreta"
        assert cliente_db2.statusConta == False, "O status da conta está incorreto"
        assert cliente_db2.indentificacaoProfessor == True, "A indentificação de professor está incorreta"

    def test_excluir_cliente_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario2 = Usuario(
                0,
                "lorenzo2",
                "lorenzo2@gmail.com",
                "hfevh2",
                "3175549-982",
                "2101092")
        usuario_inserido = inserir_usuario(usuario)
        usuario_inserido2 = inserir_usuario(usuario2)
        criar_tabela_cliente()
        cliente = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)
        
        cliente2 = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "13-06-2025",               
                            False,                       
                            [],                         
                            True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        cliente_inserido2 = inserir_cliente(cliente2, usuario_inserido2)
        #Act
        resultado = excluir_cliente_por_id(cliente_inserido)
        cliente_excluido = obter_cliente_por_id(cliente_inserido)
        # Asserts
        assert resultado == True, "O cliente não foi excluído com sucesso"
        assert cliente_excluido is None, "O cliente deveria ser vazio"

    def test_excluir_cliente_por_email(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuario = Usuario(
                0,
                "lorenzo",
                "lorenzo@gmail.com",
                "hfevh",
                "3175549-98",
                "210109")
        usuario2 = Usuario(
                0,
                "lorenzo2",
                "lorenzo2@gmail.com",
                "hfevh2",
                "3175549-982",
                "2101092")
        usuario_inserido = inserir_usuario(usuario)
        usuario_inserido2 = inserir_usuario(usuario2)
        criar_tabela_cliente()
        cliente = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "12-05-2025",               
                            True,                       
                            [],                         
                            False)
        
        cliente2 = Cliente(
                            0,                          
                            "",                  
                            "@gmail.com",        
                            "",                    
                            "",               
                            "",                   
                            "13-06-2025",               
                            False,                       
                            [],                         
                            True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        cliente_inserido2 = inserir_cliente(cliente2, usuario_inserido2)
        usuario_db = obter_usuario_por_id(usuario_inserido)
        #Act
        resultado = excluir_cliente_por_email(usuario_db.email)
        cliente_excluido = obter_cliente_por_id(cliente_inserido)
        # Asserts
        assert resultado == True, "O cliente não foi excluído com sucesso"
        assert cliente_excluido is None, "O cliente deveria ser vazio"
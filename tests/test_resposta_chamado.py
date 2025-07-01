import sys
import os

from data.admin.admin_repo import *
from data.chamado.chamado_repo import *
from data.resposta_chamado.resposta_chamado_repo import *
from data.usuario.usuario_repo import *

class TestRchamadoRepo:
    def test_criar_tabela_rchamado(self, test_db):
        # Assert
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        # Act
        resultado = criar_tabela_rchamado()
        # Assert
        assert resultado == True, "A criação da tabela deveria retornar True"
    
    def test_inserir_rchamado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "", "", "", "", "", 3)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        chamado = Chamado(0, usuario_inserido, "Deu errado aqui ó", "01/02/2025", "16:18", False)
        chamado_inserido = gerar_chamado(chamado)
        # Act
        rchamado = respostaChamado(0, admin_inserido, chamado_inserido, "Deu certo agora", "01/07/2025", "16:22", False)
        rchamado_inserido = gerar_rchamado(rchamado)
        rchamado_db = obter_rchamado_por_id(rchamado_inserido)
        # Assert
        assert rchamado_db is not None, "A resposta do chamado não deveria ser vazia"
        assert rchamado_db.idChamado == chamado_inserido, "O ID do chamado está incorreto"
        assert rchamado_db.idAdmin == admin_inserido, "O ID do admin está incorreto"
        assert rchamado_db.descricao == "Deu certo agora", "A descrição da resposta está incorreta"
        assert rchamado_db.dataEnvio == "01/07/2025", "A data de envio da resposta está incorreta"
        assert rchamado_db.horaEnvio == "16:22", "A hora de envio da resposta está incorreta"
        assert rchamado_db.visualizacao is 0, "O status de visualização está incorreto"
    
    def test_obter_chamados(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "", "", "", "", "", 3)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        for i in range (9):
            chamado = Chamado(0, usuario_inserido, "Deu errado aqui ó", "01/02/2025", "16:18", False)
            gerar_chamado(chamado)
        for c in range(9):
            rchamado = respostaChamado(0, admin_inserido, c+1, "Deu certo agora", "01/07/2025", "16:22", False)
            rchamado_inserido = gerar_rchamado(rchamado)
        #Act
        rchamados = obter_todos_rchamados()
        #Assert
        assert len(rchamados) == 9, "A quantidade de resposta chamados deveria ser 9"

    def test_obter_rchamado_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "ana", "ana@g.com", "123", "4321", "01-01-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        chamado = Chamado(0, usuario_inserido, "Problema X", "02/02/2025", "10:00", False)
        chamado_inserido = gerar_chamado(chamado)
        rchamado = respostaChamado(0, admin_inserido, chamado_inserido, "Resolvido", "03/02/2025", "11:00", False)
        rchamado_id = gerar_rchamado(rchamado)
        # Act
        resposta = obter_rchamado_por_id(rchamado_id)
        # Assert
        assert resposta is not None, "Deveria retornar uma resposta"
        assert resposta.id == rchamado_id, "ID da resposta está incorreto"
        assert resposta.descricao == "Resolvido", "Descrição incorreta"

    def test_obter_rchamado_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "lucas", "lucas@g.com", "123", "4321", "01-01-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        for i in range(5):
            chamado = Chamado(0, usuario_inserido, f"Problema {i}", "02/02/2025", "10:00", False)
            chamado_id = gerar_chamado(chamado)
            rchamado = respostaChamado(0, admin_inserido, chamado_id, f"Resp {i}", "03/02/2025", "11:00", False)
            gerar_rchamado(rchamado)
        # Act
        resultados1 = obter_rchamado_paginado(1, 3)
        resultados2 = obter_rchamado_paginado(2, 3)
        # Assert
        assert len(resultados1) == 3, "Deveria retornar 3 respostas paginadas"
        assert len(resultados2) == 2, "Deveria retornar 2 respostas paginadas"

    def test_obter_quantidade_rchamados(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "bruna", "bruna@g.com", "123", "4321", "01-01-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        for i in range(4):
            chamado = Chamado(0, usuario_inserido, f"Problema {i}", "02/02/2025", "10:00", False)
            chamado_id = gerar_chamado(chamado)
            rchamado = respostaChamado(0, admin_inserido, chamado_id, f"Resposta {i}", "03/02/2025", "11:00", False)
            gerar_rchamado(rchamado)
        # Act
        quantidade = obter_quantidade_rchamados()
        # Assert
        assert quantidade == 4, "A quantidade de respostas deveria ser 4"

    def test_obter_quantidade_rchamados_por_nome_admin(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "jose", "jose@g.com", "123", "4321", "01-01-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "Jose da Silva", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        for i in range(3):
            chamado = Chamado(0, usuario_inserido, f"Problema {i}", "01/01/2025", "08:00", False)
            chamado_id = gerar_chamado(chamado)
            rchamado = respostaChamado(0, admin_inserido, chamado_id, f"Resposta {i}", "01/01/2025", "09:00", False)
            gerar_rchamado(rchamado)
        # Act
        quantidade = obter_quantidade_rchamados_por_nome_admin("Jose")
        # Assert
        assert quantidade == 3, "A quantidade de respostas do admin deveria ser 3"

    def test_obter_rchamado_por_nome_admin(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "maria", "maria@g.com", "123", "4321", "01-01-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        for i in range(2):
            chamado = Chamado(0, usuario_inserido, f"Erro {i}", "05/05/2025", "10:00", False)
            chamado_id = gerar_chamado(chamado)
            rchamado = respostaChamado(0, admin_inserido, chamado_id, f"Resolvido {i}", "06/05/2025", "10:30", False)
            gerar_rchamado(rchamado)
        # Act
        rchamados = obter_rchamado_por_nome_admin("maria", 1, 2)
        # Assert
        assert len(rchamados) == 2, "Deveria haver 2 respostas do admin Maria"
        assert rchamados[0].descricao.startswith("Resolvido"), "A descrição da resposta não está correta"

    def test_obter_rchamado_por_termo_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "renan", "renan@g.com", "123", "4321", "01-01-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "Renan Admin", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        for i in range(5):
            chamado = Chamado(0, usuario_inserido, f"Bug {i}", "03/03/2025", "12:00", False)
            chamado_id = gerar_chamado(chamado)
            rchamado = respostaChamado(0, admin_inserido, chamado_id, f"Erro crítico {i}", "03/03/2025", "12:30", False)
            gerar_rchamado(rchamado)
        # Act
        resultados = obter_rchamado_por_termo_paginado("crítico", 1, 5)
        # Assert
        assert len(resultados) == 5, "Deveria retornar 5 resultados com o termo 'crítico'"

    def test_obter_rchamado_por_id_chamado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "leo", "leo@g.com", "123", "4321", "01-01-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "Leo Admin", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        chamado = Chamado(0, usuario_inserido, "Erro específico", "04/04/2025", "11:00", False)
        chamado_id = gerar_chamado(chamado)
        for i in range(2):
            rchamado = respostaChamado(0, admin_inserido, chamado_id, f"Resposta {i}", "04/04/2025", "11:30", False)
            gerar_rchamado(rchamado)
        # Act
        respostas = obter_rchamado_por_id_chamado(chamado_id)
        # Assert
        assert len(respostas) == 2, "Deveria retornar 2 respostas para o chamado"

    def test_excluir_rchamado_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        usuario = Usuario(0, "tina", "tina@g.com", "123", "4321", "01-01-2025")
        usuario_inserido = inserir_usuario(usuario)
        admin = Admin(0, "Tina Admin", "", "", "", "", 1)
        admin_inserido = inserir_admin(admin, usuario_inserido)
        chamado = Chamado(0, usuario_inserido, "Bug 404", "06/06/2025", "14:00", False)
        chamado_id = gerar_chamado(chamado)
        rchamado = respostaChamado(0, admin_inserido, chamado_id, "Foi corrigido", "06/06/2025", "14:30", False)
        rchamado_id = gerar_rchamado(rchamado)
        # Act
        excluir_rchamado_por_id(rchamado_id)
        resposta = obter_rchamado_por_id(rchamado_id)
        # Assert
        assert resposta is None, "A resposta deveria ter sido excluída"


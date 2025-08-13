from data.admin.admin_repo import *
from data.banner.banner_repo import *
from data.usuario.usuario_repo import *

class TestBannerRepo:
    def test_criar_tabela_banner(self, test_db):
        criar_tabela_usuario()
        criar_tabela_admin()
        resultado = criar_tabela_banner()
        assert resultado == True, "A tabela banner não foi criada corretamente."

    def test_inserir_banner(self, test_db):
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_banner()

        usuario = Usuario(
            id=None,
            nome="Professor Teste",
            email="oi@ogyoghkc.oi",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01"
        )
        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario  # Atualiza o objeto com o ID retornado
        admin = Admin(usuario.id, usuario.nome, usuario.email, usuario.senha, usuario.telefone, usuario.dataCriacao, "1")
        # Act
        admin_inserido = inserir_admin(admin, id_usuario)
        banner = Banner(id=0, idAdmin=admin_inserido, status=False)
        idBanner = inserir_banner(banner)
        banner_inserido = obter_banner_por_id(idBanner)
        # Assert
        assert idBanner is not None, "O banner não foi inserido corretamente."
        assert banner_inserido is not None, "O banner inserido não foi encontrado."
        assert banner_inserido.idAdmin == banner.idAdmin, "O idAdmin do banner inserido não corresponde ao esperado."
        assert banner_inserido.status == banner.status, "O status do banner inserido não corresponde ao esperado."

    def test_obter_todos_banners(self, test_db):
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_banner()

        usuario = Usuario(
            id=None,
            nome="Professor Teste",
            email="oi@oi.i",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01"
        )
        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario  # Atualiza o objeto com o ID retornado
        admin = Admin(usuario.id, usuario.nome, usuario.email, usuario.senha, usuario.telefone, usuario.dataCriacao, "1")
        admin_inserido = inserir_admin(admin, id_usuario)
        for i in range(10):
            banner = Banner(id=0, idAdmin=admin_inserido, status=True)
            inserir_banner(banner)
        #act
        banners = obter_todos_banners()
        #assert
        assert banners is not None, "Não foi possível obter todos os banners."
        assert len(banners) == 10, "O número de banners obtidos não corresponde ao esperado."
    
    def test_obter_banner_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_banner()

        usuario = Usuario(
            id=None,
            nome="Professor Teste",
            email="oi@oi.i",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01"
        )
        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario
        admin = Admin(usuario.id, usuario.nome, usuario.email, usuario.senha, usuario.telefone, usuario.dataCriacao, "1")
        admin_inserido = inserir_admin(admin, id_usuario)
        banner = Banner(id=0, idAdmin=admin_inserido, status=True)
        idBanner = inserir_banner(banner)
        # Act
        banner_obtido = obter_banner_por_id(idBanner)
        # Assert
        assert banner_obtido is not None, "Não foi possível obter o banner pelo ID."
        assert banner_obtido.id == idBanner, "O ID do banner obtido não corresponde ao esperado."
        assert banner_obtido.idAdmin == banner.idAdmin, "O idAdmin do banner obtido não corresponde ao esperado."
        assert banner_obtido.status == banner.status, "O status do banner obtido não corresponde ao esperado."
    
    def test_obter_banner_paginado(self, test_db):
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_banner()

        usuario = Usuario(
            id=None,
            nome="Professor Teste",
            email="oi@oi.i",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01"
        )
        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario
        admin = Admin(usuario.id, usuario.nome, usuario.email, usuario.senha, usuario.telefone, usuario.dataCriacao, "1")
        admin_inserido = inserir_admin(admin, id_usuario)
        for i in range(10):
            banner = Banner(id=0, idAdmin=admin_inserido, status=True)
            inserir_banner(banner)
        # Act
        banners_paginados = obter_banner_paginado(0, 5)
        # Assert
        assert banners_paginados is not None, "Não foi possível obter os banners paginados."
        assert len(banners_paginados) == 5, "O número de banners paginados obtidos não corresponde ao esperado."

    def test_atualizar_banner(self, test_db):
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_banner()

        usuario = Usuario(
            id=None,
            nome="Professor Teste",
            email="oi@oi.i",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01"
        )
        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario
        admin = Admin(usuario.id, usuario.nome, usuario.email, usuario.senha, usuario.telefone, usuario.dataCriacao, "1")
        admin_inserido = inserir_admin(admin, id_usuario)
        banner = Banner(id=0, idAdmin=admin_inserido, status=True)
        idBanner = inserir_banner(banner)

        # Act
        banner.status = False
        banner.id = idBanner
        resultado_atualizacao = atualizar_banner(banner)

        # Assert
        assert resultado_atualizacao is not None, "Não foi possível atualizar o banner."
        banner_atualizado = obter_banner_por_id(idBanner)
        assert banner_atualizado.status == False, "O status do banner atualizado não corresponde ao esperado."

    def test_deletar_banner(self, test_db):
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_banner()

        usuario = Usuario(
            id=None,
            nome="Professor Teste",
            email="oi@oi.i",
            senha="senha123",
            telefone="123456789",
            dataCriacao="2023-01-01"
        )
        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario
        admin = Admin(usuario.id, usuario.nome, usuario.email, usuario.senha, usuario.telefone, usuario.dataCriacao, "1")
        admin_inserido = inserir_admin(admin, id_usuario)
        banner = Banner(id=0, idAdmin=admin_inserido, status=True)
        idBanner = inserir_banner(banner)

        # Act
        resultado_delecao = deletar_banner(idBanner)

        # Assert
        assert resultado_delecao is True, "Não foi possível deletar o banner."
        banner_deletado = obter_banner_por_id(idBanner)
        assert banner_deletado is None, "O banner ainda existe após a tentativa de deleção."


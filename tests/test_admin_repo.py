from data.admin.admin_repo import *
from data.usuario.usuario_repo import *

class TestAdminRepo:
    def test_criar_tabela_admin(self, test_db):
        # Arrange
        criar_tabela_usuario()
        # Act
        resultado = criar_tabela_admin()
        # Assert
        assert resultado is True, "A criação da tabela admin não deve retornar nenhum valor"


    def test_inserir_admin(self, test_db):
    # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=None,
            nome="Professor Teste",
            email="professor.teste@example.com",
            senha="senha123",
            telefone="123456789",
            data_nascimento="2023-01-01",
            perfil="professor",
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2023-10-10",
            foto=None
        )
        
        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario  # Atualiza o objeto com o ID retornado

        admin = Admin(usuario.id, usuario.nome, usuario.email, usuario.senha, usuario.telefone, usuario.dataCriacao, "1")
        
        # Act
        admin_inserido = inserir_admin(admin, id_usuario)
        admin_db = obter_admin_por_id(admin_inserido)
        

        # Assert
        assert admin_db is not None, "Admin não foi encontrado no banco"
        assert admin_db.nivelAcesso == 1, "Professor não achou nível de acesso"
        assert admin_db.id == id_usuario, "Tá errado o id de admin"
        assert admin_db.email == "professor.teste@example.com"
        assert admin_db.telefone == usuario.telefone, "Tá errado o telefone de admin"
        assert admin_db.dataCriacao == usuario.dataCriacao,  "Tá errada a data de criação de admin"


    def test_obter_todos_admins(self, test_db):
    # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuarios = [
            Usuario(
                id=None,
                nome="Admin Um",
                email="admin1@example.com",
                senha="senha1",
                telefone="111111111",
                dataCriacao="2023-01-01"
            ),
            Usuario(
                id=None,
                nome="Admin Dois",
                email="admin2@example.com",
                senha="senha2",
                telefone="222222222",
                dataCriacao="2023-01-02"
            )
        ]

        admins_ids = []
        for i, usuario in enumerate(usuarios):
            usuario_id = inserir_usuario(usuario)
            usuario.id = usuario_id
            admin = Admin(
                id=usuario.id,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataCriacao=usuario.dataCriacao,
                nivelAcesso=i + 1  # Só pra variar um pouco o nível
            )
            id_admin = inserir_admin(admin, usuario.id)
            admins_ids.append(id_admin)

        # Act
        lista_admins = obter_todos_admins()

        # Assert
        assert lista_admins is not None, "A lista de admins não deve ser None"
        assert len(lista_admins) >= 2, "Deveria haver pelo menos dois admins na lista"

        emails_esperados = {u.email for u in usuarios}
        emails_retorno = {admin.email for admin in lista_admins}

        assert emails_esperados.issubset(emails_retorno), "Nem todos os admins esperados foram retornados"


    def test_obter_admin_por_email(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=None,
            nome="Admin Email",
            email="admin.email@example.com",
            senha="senhaemail",
            telefone="5551999999999",
            dataCriacao="2023-02-02"
        )

        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario

        admin = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            nivelAcesso=2
        )

        inserir_admin(admin, usuario.id)

        # Act
        admin_encontrado = obter_admin_por_email("admin.email@example.com")

        # Assert
        assert admin_encontrado is not None, "Admin não encontrado por email"
        assert admin_encontrado.email == "admin.email@example.com"
        assert admin_encontrado.nivelAcesso == 2
        assert admin_encontrado.id == id_usuario
        assert admin_encontrado.nome == "Admin Email"

    
    def test_obter_admin_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=None,
            nome="Admin ID",
            email="admin.id@example.com",
            senha="senhaid",
            telefone="44999999999",
            dataCriacao="2023-03-03"
        )

        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario

        admin = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            nivelAcesso=3
        )

        id_admin = inserir_admin(admin, id_usuario)

        # Act
        admin_encontrado = obter_admin_por_id(id_admin)

        # Assert
        assert admin_encontrado is not None, "Admin não encontrado por ID"
        assert admin_encontrado.id == id_usuario
        assert admin_encontrado.email == "admin.id@example.com"
        assert admin_encontrado.nivelAcesso == 3
        assert admin_encontrado.nome == "Admin ID"


    def test_atualizar_admin_por_email(test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=None,
            nome="Admin Original",
            email="admin.atualizar@example.com",
            senha="originalsenha",
            telefone="555555555",
            dataCriacao="2023-04-04"
        )

        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario

        admin = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            nivelAcesso=1
        )

        inserir_admin(admin, id_usuario)

        # Act
        admin_atualizado = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            nivelAcesso=3  # novo nível de acesso
        )

        atualizar_admin_por_email(admin_atualizado, usuario.email)

        # Assert
        admin_db = obter_admin_por_email(usuario.email)
        assert admin_db is not None
        assert admin_db.nivelAcesso == 3
        assert admin_db.email == usuario.email


    def test_excluir_admin_por_email(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=None,
            nome="Admin Exclusão",
            email="admin.excluir@example.com",
            senha="senha_delete",
            telefone="777777777",
            dataCriacao="2023-05-05"
        )
        usuario_id = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_id)

        admin = Admin(
            id=usuario_db.id,
            nome=usuario_db.nome,
            email=usuario_db.email,
            senha=usuario_db.senha,
            telefone=usuario_db.telefone,
            dataCriacao=usuario_db.dataCriacao,
            nivelAcesso=2
        )
        inserir_admin(admin, usuario_db.id)

        # Act
        email = usuario_db.email
        resultado = excluir_admin_por_email(email)

        # Assert
        assert resultado is True, "O admin não foi excluído"
        admin_excluido = obter_admin_por_email(email)
        assert admin_excluido is None, "O admin com esse email excluído deveria ser None ou seja não existir mais"


    def test_obter_admin_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()
        for i in range(10):
            usuario = Usuario(
                id=None,
                nome=f"admin{i+1}",
                email=f"admin{i+1}@gmail.com",
                senha=f"senha{i+1}",
                telefone=f"9999-{i+1:04d}",
                dataCriacao=f"2023-06-{i+1:02d}"
            )
            id_usuario = inserir_usuario(usuario)
            usuario.id = id_usuario
            admin = Admin(
                id=usuario.id,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataCriacao=usuario.dataCriacao,
                nivelAcesso=i + 1
            )
            inserir_admin(admin, usuario.id)

        # Act
        admins1 = obter_admin_paginado(1, 4)
        admins2 = obter_admin_paginado(2, 4)
        admins3 = obter_admin_paginado(3, 4)

        # Assert
        assert len(admins1) == 4, "Na primeira página deveria haver 4 admins"
        assert len(admins2) == 4, "Na segunda página deveria haver 4 admins"
        assert admins3[0].id == 9, "O primeiro id da terceira página deveria ser 9"


    def test_obter_admin_por_termo_paginado(self, test_db):
        #Arrannge
        criar_tabela_usuario()
        criar_tabela_admin()

        for i in range(1, 6): #eu basicamente estou criando 5 usuários e admins
            usuario = Usuario(
                id=None,
                nome=f"Admin {i}",
                email=f"admin{i}@gmail.com",
                senha=f"senha{i}",
                telefone=f"9999-{i}",
                dataCriacao=f"2023-01-0{i}"
            )
            id_usuario = inserir_usuario(usuario)
            usuario.id = id_usuario
            admin = Admin(
                id=usuario.id,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataCriacao=usuario.dataCriacao,
                nivelAcesso=i
            )
            inserir_admin(admin, usuario.id)
        
        #Act
        resultado1 = obter_admin_por_termo_paginado("admin", 1, 2)
        resultado2 = obter_admin_por_termo_paginado("admin", 2, 2)
        resultado3 = obter_admin_por_termo_paginado("admin", 3, 2)

        #Assert
        assert len(resultado1) == 2 #esse trecho serve para testar a 1º página que como tem pg_size dois deve retornar dois admins
        assert len(resultado2) == 2
        assert resultado3[0].id == 5 #vê se o admin dá última página é o quinto id


    def test_obter_quantidade_admins(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        for i in range(1, 4):
            usuario = Usuario(
                id=0,
                nome=f"Admin {i}",
                email=f"admin{i}@example.com",
                senha="senha123",
                telefone=f"1199999999{i}",
                dataCriacao="2025-07-01"
            )
            usuario_id = inserir_usuario(usuario)

            admin = Admin(
                id=usuario.id,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataCriacao= usuario.dataCriacao,
                nivelAcesso=1
            )

            inserir_admin(admin, usuario_id)

        # Act
        quantidade = obter_quantidade_admins()

        # Assert
        assert quantidade == 3, "A quantidade de admins deveria ser 3"


    def test_atualizar_admin_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=0,
            nome="Admin Teste",
            email="admin@example.com",
            senha="senha123",
            telefone="11999999999",
            dataCriacao="2025-07-01"
        )
        usuario_id = inserir_usuario(usuario)

        admin = Admin(
            id=usuario_id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            nivelAcesso=1
        )
        inserir_admin(admin, usuario_id)

        # Act
        admin_atualizado = Admin(
            id=usuario_id,
            nome=admin.nome,
            email=admin.email,
            senha=admin.senha,
            telefone=admin.telefone,
            dataCriacao=admin.dataCriacao,
            nivelAcesso=3  # novo nível de acesso atualizado
        )

        atualizar_admin_por_id(admin_atualizado, usuario_id) #atualiza o admin pelo id

        admin_buscado = obter_admin_por_id(usuario_id) #busca na BD esse admin atualizado pelo id

        # Assert
        assert admin_buscado.nivelAcesso == 3, "O nível de acesso do admin deveria ser atualizado para 5"


    def test_excluir_admin_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=0,
            nome="Admin Deletável",
            email="deletavel@example.com",
            senha="senha123",
            telefone="11999999998",
            dataCriacao="2025-07-01"
        )
        usuario_id = inserir_usuario(usuario)

        admin = Admin(
            id=usuario_id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataCriacao=usuario.dataCriacao,
            nivelAcesso=1
        )
        inserir_admin(admin, usuario_id)

        # Garantir que o admin está lá
        admin_existente = obter_admin_por_id(usuario_id)
        assert admin_existente is not None, "Admin deveria estar presente antes da exclusão"

        # Act
        excluir_admin_por_id(usuario_id)

        # Assert
        admin_excluido = obter_admin_por_id(usuario_id)
        assert admin_excluido is None, "O admin deveria ter sido removido do banco de dados"

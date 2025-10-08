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
            dataNascimento="2023-01-01",
            perfil="professor",
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2023-10-10",
            foto=None
        )
        
        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario  # Atualiza o objeto com o ID retornado

        admin = Admin(usuario.id, usuario.nome, usuario.email, usuario.senha, usuario.telefone, usuario.dataNascimento, 
        usuario.perfil, usuario.token_redefinicao, usuario.data_token, usuario.data_cadastro, usuario.foto, "1")
        
        # Act
        admin_inserido = inserir_admin(admin, id_usuario)
        admin_db = obter_admin_por_id(admin_inserido)
        

        # Assert
        assert admin_db is not None, "Admin não foi encontrado no banco"
        assert admin_db.nivelAcesso == 1, "Professor não achou nível de acesso"
        assert admin_db.id == id_usuario, "Tá errado o id de admin"
        assert admin_db.nome == "Professor Teste", "Tá errado o nome de admin"
        assert admin_db.email == "professor.teste@example.com"
        assert admin_db.senha == usuario.senha, "Tá errada a senha de admin"
        assert admin_db.telefone == usuario.telefone, "Tá errado o telefone de admin"
        assert admin_db.dataNascimento == usuario.dataNascimento,  "Tá errada a data de nascimento de admin"
        assert admin_db.perfil == "professor", "Tá errado o perfil de admin"
        assert admin.token_redefinicao == None, "Tá errado o token de admin"
        assert admin.data_token == None, "Tá errada a data do token de admin"
        assert admin.data_cadastro == "2023-10-10", "Tá errada a data de cadastro de admin"
        assert admin.foto == None, "Tá errada a foto de admin"


    def test_obter_todos_admins(self, test_db):
    # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuarios = [
            Usuario(
            id=None,
            nome="Admin Teste",
            email="admin.teste@example.com",
            senha="senha123",
            telefone="123456789",
            dataNascimento="2023-01-01",
            perfil="cliente",
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2023-10-10",
            foto=None
            ),
            Usuario(
                id=None,
                nome="Admin Dois",
                email="admin2@example.com",
                senha="senha2",
                telefone="222222222",
                dataNascimento="2023-01-02",
                perfil="cliente",
                token_redefinicao=None,
                data_token=None,
                data_cadastro="2023-10-10",
                foto=None
            ),
            Usuario(
                id=None,
                nome="Admin Três",
                email="admin3@example.com",
                senha="senha3",
                telefone="333333333",
                dataNascimento="2015-01-02",
                perfil="cliente",
                token_redefinicao=None,
                data_token=None,
                data_cadastro="2023-10-10",
                foto=None
            )
            #... você pode adicionar mais usuários conforme necessário para o teste ...
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
                dataNascimento=usuario.dataNascimento,
                perfil=usuario.perfil,
                token_redefinicao=usuario.token_redefinicao,
                data_token=usuario.data_token,
                data_cadastro=usuario.data_cadastro,
                foto=usuario.foto,
                nivelAcesso=i + 1  # Só pra variar um pouco o nível
            )
            id_admin = inserir_admin(admin, usuario.id)
            admins_ids.append(id_admin)

        # Act
        lista_admins = obter_todos_admins()

        # Assert
        assert lista_admins is not None, "A lista de admins não deve ser None"
        assert len(lista_admins) >= 3, "Deveria haver pelo menos três admins na lista"

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
            dataNascimento="2013-02-02",
            perfil="cliente",
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2023-10-10",
            foto=None
        )

        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario

        admin = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataNascimento=usuario.dataNascimento,
            perfil=usuario.perfil,
            token_redefinicao=usuario.token_redefinicao,    
            data_token=usuario.data_token,
            data_cadastro=usuario.data_cadastro,
            foto=usuario.foto,
            nivelAcesso=2
        )

        inserir_admin(admin, usuario.id)

        # Act
        admin_encontrado = obter_admin_por_email("admin.email@example.com")

        # Assert
        assert admin_encontrado is not None, "Admin não encontrado por email"
        assert admin_encontrado.id == admin.id
        assert admin_encontrado.nome == admin.nome, "Nome do admin não corresponde ao esperado"
        assert admin_encontrado.email == admin.email, "Email do admin não corresponde ao esperado"
        assert admin_encontrado.senha == admin.senha, "Senha do admin não corresponde ao esperado"
        assert admin_encontrado.telefone == admin.telefone, "Telefone do admin não corresponde ao esperado"
        assert admin_encontrado.dataNascimento == admin.dataNascimento, "Data de nascimento do admin não corresponde ao esperado"  
        assert admin_encontrado.perfil == admin.perfil, "Perfil do admin não corresponde ao esperado"
        assert admin_encontrado.token_redefinicao == admin.token_redefinicao, "Token de redefinição do admin não corresponde ao esperado"
        assert admin_encontrado.data_token == admin.data_token, "Data do token do admin não corresponde ao esperado"
        assert admin_encontrado.data_cadastro == admin.data_cadastro, "Data de cadastro do admin não corresponde ao esperado"
        assert admin_encontrado.foto == admin.foto, "Foto do admin não corresponde ao esperado"
        assert admin_encontrado.nivelAcesso == admin.nivelAcesso, "Nível de acesso do admin não corresponde ao esperado"

    
    def test_obter_admin_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=None,
            nome="Admin Buscar por ID",
            email="admin.id@example.com",
            senha="senhaid",
            telefone="8888888888",
            dataNascimento="2023-07-07",
            perfil="cliente",  # Incluindo o campo 'perfil'
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2023-10-10",
            foto=None
        )

        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario

        admin = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataNascimento=usuario.dataNascimento,
            perfil=usuario.perfil,
            token_redefinicao=usuario.token_redefinicao,
            data_token=usuario.data_token,
            data_cadastro=usuario.data_cadastro,
            foto=usuario.foto,
            nivelAcesso=1
        )
        inserir_admin(admin, usuario.id)

        # Act
        admin_obtido = obter_admin_por_id(usuario.id)

        # Assert
        assert admin_obtido is not None, "O admin deveria ser encontrado pelo ID"
        assert admin_obtido.id == usuario.id, f"Esperado ID {usuario.id}, mas obtido {admin_obtido.id}"
        assert admin_obtido.email == usuario.email, f"Esperado email {usuario.email}, mas obtido {admin_obtido.email}"
        assert admin_obtido.nivelAcesso == 1, f"Esperado nível de acesso 1, mas obtido {admin_obtido.nivelAcesso}"
        assert admin_obtido.nome == usuario.nome, f"Esperado nome {usuario.nome}, mas obtido {admin_obtido.nome}"
        assert admin_obtido.senha == usuario.senha, f"Esperado senha {usuario.senha}, mas obtido {admin_obtido.senha}"
        assert admin_obtido.telefone == usuario.telefone, f"Esperado telefone {usuario.telefone}, mas obtido {admin_obtido.telefone}"
        assert admin_obtido.dataNascimento == usuario.dataNascimento, f"Esperado data de nascimento {usuario.dataNascimento}, mas obtido {admin_obtido.dataNascimento}"
        assert admin_obtido.perfil == usuario.perfil, f"Esperado perfil {usuario.perfil}, mas obtido {admin_obtido.perfil}"
        assert admin_obtido.token_redefinicao == usuario.token_redefinicao, f"Esperado token de redefinição {usuario.token_redefinicao}, mas obtido {admin_obtido.token_redefinicao}"
        assert admin_obtido.data_token == usuario.data_token, f"Esperado data do token {usuario.data_token}, mas obtido {admin_obtido.data_token}"
        assert admin_obtido.data_cadastro == usuario.data_cadastro, f"Esperado data de cadastro {usuario.data_cadastro}, mas obtido {admin_obtido.data_cadastro}"
        assert admin_obtido.foto == usuario.foto, f"Esperado foto {usuario.foto}, mas obtido {admin_obtido.foto}"


    def test_atualizar_admin_por_email(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=None,
            nome="Admin Original",
            email="admin.atualizar.email@example.com",
            senha="senhaoriginal",
            telefone="5555555555",
            dataNascimento="2023-04-04",
            perfil="cliente",  # Incluindo o campo 'perfil'
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2023-10-10",
            foto=None
        )

        id_usuario = inserir_usuario(usuario)
        usuario.id = id_usuario

        admin = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataNascimento=usuario.dataNascimento,
            perfil=usuario.perfil,
            token_redefinicao=usuario.token_redefinicao,
            data_token=usuario.data_token,
            data_cadastro=usuario.data_cadastro,
            foto=usuario.foto,
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
            dataNascimento=usuario.dataNascimento,
            perfil=usuario.perfil,
            token_redefinicao=usuario.token_redefinicao,
            data_token=usuario.data_token,
            data_cadastro=usuario.data_cadastro,
            foto=usuario.foto,
            nivelAcesso=2  # Novo nível de acesso
        )

        atualizar_admin_por_email(admin_atualizado, usuario.email)

        # Assert
        admin_db = obter_admin_por_email(usuario.email)
        assert admin_db is not None
        assert admin_db.nivelAcesso == 2, "O nível de acesso do admin deveria ser atualizado para 2"
        assert admin_db.email == usuario.email, "O email do admin deveria ser o mesmo"


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
            dataNascimento="2023-05-05",
            perfil="cliente",  # Incluindo o campo 'perfil'
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2023-10-10",
            foto=None
        )
        # Inserindo o usuário no banco de dados
        usuario_id = inserir_usuario(usuario)
        usuario_db = obter_usuario_por_id(usuario_id)

        # Criando o Admin a partir do usuário
        admin = Admin(
            id=usuario_db.id,
            nome=usuario_db.nome,
            email=usuario_db.email,
            senha=usuario_db.senha,
            telefone=usuario_db.telefone,
            dataNascimento=usuario_db.dataNascimento,
            perfil=usuario_db.perfil,
            token_redefinicao=usuario_db.token_redefinicao,
            data_token=usuario_db.data_token,
            data_cadastro=usuario_db.data_cadastro,
            foto=usuario_db.foto,
            nivelAcesso=2
        )
        # Inserindo o Admin no banco de dados
        inserir_admin(admin, usuario_db.id)

        # Garantir que o admin foi inserido
        admin_existente = obter_admin_por_email("admin.excluir@example.com")
        assert admin_existente is not None, "O admin deveria estar presente antes da exclusão"

        # Act - Excluir o admin pelo email
        email = usuario_db.email
        resultado = excluir_admin_por_email(email)

        # Assert
        assert resultado is True, "O admin não foi excluído com sucesso"
        
        # Verificando se o admin foi realmente excluído
        admin_excluido = obter_admin_por_email(email)
        assert admin_excluido is None, "O admin com o email fornecido deveria ter sido excluído"


    def test_obter_admin_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        for i in range(15):  # Criando 15 admins para testar a paginação
            usuario = Usuario(
                id=None,
                nome=f"admin{i+1}",
                email=f"admin{i+1}@gmail.com",
                senha=f"senha{i+1}",
                telefone=f"9999-{i+1:04d}",
                dataNascimento=f"2023-06-{i+1:02d}",
                perfil="cliente",  # Incluindo o campo 'perfil'
                token_redefinicao=None,
                data_token=None,
                data_cadastro="2023-10-10",
                foto=None
            )
            id_usuario = inserir_usuario(usuario)
            usuario.id = id_usuario
            admin = Admin(
                id=usuario.id,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataNascimento=usuario.dataNascimento,
                perfil=usuario.perfil,
                token_redefinicao=usuario.token_redefinicao,
                data_token=usuario.data_token,
                data_cadastro=usuario.data_cadastro,
                foto=usuario.foto,
                nivelAcesso=i + 1
            )
            inserir_admin(admin, usuario.id)

        # Act
        admins1 = obter_admin_paginado(1, 5)
        admins2 = obter_admin_paginado(2, 5)
        admins3 = obter_admin_paginado(3, 5)

        # Assert
        assert len(admins1) == 5, "Na primeira página deveria haver 5 admins"
        assert len(admins2) == 5, "Na segunda página deveria haver 5 admins"
        assert len(admins3) == 5, "Na terceira página deveria haver 5 admins"
        assert admins1[0].nome == "admin1", "O primeiro admin da primeira página deveria ser admin1"
        assert admins2[0].nome == "admin6", "O primeiro admin da segunda página deveria ser admin6"
        assert admins3[0].nome == "admin11", "O primeiro admin da terceira página deveria ser admin11"


    def test_obter_admin_por_termo_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        # Criar 5 admins com nomes e e-mails contendo "admin"
        for i in range(1, 6):
            usuario = Usuario(
                id=None,
                nome=f"Admin Termo {i}",
                email=f"admin.termo{i}@example.com",
                senha=f"senha{i}",
                telefone=f"9999-000{i}",
                dataNascimento=f"2023-01-0{i}",
                perfil="cliente",
                token_redefinicao=None,
                data_token=None,
                data_cadastro="2023-10-10",
                foto=None
            )

            id_usuario = inserir_usuario(usuario)
            usuario.id = id_usuario

            admin = Admin(
                id=usuario.id,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataNascimento=usuario.dataNascimento,
                perfil=usuario.perfil,
                token_redefinicao=usuario.token_redefinicao,
                data_token=usuario.data_token,
                data_cadastro=usuario.data_cadastro,
                foto=usuario.foto,
                nivelAcesso=i
            )

            inserir_admin(admin, usuario.id)

        # Act
        resultado_pagina1 = obter_admin_por_termo_paginado("admin", 1, 2)  # Deve trazer os 2 primeiros
        resultado_pagina2 = obter_admin_por_termo_paginado("admin", 2, 2)  # Deve trazer os 2 seguintes
        resultado_pagina3 = obter_admin_por_termo_paginado("admin", 3, 2)  # Deve trazer o último

        # Assert
        assert len(resultado_pagina1) == 2, "Página 1 deveria conter 2 admins"
        assert resultado_pagina1[0].nome.startswith("Admin Termo"), "Nome do admin da página 1 inválido"

        assert len(resultado_pagina2) == 2, "Página 2 deveria conter 2 admins"
        assert resultado_pagina2[0].email.startswith("admin.termo"), "Email da página 2 inválido"

        assert len(resultado_pagina3) == 1, "Página 3 deveria conter apenas 1 admin"
        assert resultado_pagina3[0].nome == "Admin Termo 5", "Último admin da página 3 deveria ser o Admin Termo 5"



    def test_obter_quantidade_admins(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        for i in range(1, 4):  # Criando 3 admins
            usuario = Usuario(
                id=None,
                nome=f"Admin {i}",
                email=f"admin{i}@example.com",
                senha="senha123",
                telefone=f"1199999999{i}",
                dataNascimento="2025-07-01",
                perfil="cliente",  # Incluindo o campo 'perfil'
                token_redefinicao=None,
                data_token=None,
                data_cadastro="2023-10-10",
                foto=None
            )
            usuario_id = inserir_usuario(usuario)

            admin = Admin(
                id=usuario.id,
                nome=usuario.nome,
                email=usuario.email,
                senha=usuario.senha,
                telefone=usuario.telefone,
                dataNascimento=usuario.dataNascimento,
                perfil=usuario.perfil,
                token_redefinicao=usuario.token_redefinicao,
                data_token=usuario.data_token,
                data_cadastro=usuario.data_cadastro,
                foto=usuario.foto,
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
            id=None,
            nome="Admin Atualizar",
            email="atualizar@example.com",
            senha="senha123",
            telefone="11999999999",
            dataNascimento="2025-07-01",
            perfil="cliente",
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2025-10-01",
            foto=None
        )
        usuario_id = inserir_usuario(usuario)
        usuario.id = usuario_id

        admin = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataNascimento=usuario.dataNascimento,
            perfil=usuario.perfil,
            token_redefinicao=usuario.token_redefinicao,
            data_token=usuario.data_token,
            data_cadastro=usuario.data_cadastro,
            foto=usuario.foto,
            nivelAcesso=1
        )
        inserir_admin(admin, usuario_id)

        # Act: atualizar o nível de acesso
        admin_atualizado = Admin(
            id=usuario_id,
            nome=admin.nome,
            email=admin.email,
            senha=admin.senha,
            telefone=admin.telefone,
            dataNascimento=admin.dataNascimento,
            perfil=admin.perfil,
            token_redefinicao=admin.token_redefinicao,
            data_token=admin.data_token,
            data_cadastro=admin.data_cadastro,
            foto=admin.foto,
            nivelAcesso=5
        )

        atualizar_admin_por_id(admin_atualizado, usuario_id)

        # Assert
        admin_banco = obter_admin_por_id(usuario_id)
        assert admin_banco is not None, "O admin deveria existir após atualização"
        assert admin_banco.nivelAcesso == 5, "O nível de acesso do admin não foi atualizado corretamente"
        assert admin_banco.email == "atualizar@example.com"



    def test_excluir_admin_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_admin()

        usuario = Usuario(
            id=None,
            nome="Admin Para Excluir",
            email="excluir@example.com",
            senha="senha123",
            telefone="11988888888",
            dataNascimento="2025-07-01",
            perfil="cliente",
            token_redefinicao=None,
            data_token=None,
            data_cadastro="2025-10-01",
            foto=None
        )
        usuario_id = inserir_usuario(usuario)
        usuario.id = usuario_id

        admin = Admin(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha,
            telefone=usuario.telefone,
            dataNascimento=usuario.dataNascimento,
            perfil=usuario.perfil,
            token_redefinicao=usuario.token_redefinicao,
            data_token=usuario.data_token,
            data_cadastro=usuario.data_cadastro,
            foto=usuario.foto,
            nivelAcesso=2
        )
        inserir_admin(admin, usuario_id)

        # Garantir que o admin foi inserido
        admin_existente = obter_admin_por_id(usuario_id)
        assert admin_existente is not None, "Admin deveria existir antes da exclusão"

        # Act
        resultado = excluir_admin_por_id(usuario_id)

        # Assert
        assert resultado is True, "A função deveria retornar True após exclusão bem-sucedida"
        admin_deletado = obter_admin_por_id(usuario_id)
        assert admin_deletado is None, "O admin deveria ter sido removido do banco de dados"



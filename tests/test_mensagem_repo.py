import sys
import os
from data.mensagem.mensagem_repo import *
from data.usuario.usuario_repo import *

class TestMensagemRepo:
    def test_criar_tabela_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        # Act
        resultado = criar_tabela_mensagem()
        # Assert
        assert resultado is True, "A tabela de mensagens não foi criada"


    def test_inserir_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuarioremetente = Usuario(0, "lorenzo", "lorenzo@gmail.com", "hfevh", "3175549-98", "210109")
        id_remetente = inserir_usuario(usuarioremetente)
        usuariodestinatario = Usuario(1, "mateus", "mateus@gmail.com", "mt123", "1234567-11","220209")
        id_destinatario = inserir_usuario(usuariodestinatario)
        criar_tabela_mensagem()
        # Act
        mensagem = Mensagem(0,id_remetente,id_destinatario,"conteudo da mensagem","2023-10-01", "12:00:00",False )
        mensagem_inserida = inserir_mensagem(mensagem)
        mensagem_db = obter_mensagem_por_id(mensagem_inserida)
        # Assert
        assert mensagem_db is not None, "A mensagem não foi inserida"
        assert mensagem_db.id == 1, "O id da mensagem está incorreto"
        assert mensagem_db.idRmetente == id_remetente, "O id do remetente está incorreto"
        assert mensagem_db.idDestinatario == id_destinatario, "O id do destinatario está incorreto"
        assert mensagem_db.conteudo == "conteudo da mensagem", "O conteúdo da mensagem está incorreto"
        assert mensagem_db.dataEnvio == "2023-10-01", "A data de envio está incorreta"
        assert mensagem_db.horaEnvio == "12:00:00", "A hora de envio está incorreta"
        assert mensagem_db.visualizacao is 0, "O status de visualização está incorreto"
    
    def test_obter_todas_mensagens(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuarioremetente = Usuario(0, "lorenzo", "lorenzo@gmail.com", "hfevh", "3175549-98", "210109")
        id_remetente = inserir_usuario(usuarioremetente)
        usuariodestinatario = Usuario(1, "mateus", "mateus@gmail.com", "mt123", "1234567-11","220209")
        id_destinatario = inserir_usuario(usuariodestinatario)
        criar_tabela_mensagem()
        for m in range(10):
            mensagem = Mensagem(0,id_remetente,id_destinatario, "conteudo da mensagem","2023-10-01", "12:00:00",False )
            inserir_mensagem(mensagem)
        # Act
        mensagens = obter_mensagens()
        # Assert
        assert len(mensagens) == 10, "Deveria haver 10 mensagens" 

    import sys
import os
from data.mensagem.mensagem_repo import *
from data.usuario.usuario_repo import *

class TestMensagemRepo:
    def test_criar_tabela_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        # Act
        resultado = criar_tabela_mensagem()
        # Assert
        assert resultado is True, "A tabela de mensagens não foi criada"

    def test_inserir_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        usuarioremetente = Usuario(0, "lorenzo", "lorenzo@gmail.com", "hfevh", "3175549-98", "210109")
        id_remetente = inserir_usuario(usuarioremetente)
        usuariodestinatario = Usuario(1, "mateus", "mateus@gmail.com", "mt123", "1234567-11","220209")
        id_destinatario = inserir_usuario(usuariodestinatario)
        criar_tabela_mensagem()
        # Act
        mensagem = Mensagem(0, id_remetente, id_destinatario, "conteudo da mensagem", "2023-10-01", "12:00:00", False)
        mensagem_inserida = inserir_mensagem(mensagem)
        mensagem_db = obter_mensagem_por_id(mensagem_inserida)
        # Assert
        assert mensagem_db is not None, "A mensagem não foi inserida"
        assert mensagem_db.id == mensagem_inserida, "O id da mensagem está incorreto"
        assert mensagem_db.idRmetente == id_remetente, "O id do remetente está incorreto"
        assert mensagem_db.idDestinatario == id_destinatario, "O id do destinatario está incorreto"
        assert mensagem_db.conteudo == "conteudo da mensagem", "O conteúdo da mensagem está incorreto"
        assert mensagem_db.dataEnvio == "2023-10-01", "A data de envio está incorreta"
        assert mensagem_db.horaEnvio == "12:00:00", "A hora de envio está incorreta"
        assert mensagem_db.visualizacao is 0, "O status de visualização está incorreto"

    def test_obter_todas_mensagens(self, test_db):
        # Arrange
        criar_tabela_usuario()
        remetente = Usuario(0, "lorenzo", "lorenzo@gmail.com", "hfevh", "3175549-98", "210109")
        id_rem = inserir_usuario(remetente)
        destinatario = Usuario(1, "mateus", "mateus@gmail.com", "mt123", "1234567-11","220209")
        id_dest = inserir_usuario(destinatario)
        criar_tabela_mensagem()
        for _ in range(10):
            msg = Mensagem(0, id_rem, id_dest, "abc", "2023-10-01", "12:00:00", False)
            inserir_mensagem(msg)
        # Act
        mensagens = obter_mensagens()
        # Assert
        assert len(mensagens) == 10, "Deveria haver 10 mensagens"

    def test_obter_mensagem_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        id_rem, id_dest = inserir_usuario(Usuario(0,"a","a@","u","p","d")), inserir_usuario(Usuario(1,"b","b@","u","p","d"))
        criar_tabela_mensagem()
        for i in range(7):
            inserir_mensagem(Mensagem(0, id_rem, id_dest, f"msg{i}", "2023-10-01", "12:00:00", False))
        # Act
        page1 = obter_mensagem_paginado(1, 3)
        page2 = obter_mensagem_paginado(2, 3)
        page3 = obter_mensagem_paginado(3, 3)
        # Assert
        assert len(page1) == 3, "Página 1 deveria ter 3 mensagens"
        assert len(page2) == 3, "Página 2 deveria ter 3 mensagens"
        assert len(page3) == 1, "Página 3 deveria ter 1 mensagem"

    def test_obter_mensagem_por_termo_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        id_rem, id_dest = inserir_usuario(Usuario(0,"x","x@","u","p","d")), inserir_usuario(Usuario(1,"y","y@","u","p","d"))
        criar_tabela_mensagem()
        for txt in ["foo", "barfoo", "baz", "fooqux", "quux"]:
            inserir_mensagem(Mensagem(0, id_rem, id_dest, txt, "2023-10-01", "12:00:00", False))
        # Act
        resultados = obter_mensagem_por_termo_paginado("foo", 1, 10)
        # Assert
        assert len(resultados) == 3, "Deveriam ser 3 mensagens contendo 'foo'"

    def test_obter_mensagem_por_nome_remetente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        u1 = Usuario(0, "ana", "ana@a","u","p","d")
        u2 = Usuario(1, "bob", "bob@b","u","p","d")
        id1, id2 = inserir_usuario(u1), inserir_usuario(u2)
        criar_tabela_mensagem()
        inserir_mensagem(Mensagem(0, id1, id2, "m1", "d","h", False))
        inserir_mensagem(Mensagem(0, id2, id1, "m2", "d","h", False))
        # Act
        msgs = obter_mensagem_por_nome_remetente("ana", 1, 10)
        # Assert
        assert all(m.idRmetente == id1 for m in msgs), "Todas devem ser de 'ana'"

    def test_obter_mensagem_por_nome_destinatario(self, test_db):
        # Arrange
        criar_tabela_usuario()
        u1 = Usuario(0, "ana", "ana@a","u","p","d")
        u2 = Usuario(1, "bob", "bob@b","u","p","d")
        id1, id2 = inserir_usuario(u1), inserir_usuario(u2)
        criar_tabela_mensagem()
        inserir_mensagem(Mensagem(0, id1, id2, "m1", "d","h", False))
        inserir_mensagem(Mensagem(0, id2, id1, "m2", "d","h", False))
        # Act
        msgs = obter_mensagem_por_nome_destinatario("bob", 1, 10)
        # Assert
        assert all(m.idDestinatario == id2 for m in msgs), "Todas devem ter destinatário 'bob'"

    def test_obter_quantidade_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        id_rem, id_dest = inserir_usuario(Usuario(0,"a","a@","u","p","d")), inserir_usuario(Usuario(1,"b","b@","u","p","d"))
        criar_tabela_mensagem()
        for _ in range(4):
            inserir_mensagem(Mensagem(0, id_rem, id_dest, "x","d","h", False))
        # Act
        qtd = obter_quantidade_mensagem()
        # Assert
        assert qtd == 4, "A quantidade total deveria ser 4"

    def test_obter_quantidade_mensagem_por_nome_remetente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        u = Usuario(0,"c","c@","u","p","d")
        idc = inserir_usuario(u)
        other = inserir_usuario(Usuario(1,"d","d@","u","p","d"))
        criar_tabela_mensagem()
        inserir_mensagem(Mensagem(0, idc, other, "x","d","h", False))
        inserir_mensagem(Mensagem(0, idc, other, "y","d","h", False))
        # Act
        qtd = obter_quantidade_mensagem_por_nome_remetente("c")
        # Assert
        assert qtd == 2, "Deveria haver 2 mensagens de 'c'"

    def test_obter_quantidade_mensagem_por_nome_destinatario(self, test_db):
        # Arrange
        criar_tabela_usuario()
        u = Usuario(0,"c","c@","u","p","d")
        idc = inserir_usuario(u)
        other = inserir_usuario(Usuario(1,"d","d@","u","p","d"))
        criar_tabela_mensagem()
        inserir_mensagem(Mensagem(0, other, idc, "x","d","h", False))
        inserir_mensagem(Mensagem(0, other, idc, "y","d","h", False))
        # Act
        qtd = obter_quantidade_mensagem_por_nome_destinatario("c")
        # Assert
        assert qtd == 2, "Deveria haver 2 mensagens para 'c'"

    def test_atualizar_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        id_rem, id_dest = inserir_usuario(Usuario(0,"a","a@","u","p","d")), inserir_usuario(Usuario(1,"b","b@","u","p","d"))
        criar_tabela_mensagem()
        mid = inserir_mensagem(Mensagem(0, id_rem, id_dest, "old","d","h", False))
        # Act
        ok = atualizar_mensagem(Mensagem(0, id_rem, id_dest, "new","d2","h2", True), mid)
        msg = obter_mensagem_por_id(mid)
        # Assert
        assert ok is True, "Deveria retornar True na atualização"
        assert msg.conteudo == "new", "Conteúdo não foi atualizado"
        assert msg.visualizacao is 1, "Visualização não foi atualizada"

    def test_atualizar_visualizacao_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        id_rem, id_dest = inserir_usuario(Usuario(0,"a","a@","u","p","d")), inserir_usuario(Usuario(1,"b","b@","u","p","d"))
        criar_tabela_mensagem()
        mid = inserir_mensagem(Mensagem(0, id_rem, id_dest, "m","d","h", False))
        # Act
        ok = atualizar_visualizacao_mensagem(True, mid)
        msg = obter_mensagem_por_id(mid)
        # Assert
        assert ok is True, "Deveria retornar True na atualização de visualização"
        assert msg.visualizacao is 1, "Visualização não foi atualizada para True"

    def test_excluir_mensagem(self, test_db):
        # Arrange
        criar_tabela_usuario()
        id_rem, id_dest = inserir_usuario(Usuario(0,"a","a@","u","p","d")), inserir_usuario(Usuario(1,"b","b@","u","p","d"))
        criar_tabela_mensagem()
        mid = inserir_mensagem(Mensagem(0, id_rem, id_dest, "x","d","h", False))
        # Act
        ok = excluir_mensagem(mid)
        msg = obter_mensagem_por_id(mid)
        # Assert
        assert ok is True, "Deveria retornar True na exclusão"
        assert msg is None, "Mensagem deveria ter sido excluída"

    def test_excluir_mensagem_por_nome_remetente(self, test_db):
        # Arrange
        criar_tabela_usuario()
        u = Usuario(0,"c","c@","u","p","d")
        idc = inserir_usuario(u)
        other = inserir_usuario(Usuario(1,"d","d@","u","p","d"))
        criar_tabela_mensagem()
        inserir_mensagem(Mensagem(0, idc, other, "x","d","h", False))
        inserir_mensagem(Mensagem(0, idc, other, "y","d","h", False))
        # Act
        ok = excluir_mensagem_por_nome_remetente("c")
        msgs = obter_mensagens()
        # Assert
        assert ok is True, "Deveria retornar True ao excluir por remetente"
        assert all(m.idRmetente != idc for m in msgs), "Todas as mensagens de 'c' deveriam ter sido excluídas"

    def test_excluir_mensagem_por_nome_destinatario(self, test_db):
        # Arrange
        criar_tabela_usuario()
        u = Usuario(0,"c","c@","u","p","d")
        idc = inserir_usuario(u)
        other = inserir_usuario(Usuario(1,"d","d@","u","p","d"))
        criar_tabela_mensagem()
        inserir_mensagem(Mensagem(0, other, idc, "x","d","h", False))
        inserir_mensagem(Mensagem(0, other, idc, "y","d","h", False))
        # Act
        ok = excluir_mensagem_por_nome_destinatario("c")
        msgs = obter_mensagens()
        # Assert
        assert ok is True, "Deveria retornar True ao excluir por destinatário"
        assert all(m.idDestinatario != idc for m in msgs), "Todas as mensagens para 'c' deveriam ter sido excluídas"
 
   



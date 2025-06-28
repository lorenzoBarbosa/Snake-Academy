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
        usuarioremetente = Usuario(
            0,
            "lorenzo",
            "lorenzo@gmail.com",
            "hfevh",
            "3175549-98",
            "210109"
        )
        id_remetente = inserir_usuario(usuarioremetente)

        usuariodestinatario = Usuario(
            1,
            "mateus",
            "mateus@gmail.com",
            "mt123",
            "1234567-11",
            "220209"
        )
        id_destinatario = inserir_usuario(usuariodestinatario)
        
        criar_tabela_mensagem()
        mensagem = Mensagem(
            0,
            id_remetente,
            id_destinatario,
            "conteudo da mensagem",
            "2023-10-01",
            "12:00:00",
            False
        )
        mensagem_inserida = inserir_mensagem(mensagem)
        mensagem_db = obter_mensagem_por_id_teste(mensagem_inserida)
        # Assert
        assert mensagem_db is not None, "A mensagem não foi inserida"
        assert mensagem_db.id == 1, "O id da mensagem está incorreto"
        assert mensagem_db.idRmetente == id_remetente, "O id do remetente está incorreto"
        assert mensagem_db.idDestinatario == id_destinatario, "O id do destinatario está incorreto"
        assert mensagem_db.conteudo == "conteudo da mensagem", "O conteúdo da mensagem está incorreto"
        assert mensagem_db.dataEnvio == "2023-10-01", "A data de envio está incorreta"
        assert mensagem_db.horaEnvio == "12:00:00", "A hora de envio está incorreta"
        assert mensagem_db.visualizacao is False, "O status de visualização está incorreto"


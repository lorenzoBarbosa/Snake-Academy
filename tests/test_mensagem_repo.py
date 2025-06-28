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


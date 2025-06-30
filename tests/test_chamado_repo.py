import sys
import os
from data.chamado.chamado_repo import *
from data.usuario.usuario_repo import *

class TestChamadoRepo:
    def test_criar_tabela_chamado(self, test_db):
        # Arrange
        criar_tabela_usuario
        # Act
        resultado = criar_tabela_chamado()
        # Assert
        assert resultado is None, "A criação da tabela deveria retornar None"
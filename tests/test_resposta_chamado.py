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
        # Assert
        criar_tabela_usuario()
        criar_tabela_admin()
        criar_tabela_chamado()
        criar_tabela_rchamado()
        


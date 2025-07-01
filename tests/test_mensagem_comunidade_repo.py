import sys
import os
from data.mensagem_comunidade.mensagem_comunidade_repo import *
from data.cliente.cliente_repo import *
from data.usuario.usuario_repo import *
from data.matricula.matricula_repo import *
from data.professor.professor_repo import *
from data.curso.curso_repo import *
from data.comunidade.comunidade_repo import *


class TestMensagemComunidadeRepo:
    
    def test_criar_tabela_mensagem_comunidade(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
    
        #Act
        resultado = criar_tabela_mensagem_comunidade()

        # Assert
        assert resultado is True, "A tabela não foi criada"
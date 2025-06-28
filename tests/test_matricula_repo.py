import sys
import os
from data.cliente.cliente_repo import *
from data.matricula.matricula_repo import *
from data.usuario.usuario_repo import *
from data.curso.curso_repo import *


class TestMatriculaRepo:
    def test_criar_tabela_matricula(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_curso()
        #Act
        resultado = criar_tabela_matricula()
        #Asserts
        assert resultado == True, "A tabela não foi criada"
import os
from random import random
import sys
import random

from data.aula.aula_repo import *
from data.cliente.cliente_repo import *
from data.matricula.matricula_repo import *
from data.modulo.modulo_repo import *
from data.professor.professor_repo import *
from data.progresso.progresso_repo import *
from data.usuario.usuario_repo import *

class TestProgressoRepo:
    def test_criar_tabela_progresso(self):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_matricula()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()
        # Act
        resultado = criar_tabela_progresso()
        # Assert
        assert resultado is True, "A tabela não foi criada"

    def test_inserir_progresso(self):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_matricula()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()
       
        usuario = Usuario(0, "claudio", f"claudio{random.randint(0,99999)}@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        matricula_obj = Matricula( 0, 1, 1, "Bom", "Bom","Bom", "12-06-2025")
        matricula_inserida = inserir_matricula(matricula_obj)
        curso_obj = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        modulo_obj = Modulo(0, curso_inserido, "Variáveis", "Muitas variáveis", [], [])
        modulo_inserido = inserir_modulo(modulo_obj)
        aula_obj = Aula(0, modulo_inserido, "Aula 1", "Aula 1 é bom", "12:36", "Bom", 0, "12-06-2025")
        aula_inserida = inserir_aula(aula_obj)
        # Act
        progresso_obj = Progresso(0, aula_inserida, matricula_inserida, "12-06-2025", "01-07-2025", "Bom",  0.75)
        progresso_inserido = inserir_progresso(progresso_obj)
        progresso_db = obter_progresso_por_id(progresso_inserido)
        # Assert
       # Assert
        assert progresso_db is not None, "O progresso não foi encontrado no banco"
        assert progresso_db.idAula == aula_inserida, "O id da aula não corresponde"
        assert progresso_db.idMatricula == matricula_inserida, "O id da matrícula não corresponde"
        assert progresso_db.dataInicio == "12-06-2025", "Data de início incorreta"
        assert progresso_db.dataFim == "01-07-2025", "Data de fim incorreta"
        assert progresso_db.statusAula == "Bom", "Status da aula incorreto"
        assert progresso_db.porcentagemConclusao == 0.75, "Porcentagem de conclusão incorreta"



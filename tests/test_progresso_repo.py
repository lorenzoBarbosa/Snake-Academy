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
    def test_criar_tabela_progresso(self, test_db):
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

    def test_inserir_progresso(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_matricula()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()
        criar_tabela_progresso()
        usuario = Usuario(0, "claudio", f"claudio@g.com", "123", "1234", "12-06-2025")
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
        assert progresso_db is not None, "O progresso não foi encontrado no banco"
        assert progresso_db.idAula == aula_inserida, "O id da aula não corresponde"
        assert progresso_db.idMatricula == matricula_inserida, "O id da matrícula não corresponde"
        assert progresso_db.dataInicio == "12-06-2025", "Data de início incorreta"
        assert progresso_db.dataFim == "01-07-2025", "Data de fim incorreta"
        assert progresso_db.statusAula == "Bom", "Status da aula incorreto"
        assert progresso_db.porcentagemConclusao == 0.75, "Porcentagem de conclusão incorreta"


    def test_obter_todos_progresso(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        # setup base
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "x","x","x","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof, 0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0, id_mod, "N","D","h","s",0,"d"))
        # insere 5
        for _ in range(5): inserir_progresso(Progresso(0, id_aula, id_mat, "d1","d2","OK",100))
        # Act
        lista = obter_todos_progresso()
        # Assert
        assert len(lista) == 5, "Deveria haver 5 registros de progresso"

    def test_obter_progresso_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "m","m","m","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        for i in range(7): inserir_progresso(Progresso(0, id_aula, id_mat, f"d{i}",f"d{i}","OK",i))
        # Act
        pg1 = obter_progresso_paginado(3, 0)
        pg2 = obter_progresso_paginado(3, 3)
        pg3 = obter_progresso_paginado(3, 6)
        # Assert
        assert len(pg1) == 3, "Página 1 deveria ter 3 itens"
        assert len(pg2) == 3, "Página 2 deveria ter 3 itens"
        assert len(pg3) == 1, "Página 3 deveria ter 1 item"

    def test_obter_progresso_por_aula(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "m","m","m","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod1 = inserir_modulo(Modulo(0,id_curso,"M1","D",[],[]))
        id_mod2 = inserir_modulo(Modulo(0,id_curso,"M2","D",[],[]))
        id_a1 = inserir_aula(Aula(0,id_mod1,"N1","D","h","s",0,"d"))
        id_a2 = inserir_aula(Aula(0,id_mod2,"N2","D","h","s",0,"d"))
        inserir_progresso(Progresso(0, id_a1, id_mat, "d","d","OK",0))
        inserir_progresso(Progresso(0, id_a2, id_mat, "d","d","OK",0))
        # Act
        lista = obter_progresso_por_aula(id_a1, 10, 0)
        # Assert
        assert all(p.idAula == id_a1 for p in lista), "Todos devem ter idAula igual"

    def test_obter_progresso_por_matricula(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_u1 = inserir_usuario(Usuario(0,"U1","u1@u","u","p","d"))
        id_u2 = inserir_usuario(Usuario(1,"U2","u2@u","u","p","d"))
        id_c1 = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_u1)
        id_p1 = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_c1)
        id_curso = inserir_curso(Curso(0,"X", id_p1,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        m1 = inserir_matricula(Matricula(0, id_u1, id_curso, "m","m","m","d"))
        m2 = inserir_matricula(Matricula(0, id_u2, id_curso, "m","m","m","d"))
        inserir_progresso(Progresso(0, id_aula, m1, "d","d","OK",0))
        inserir_progresso(Progresso(0, id_aula, m2, "d","d","OK",0))
        # Act
        lista = obter_progresso_por_matricula(m1, 10, 0)
        # Assert
        assert all(p.idMatricula == m1 for p in lista), "Todos devem ter idMatricula igual"

    def test_obter_quantidade_progresso(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "m","m","m","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        for _ in range(4): inserir_progresso(Progresso(0, id_aula, id_mat, "d","d","OK",0))
        # Act
        qtd = obter_quantidade_progresso()
        # Assert
        assert qtd == 4, "Deveria haver 4 registros de progresso"

    def test_obter_quantidade_progresso_por_aula(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "m","m","m","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        for _ in range(3): inserir_progresso(Progresso(0, id_aula, id_mat, "d","d","OK",0))
        # Act
        qtd = obter_quantidade_progresso_por_aula(id_aula)
        # Assert
        assert qtd == 3, "Deveria haver 3 registros para essa aula"

    def test_obter_quantidade_progresso_por_matricula(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        m1 = inserir_matricula(Matricula(0, id_user, id_curso, "m","m","m","d"))
        m2 = inserir_matricula(Matricula(0, id_user, id_curso, "m","m","m","d"))
        inserir_progresso(Progresso(0, id_aula, m1, "d","d","OK",0))
        inserir_progresso(Progresso(0, id_aula, m2, "d","d","OK",0))
        # Act
        qtd = obter_quantidade_progresso_por_matricula(m1)
        # Assert
        assert qtd == 2, "Deveria haver 1 registro para essa matrícula"

    def test_atualizar_progresso_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "m","m","m","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        prog_id = inserir_progresso(Progresso(0, id_aula, id_mat, "d1","d2","OLD",10))
        # Act
        ok = atualizar_progresso_por_id(prog_id, Progresso(prog_id, id_aula, id_mat, "d3","d4","NEW",20))
        prog_db = obter_progresso_por_id(prog_id)
        # Assert
        assert ok is True, "Deveria retornar True na atualização"
        assert prog_db.statusAula == "NEW", "statusAula não atualizado"
        assert prog_db.porcentagemConclusao == 20, "porcentagemConclusao não atualizada"

    def test_atualizar_progresso_por_matricula_e_aula(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "m","m","m","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        inserir_progresso(Progresso(0, id_aula, id_mat, "d1","d2","OLD",10))
        # Act
        ok = atualizar_progresso_por_matricula_e_aula(
            id_mat, id_aula,
            {"dataInicio":"d3","dataFim":"d4","statusAula":"NEW","porcentagemConclusao":30}
        )
        lista = obter_progresso_por_matricula(id_mat, 10, 0)
        # Assert
        assert ok is True, "Deveria retornar True na atualização"
        assert any(p.statusAula == "NEW" and p.porcentagemConclusao == 30 for p in lista), \
               "O progresso não foi atualizado corretamente"

    def test_excluir_progresso_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "m","m","m","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        prog_id = inserir_progresso(Progresso(0, id_aula, id_mat, "d","d","OK",0))
        # Act
        ok = excluir_progresso_por_id(prog_id)
        prog_db = obter_progresso_por_id(prog_id)
        # Assert
        assert ok is True, "Deveria retornar True na exclusão"
        assert prog_db is None, "O progresso deveria ter sido excluído"

    def test_excluir_progresso_por_matricula_e_aula(self, test_db):
        # Arrange
        criar_tabela_usuario(); criar_tabela_cliente(); criar_tabela_professor()
        criar_tabela_matricula(); criar_tabela_curso(); criar_tabela_modulo(); criar_tabela_aula()
        criar_tabela_progresso()
        id_user = inserir_usuario(Usuario(0,"U","u@u","u","p","d"))
        id_cli = inserir_cliente(Cliente(0,"","","","","","d",True,[],True), id_user)
        id_prof = inserir_professor(Professor(0,"","","","","","",True,[],True,["x"],1,"d"), id_cli)
        id_mat = inserir_matricula(Matricula(0, id_user, id_prof, "m","m","m","d"))
        id_curso = inserir_curso(Curso(0,"X", id_prof,0.0,"","","","d",True))
        id_mod = inserir_modulo(Modulo(0,id_curso,"M","D",[],[]))
        id_aula = inserir_aula(Aula(0,id_mod,"N","D","h","s",0,"d"))
        inserir_progresso(Progresso(0, id_aula, id_mat, "d","d","OK",0))
        # Act
        ok = excluir_progresso_por_matricula_e_aula(id_mat, id_aula)
        lista = obter_progresso_por_matricula(id_mat, 10, 0)
        # Assert
        assert ok is True, "Deveria retornar True ao excluir por matrícula e aula"
        assert not any(p.idMatricula == id_mat and p.idAula == id_aula for p in lista), \
               "O progresso deveria ter sido excluído para essa matrícula e aula"

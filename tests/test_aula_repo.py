import sys
import os

from data.aula.aula_repo import *
from data.cliente.cliente_repo import *
from data.curso.curso_repo import *
from data.modulo.modulo_repo import *
from data.professor.professor_repo import *
from data.usuario.usuario_repo import *

class TestAulaRepo:
    def test_criar_tabela_aula(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        #Act
        resultado = criar_tabela_aula()
        # Assert
        assert resultado == True, "A criação de tabela deveria retornar True"
    
    def test_inserir_aula(self, test_db):
        criar_tabela_usuario() 
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso_obj = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso_obj)
        modulo_obj = Modulo(0, curso_inserido, "Variáveis", "Muitas variáveis", [], [])
        modulo_inserido = inserir_modulo(modulo_obj)
        # Act
        aula_obj = Aula(0, modulo_inserido, "Aula 1", "Aula 1 é bom", "12:36", "Bom", 0, "12-06-2025")
        aula_inserida = inserir_aula(aula_obj)
        aula_db = obter_aula_por_id(aula_inserida)
        # Asserts
        assert aula_db is not None, "A aula não deveria estar vazia"
        assert aula_db.idModulo == modulo_inserido, "O id do módulo não esta certo"
        assert aula_db.titulo == "Aula 1", "O título da aula não esta certo"
        assert aula_db.descricaoAula == "Aula 1 é bom", "A descrição da aula não esta certa"
        assert aula_db.duracaoAula == "12:36", "A duração da aula não esta certa"
        assert aula_db.tipo == "Bom", "O tipo da aula não esta certo"
        assert aula_db.ordem == 0, "A ordem da aula não esta certa"
        assert aula_db.dataDisponibilidade == "12-06-2025", "A ordem da aula não esta certa"

    def test_obter_todas_aulas(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()
        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        curso = Curso(0, "Python", professor_id, 12.99, "desc", "12:56", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)
        for i in range(10):
            aula = Aula(0, modulo_id, f"Aula {i}", "desc", "10:00", "video", i, "12-06-2025")
            inserir_aula(aula)
        #Act
        aulas = obter_todas_aulas()
        #Assert
        assert len(aulas) == 10, "Deveria haver 3 aulas no banco"

    def test_obter_aula_por_titulo(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        curso = Curso(0, "Python", professor_id, 12.99, "desc", "12:56", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        inserir_aula(Aula(0, modulo_id, "Aula Especial", "desc", "10:00", "video", 0, "12-06-2025"))
        aulas = obter_aula_por_titulo("Especial", 10, 0)
        assert len(aulas) == 1, "Deveria haver 1 aula com título contendo 'Especial'"

    def test_obter_aula_paginada_por_modulo(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        curso = Curso(0, "Python", professor_id, 12.99, "desc", "12:56", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        for i in range(5):
            inserir_aula(Aula(0, modulo_id, f"Aula {i}", "desc", "10:00", "video", i, "12-06-2025"))

        aulas = obter_aula_paginada_por_modulo(modulo_id, 3, 0)
        assert len(aulas) == 3, "Deveria retornar 3 aulas na primeira página"

    def test_obter_quantidade_aulas(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        curso = Curso(0, "Python", professor_id, 12.99, "desc", "12:56", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        for _ in range(4):
            inserir_aula(Aula(0, modulo_id, "Aula", "desc", "10:00", "video", 0, "12-06-2025"))

        qtd = obter_quantidade_aulas()
        assert qtd == 4, "Deveria haver 4 aulas no total"

    def test_obter_quantidade_aulas_por_modulo(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        curso = Curso(0, "Python", professor_id, 12.99, "desc", "12:56", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        for _ in range(2):
            inserir_aula(Aula(0, modulo_id, "Aula", "desc", "10:00", "video", 0, "12-06-2025"))

        qtd = obter_quantidade_aulas_por_modulo(modulo_id)
        assert qtd == 2, "Deveria haver 2 aulas neste módulo"

    def test_atualizar_aula_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        curso = Curso(0, "Python", professor_id, 12.99, "desc", "12:56", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        aula = Aula(0, modulo_id, "Original", "desc", "10:00", "video", 0, "12-06-2025")
        aula_id = inserir_aula(aula)
        aula_atualizada = Aula(aula_id, modulo_id, "Atualizada", "desc nova", "12:00", "pdf", 1, "13-06-2025")
        atualizar_aula_por_id(aula_atualizada)

        aula_db = obter_aula_por_id(aula_id)
        assert aula_db.titulo == "Atualizada", "Título não foi atualizado"
        assert aula_db.duracaoAula == "12:00", "Duração não foi atualizada"

    def test_excluir_aula_por_id(self, test_db):
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        curso = Curso(0, "Python", professor_id, 12.99, "desc", "12:56", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        aula = Aula(0, modulo_id, "Aula para deletar", "desc", "10:00", "video", 0, "12-06-2025")
        aula_id = inserir_aula(aula)
        excluir_aula_por_id(aula_id)
        aula_excluida = obter_aula_por_id(aula_id)
        assert aula_excluida is None, "A aula deveria ter sido excluída"

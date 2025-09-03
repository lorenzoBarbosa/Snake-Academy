import sys
import os

from data.usuario.usuario_repo import *
from data.cliente.cliente_repo import *
from data.professor.professor_repo import *
from data.curso.curso_repo import *
from data.categoria.categoria_repo import *
from data.topico.topico_repo import *
from data.modulo.modulo_repo import *
from data.aula.aula_repo import *

class TestAulaRepo:
    def test_criar_tabela_aula(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        #Act
        resultado = criar_tabela_aula()
        # Assert
        assert resultado == True, "A criação de tabela deveria retornar True"
    
    def test_inserir_aula(self, test_db):
        #Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()
        usuario= Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente= Cliente(0, "", "", "", "" ,"", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor= Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        professor_db = obter_professor_por_id(professor_inserido)
        categoria = Categoria(0, "Categoria de cursos de programação")
        categoria_inserida = inserir_categoria(categoria)
        categoria_db = obter_categoria_por_id(categoria_inserida)
        topico1 = Topico(0, "Python", categoria_db.id)
        topico_inserido = inserir_topico(topico1)
        topico_db = obter_topico_por_id(topico_inserido)
        curso = Curso(0, topico_db.id, f"Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        modulo_obj = Modulo(0, curso_inserido, "ModuloExcluir", "Descrição", [], [])
        modulo_inserido = inserir_modulo(modulo_obj)
        modulo_db = obter_modulo_por_id(modulo_inserido)
        # Act
        aula_obj = Aula(0, modulo_db.id, "Aula 1", "Aula 1 é bom", "12:36", "Bom", 3, "12-06-2025")
        aula_inserida = inserir_aula(aula_obj)
        aula_db = obter_aula_por_id(aula_inserida)
        # Asserts
        assert aula_db is not None, "A aula não deveria estar vazia"
        assert aula_db.idModulo == modulo_inserido, "O id do módulo não esta certo"
        assert aula_db.titulo == "Aula 1", "O título da aula não esta certo"
        assert aula_db.descricaoAula == "Aula 1 é bom", "A descrição da aula não esta certa"
        assert aula_db.duracaoAula == "12:36", "A duração da aula não esta certa"
        assert aula_db.tipo == "Bom", "O tipo da aula não esta certo"
        assert aula_db.ordem == 3, "A ordem da aula não esta certa"
        assert aula_db.dataDisponibilidade == "12-06-2025", "A ordem da aula não esta certa"

    def test_obter_todas_aulas(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        categoria = Categoria(0, "Categoria")
        cat_id = inserir_categoria(categoria)
        topico = Topico(0, "Topico", cat_id)
        topico_id = inserir_topico(topico)
        curso = Curso(0, topico_id, "Curso", professor_id, 20.0, "desc", "10:00", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        for i in range(5):
            aula = Aula(0, modulo_id, f"Aula {i}", "desc", "10:00", "tipo", i, "12-06-2025")
            inserir_aula(aula)

        # Act
        aulas = obter_todas_aulas()

        # Assert
        assert len(aulas) >= 5, "Deveria ter ao menos 5 aulas no banco"

    def test_obter_aula_paginada_por_modulo(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        categoria = Categoria(0, "Categoria")
        cat_id = inserir_categoria(categoria)
        topico = Topico(0, "Topico", cat_id)
        topico_id = inserir_topico(topico)
        curso = Curso(0, topico_id, "Curso", professor_id, 20.0, "desc", "10:00", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        for i in range(10):
            aula = Aula(0, modulo_id, f"Aula {i}", "desc", "10:00", "tipo", i, "12-06-2025")
            inserir_aula(aula)

        # Act
        aulas_pagina = obter_aula_paginada_por_modulo(modulo_id, 3, 0)

        # Assert
        assert len(aulas_pagina) == 3, "Deveriam ser retornadas 3 aulas na primeira página"

    def test_obter_aula_por_titulo(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        categoria = Categoria(0, "Categoria")
        cat_id = inserir_categoria(categoria)
        topico = Topico(0, "Topico", cat_id)
        topico_id = inserir_topico(topico)
        curso = Curso(0, topico_id, "Curso", professor_id, 20.0, "desc", "10:00", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        inserir_aula(Aula(0, modulo_id, "Aula Especial", "desc", "10:00", "tipo", 0, "12-06-2025"))

        # Act
        resultado = obter_aula_por_titulo("Especial", 10, 0)

        # Assert
        assert len(resultado) == 1, "Deveria retornar 1 aula com título contendo 'Especial'"

    def test_obter_quantidade_aulas(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        categoria = Categoria(0, "Categoria")
        cat_id = inserir_categoria(categoria)
        topico = Topico(0, "Topico", cat_id)
        topico_id = inserir_topico(topico)
        curso = Curso(0, topico_id, "Curso", professor_id, 20.0, "desc", "10:00", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        for _ in range(7):
            aula = Aula(0, modulo_id, "Aula", "desc", "10:00", "tipo", 0, "12-06-2025")
            inserir_aula(aula)

        # Act
        quantidade = obter_quantidade_aulas()

        # Assert
        assert quantidade >= 7, "Deveria haver ao menos 7 aulas no banco"

    def test_obter_quantidade_aulas_por_modulo(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        categoria = Categoria(0, "Categoria")
        cat_id = inserir_categoria(categoria)
        topico = Topico(0, "Topico", cat_id)
        topico_id = inserir_topico(topico)
        curso = Curso(0, topico_id, "Curso", professor_id, 20.0, "desc", "10:00", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        for _ in range(3):
            aula = Aula(0, modulo_id, "Aula", "desc", "10:00", "tipo", 0, "12-06-2025")
            inserir_aula(aula)

        # Act
        quantidade = obter_quantidade_aulas_por_modulo(modulo_id)

        # Assert
        assert quantidade == 3, "Deveria haver 3 aulas neste módulo"

    def test_atualizar_aula_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        categoria = Categoria(0, "Categoria")
        cat_id = inserir_categoria(categoria)
        topico = Topico(0, "Topico", cat_id)
        topico_id = inserir_topico(topico)
        curso = Curso(0, topico_id, "Curso", professor_id, 20.0, "desc", "10:00", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        aula = Aula(0, modulo_id, "Aula Original", "Descrição original", "10:00", "video", 1, "12-06-2025")
        aula_id = inserir_aula(aula)

        aula_atualizada = Aula(aula_id, modulo_id, "Aula Atualizada", "Descrição nova", "15:00", "pdf", 2, "15-06-2025")
        atualizar_aula_por_id(aula_atualizada)

        # Act
        aula_db = obter_aula_por_id(aula_id)

        # Assert
        assert aula_db.titulo == "Aula Atualizada", "O título da aula não foi atualizado corretamente"
        assert aula_db.duracaoAula == "15:00", "A duração da aula não foi atualizada corretamente"
        assert aula_db.tipo == "pdf", "O tipo da aula não foi atualizado corretamente"

    def test_excluir_aula_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
        criar_tabela_aula()

        usuario = Usuario(0, "claudio", "claudio@g", "123", "1234", "12-06-2025")
        usuario_id = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_id = inserir_cliente(cliente, usuario_id)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_id = inserir_professor(professor, cliente_id)
        categoria = Categoria(0, "Categoria")
        cat_id = inserir_categoria(categoria)
        topico = Topico(0, "Topico", cat_id)
        topico_id = inserir_topico(topico)
        curso = Curso(0, topico_id, "Curso", professor_id, 20.0, "desc", "10:00", "Bom", "12-06-2025", True)
        curso_id = inserir_curso(curso)
        modulo = Modulo(0, curso_id, "Modulo", "descricao", [], [])
        modulo_id = inserir_modulo(modulo)

        aula = Aula(0, modulo_id, "Aula para excluir", "desc", "10:00", "video", 0, "12-06-2025")
        aula_id = inserir_aula(aula)

        # Act
        excluir_aula_por_id(aula_id)
        aula_db = obter_aula_por_id(aula_id)

        # Assert
        assert aula_db is None, "A aula deveria ter sido excluída do banco"


import sys
import os

from data.professor.professor_repo import *
from data.usuario.usuario_repo import *
from data.cliente.cliente_repo import *
from data.categoria.categoria_repo import *
from data.topico.topico_repo import *
from data.curso.curso_repo import *
from data.modulo.modulo_repo import *


class TestModuloRepo:
    def test_criar_tabela_modulo(self, test_db):
        #Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        # Act
        resultado = criar_tabela_modulo()
        # Assert
        assert resultado == True, "A criação da tabela não foi feita"
    
    def test_inserir_modulo(self, test_db):
         #Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
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
        topico = Topico(0, "Python", categoria_db.id)
        topico_inserido = inserir_topico(topico)
        topico_db = obter_topico_por_id(topico_inserido)
        curso = Curso(0, topico_db.id, f"Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_db = obter_curso_por_id(curso_inserido)
        # Act
        
        modulo_obj = Modulo(0, curso_db.id, "Variáveis", "Muitas variáveis", [], [])
        modulo_inserido = inserir_modulo(modulo_obj)
        modulo_db = obter_modulo_por_id(modulo_inserido)
        # Assert
        assert modulo_db is not None, "O módulo não deveria estar vazio"
        assert modulo_db.idCurso == curso_inserido, "O id do curso está incorreto"
        assert modulo_db.titulo == "Variáveis", "O título do módulo está incorreto"
        assert modulo_db.descricaoModulo == "Muitas variáveis", "O título do módulo está incorreto"
    
    def test_atualizar_modulo(self, test_db):
         #Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
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
        topico = Topico(0, "Python", categoria_db.id)
        topico_inserido = inserir_topico(topico)
        topico_db = obter_topico_por_id(topico_inserido)
        curso = Curso(0, topico_db.id, f"Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_db = obter_curso_por_id(curso_inserido)
        # Act
        modulo_obj = Modulo(0, curso_db.id, "Variáveis", "Muitas variáveis", [], [])
        modulo_inserido = inserir_modulo(modulo_obj)
        modulo_db = obter_modulo_por_id(modulo_inserido)
        
        modulo_db.titulo = "Novo modulo"
        modulo_db.descricaoModulo = "Nova descrição"
        modulo_atualizado = atualizar_modulo_por_id(modulo_db.id, modulo_db)
        # Assert
        assert modulo_atualizado is True, "O módulo não foi atualizado com sucesso"
        modulo_db2 = obter_modulo_por_id(modulo_inserido)
        assert modulo_db2.titulo == "Novo modulo", "O título do módulo está incorreto"
        assert modulo_db2.descricaoModulo == "Nova descrição", "A descrição do módulo está incorreta"

    def test_obter_modulos(self, test_db):
        #Assert
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
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
        topico = Topico(0, "Python", categoria_db.id)
        topico_inserido = inserir_topico(topico)
        topico_db = obter_topico_por_id(topico_inserido)
        curso = Curso(0, topico_db.id, f"Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_db = obter_curso_por_id(curso_inserido)
        
        for m in range(10):
            modulo_obj = Modulo(0, curso_inserido, f"Variáveis{m+1}", "Muitas variáveis", [], [])
            inserir_modulo(modulo_obj)
        # Act
        modulos = obter_todos_modulos()
        # Asserts
        assert len(modulos) == 10, "A quanitdade de módulos deveria ser 10"

    def test_obter_modulos_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
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
        topico = Topico(0, "Python", categoria_db.id)
        topico_inserido = inserir_topico(topico)
        topico_db = obter_topico_por_id(topico_inserido)
        curso = Curso(0, topico_db.id, f"Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_db = obter_curso_por_id(curso_inserido)

        for i in range(10):
            modulo_obj = Modulo(0, curso_inserido, f"Modulo{i+1}", "Descrição", [], [])
            inserir_modulo(modulo_obj)
        
        # Act
        modulos_pg1 = obter_modulos_paginado(1, 4)
        modulos_pg2 = obter_modulos_paginado(2, 4)
        modulos_pg3 = obter_modulos_paginado(3, 4)
        
        # Assert
        assert len(modulos_pg1) == 4, "Deveria retornar 4 módulos na página 1"
        assert len(modulos_pg2) == 4, "Deveria retornar 4 módulos na página 2"
        assert len(modulos_pg3) == 2, "Deveria retornar 2 módulos na página 3 (restantes)"
        assert modulos_pg1[0].titulo == "Modulo1", "O primeiro módulo da página 1 está incorreto"
        assert modulos_pg3[0].titulo == "Modulo9", "O primeiro módulo da página 3 está incorreto"
    
    def test_obter_modulos_por_curso_paginado(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
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
        topico2 = Topico(0, "Python2", categoria_db.id)
        topico_inserido = inserir_topico(topico2)
        topico_db = obter_topico_por_id(topico_inserido)
        
        #Criando dois cursos
        curso1 = Curso(0, topico_db.id, f"Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido1 = inserir_curso(curso1)
        curso_db = obter_curso_por_id(curso_inserido1)

        curso2 = Curso(0, topico_db.id, f"Python2", professor_db.id, 15.99, "não sei", "10:00", "Ótimo", "12-06-2025", True)
        curso_inserido2 = inserir_curso(curso2)
        curso_db2 = obter_curso_por_id(curso_inserido2)

        # módulos para curso 1
        for i in range(5):
            modulo_obj = Modulo(0, curso_inserido1, f"ModuloCurso1-{i+1}", "Descrição", [], [])
            inserir_modulo(modulo_obj)
        # módulos para curso 2
        for i in range(3):
            modulo_obj = Modulo(0, curso_inserido2, f"ModuloCurso2-{i+1}", "Descrição", [], [])
            inserir_modulo(modulo_obj)
        
        # Act
        modulos_curso1_pg1 = obter_modulos_por_curso_paginado(curso_inserido1, 1, 3)
        modulos_curso1_pg2 = obter_modulos_por_curso_paginado(curso_inserido1, 2, 3)
        modulos_curso2_pg1 = obter_modulos_por_curso_paginado(curso_inserido2, 1, 3)

        # Assert
        assert len(modulos_curso1_pg1) == 3, "Curso 1 deveria ter 3 módulos na página 1"
        assert len(modulos_curso1_pg2) == 2, "Curso 1 deveria ter 2 módulos na página 2"
        assert len(modulos_curso2_pg1) == 3, "Curso 2 deveria ter 3 módulos na página 1"
        assert modulos_curso1_pg1[0].titulo == "ModuloCurso1-1", "Título do módulo está incorreto"
        assert modulos_curso2_pg1[2].titulo == "ModuloCurso2-3", "Título do módulo está incorreto"

    def test_obter_quantidade_modulos(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
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
        
        for i in range(7):
            modulo_obj = Modulo(0, curso_inserido, f"Modulo{i+1}", "Descrição", [], [])
            inserir_modulo(modulo_obj)

        # Act
        quantidade = obter_quantidade_modulos()
        # Assert
        assert quantidade == 7, "A quantidade total de módulos deveria ser 7"

    def test_obter_quantidade_modulos_por_curso(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
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
        topico2 = Topico(0, "Python2", categoria_db.id)
        topico_inserido = inserir_topico(topico2)
        topico_db = obter_topico_por_id(topico_inserido)
       
       #Criando dois cursos
        curso1 = Curso(0, topico_db.id, f"Python", professor_db.id, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido1 = inserir_curso(curso1)

        curso2 = Curso(0, topico_db.id, f"Python2", professor_db.id, 15.99, "não sei", "10:00", "Ótimo", "12-06-2025", True)
        curso_inserido2 = inserir_curso(curso2)
        
        # módulos para curso 1
        for i in range(5):
            modulo_obj = Modulo(0, curso_inserido1, f"ModuloCurso1-{i+1}", "Descrição", [], [])
            inserir_modulo(modulo_obj)
        # módulos para curso 2
        for i in range(3):
            modulo_obj = Modulo(0, curso_inserido2, f"ModuloCurso2-{i+1}", "Descrição", [], [])
            inserir_modulo(modulo_obj)

        # Act
        qtd_curso1 = obter_quantidade_modulos_por_curso(curso_inserido1)
        qtd_curso2 = obter_quantidade_modulos_por_curso(curso_inserido2)

        # Assert
        assert qtd_curso1 == 5, "Curso 1 deveria ter 5 módulos"
        assert qtd_curso2 == 3, "Curso 2 deveria ter 3 módulos"

    def test_excluir_modulo_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_professor()
        criar_tabela_categoria()
        criar_tabela_topico()
        criar_tabela_curso()
        criar_tabela_modulo()
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

        # Act
        resultado = excluir_modulo_por_id(modulo_inserido)
        modulo_excluido = obter_modulo_por_id(modulo_inserido)

        # Assert
        assert resultado is True, "Deveria retornar True na exclusão"
        assert modulo_excluido is None, "Módulo deveria ter sido excluído"





        
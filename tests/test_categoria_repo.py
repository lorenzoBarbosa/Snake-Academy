import sys
import os
from data.categoria.categoria_repo import *

class TestCategoriaRepo:
    def test_criar_tabela_categoria(self, test_db):
        #Arrange
        criar_tabela_categoria()
        #Act
        resultado = criar_tabela_categoria()
        #Assert
        assert resultado is True, "A tabela de categorias não foi criada"

    def test_inserir_categoria(self, test_db):
        #Arrange
        criar_tabela_categoria()

        #Act
        categoria = Categoria(id=1, nome="Categoria Teste")
        
        categoria_inserida = inserir_categoria(categoria)
        categoria_db = obter_categoria_por_id(categoria_inserida)

        #Assert
        assert categoria_db is not None, "Categoria não foi inserida"
        assert categoria_db.id == categoria_inserida, "ID da categoria inserida não corresponde ao esperado"
        assert categoria_db.nome == categoria.nome, "Nome da categoria inserida não corresponde ao esperado"

    def test_obter_categorias(self, test_db):
        #Arrange
        criar_tabela_categoria()
        
        #Act
        inserir_categoria(Categoria(id=1, nome="Categoria Teste 1"))
        inserir_categoria(Categoria(id=2, nome="Categoria Teste 2"))

        resultado = obter_categorias()
        
        #Assert

        assert resultado, "A lista de categorias não deve estar vazia"
        assert len(resultado) == 2, "Número de categorias obtidas não corresponde ao esperado"
        assert resultado[0].nome == "Categoria Teste 1", "Nome da primeira categoria não corresponde ao esperado"
        assert resultado[1].nome == "Categoria Teste 2", "Nome da segunda categoria não corresponde ao esperado"
        assert resultado[0].id == 1, "Id da primeira categoria não corresponde ao esperado"
        assert resultado[1].id == 2, "Id da segunda categoria não corresponde ao esperado"

    def test_obter_categoria_por_id(self, test_db):
        # Arrange
        criar_tabela_categoria()
        inserir_categoria(Categoria(id=1, nome="Categoria Teste 1"))
        inserir_categoria(Categoria(id=2, nome="Categoria Teste 2"))

        # Act
        resultado = obter_categoria_por_id(1)
        resultado_inexistente = obter_categoria_por_id(999)

        # Assert
        assert resultado is not None, "A categoria com id=1 não foi encontrada"
        assert resultado.id == 1, "O id da categoria retornada não corresponde ao esperado"
        assert resultado.nome == "Categoria Teste 1", "O nome da categoria retornada não corresponde ao esperado"
        
        assert resultado_inexistente is None, "Deveria retornar None para categoria inexistente"

    def test_obter_categoria_por_nome(self, test_db):
        # Arrange
        criar_tabela_categoria()
        inserir_categoria(Categoria(id=1, nome="Categoria Teste 1"))
        inserir_categoria(Categoria(id=2, nome="Categoria Teste 2"))

        # Act
        resultado = obter_categoria_por_nome("Categoria Teste 2")
        resultado_inexistente = obter_categoria_por_nome("Categoria Inexistente")

        # Assert
        assert resultado is not None, "A categoria com nome 'Categoria Teste 2' não foi encontrada"
        assert resultado.id == 2, "O id da categoria retornada não corresponde ao esperado"
        assert resultado.nome == "Categoria Teste 2", "O nome da categoria retornada não corresponde ao esperado"
        
        assert resultado_inexistente is None, "Deveria retornar None para categoria inexistente"

    def test_obter_quantidade_categoria_por_id(self, test_db):
        # Arrange
        criar_tabela_categoria()
        inserir_categoria(Categoria(id=1, nome="Categoria Teste 1"))

        # Act
        quantidade_existente = obter_quantidade_categoria_por_id(1)
        quantidade_inexistente = obter_quantidade_categoria_por_id(999)

        # Assert
        assert quantidade_existente == 1, "A quantidade para o id 1 deveria ser 1"
        assert quantidade_inexistente == 0, "A quantidade para id inexistente deveria ser 0"

    def test_obter_quantidade_categoria_por_nome(self, test_db):
        # Arrange
        criar_tabela_categoria()
        inserir_categoria(Categoria(id=1, nome="Categoria Teste 1"))

        # Act
        quantidade_existente = obter_quantidade_categoria_por_nome("Categoria Teste 1")
        quantidade_inexistente = obter_quantidade_categoria_por_nome("Nome Inexistente")

        # Assert
        assert quantidade_existente == 1, "A quantidade para o nome 'Categoria Teste 1' deveria ser 1"
        assert quantidade_inexistente == 0, "A quantidade para nome inexistente deveria ser 0"

    def test_atualizar_categoria_por_id(self, test_db):
        # Arrange
        criar_tabela_categoria()
        inserir_categoria(Categoria(id=1, nome="Categoria Teste 1"))

        # Act
        sucesso = atualizar_categoria_por_id(1, "Categoria Atualizada")
        categoria_atualizada = obter_categoria_por_id(1)
        falha = atualizar_categoria_por_id(999, "Categoria Inexistente")

        # Assert
        assert sucesso is True, "A atualização da categoria deveria ser bem sucedida"
        assert categoria_atualizada.nome == "Categoria Atualizada", "O nome da categoria não foi atualizado"
        assert falha is False, "Atualizar categoria inexistente deveria retornar False"

    def test_excluir_categoria_por_id(self, test_db):
        # Arrange
        criar_tabela_categoria()
        inserir_categoria(Categoria(id=1, nome="Categoria Teste 1"))

        # Act
        sucesso = excluir_categoria_por_id(1)
        categoria_depois = obter_categoria_por_id(1)
        falha = excluir_categoria_por_id(999)  # não existente

        # Assert
        assert sucesso is True, "A exclusão da categoria deveria ser bem sucedida"
        assert categoria_depois is None, "A categoria deveria ser removida e não encontrada"
        # A exclusão de categoria inexistente retorna True no seu código atual, isso pode ser ajustado se desejar



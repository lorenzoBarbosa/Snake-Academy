import os
import sys
from data.categoria.categoria_repo import *
from data.topico.topico_repo import *


class TestTopicoRepo:
    def test_criar_tabela_topico(self, test_db):
        #Arrange
        criar_tabela_categoria()

        #Act
        resultado = criar_tabela_topico()

        #Assert
        assert resultado is True, "O resultado deveria criar a tabela topico"
    
    def test_inserir_topico(self, test_db):
        #Arrange
        criar_tabela_categoria()
        criar_tabela_topico()
        
        #Act
        categoria = Categoria(id=1, nome="Desenvolvimento Web")
        inserir_categoria(categoria)
        topico = Topico(id=1, idCategoria=1, nome="HTML")
        inserir_topico(topico)

        #Assert
        assert topico.id is not None, "O ID do tópico inserido não deveria ser None"

    def test_obter_topicos(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        categoria = Categoria(id=1, nome="Dev Web")
        inserir_categoria(categoria)
        for nome in ["HTML", "CSS", "JavaScript"]:
            inserir_topico(Topico(id=0, nome=nome, idCategoria=1))
        topicos = obter_topicos()
        assert len(topicos) == 3, "Deveria retornar 3 tópicos"
        assert topicos[0].nome == "HTML", "Primeiro tópico está incorreto"

    def test_obter_topicos_paginado(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        categoria = Categoria(id=1, nome="Dev Web")
        inserir_categoria(categoria)
        for i in range(10):
            inserir_topico(Topico(id=0, nome=f"Tópico{i+1}", idCategoria=1))
        pagina1 = obter_topicos_paginado(1, 4)
        pagina2 = obter_topicos_paginado(2, 4)
        pagina3 = obter_topicos_paginado(3, 4)
        assert len(pagina1) == 4, "Página 1 deveria ter 4 tópicos"
        assert len(pagina2) == 4, "Página 2 deveria ter 4 tópicos"
        assert len(pagina3) == 2, "Página 3 deveria ter 2 tópicos"
        assert pagina1[0].nome == "Tópico1", "Primeiro tópico da página 1 está incorreto"

    def test_obter_topico_por_id(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        categoria = Categoria(id=1, nome="Dev Web")
        inserir_categoria(categoria)
        inserir_topico(Topico(id=0, nome="HTML", idCategoria=1))
        topicos = obter_topicos()
        id_topico = topicos[0].id
        topico = obter_topico_por_id(id_topico)
        assert topico is not None, "Deveria retornar um tópico"
        assert topico.nome == "HTML", "Nome do tópico está incorreto"

    def test_obter_topicos_por_categoria_paginado(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        inserir_categoria(Categoria(id=1, nome="Categoria1"))
        inserir_categoria(Categoria(id=2, nome="Categoria2"))
        for i in range(5):
            inserir_topico(Topico(id=0, nome=f"Cat1-{i+1}", idCategoria=1))
        for i in range(3):
            inserir_topico(Topico(id=0, nome=f"Cat2-{i+1}", idCategoria=2))
        cat1_pg1 = obter_topico_por_categoria_paginado(1, 1, 3)
        cat1_pg2 = obter_topico_por_categoria_paginado(1, 2, 3)
        cat2_pg1 = obter_topico_por_categoria_paginado(2, 1, 3)
        assert len(cat1_pg1) == 3, "Categoria 1 página 1 deveria ter 3 tópicos"
        assert len(cat1_pg2) == 2, "Categoria 1 página 2 deveria ter 2 tópicos"
        assert len(cat2_pg1) == 3, "Categoria 2 página 1 deveria ter 3 tópicos"
        assert cat1_pg1[0].nome == "Cat1-1", "Nome do primeiro tópico categoria 1 está incorreto"

    def test_obter_topico_por_nome(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        inserir_categoria(Categoria(id=1, nome="Categoria1"))
        inserir_topico(Topico(id=0, nome="Python", idCategoria=1))
        topico = obter_topico_por_nome("Python")
        assert topico is not None, "Deveria encontrar o tópico"
        assert topico.nome == "Python", "Nome do tópico está incorreto"

    def test_obter_quantidade_topicos(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        inserir_categoria(Categoria(id=1, nome="Categoria1"))
        for i in range(5):
            inserir_topico(Topico(id=0, nome=f"Tópico{i+1}", idCategoria=1))
        qtd = obter_quantidade_topicos()
        assert qtd == 5, "Quantidade total de tópicos deveria ser 5"

    def test_obter_quantidade_topicos_por_categoria(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        inserir_categoria(Categoria(id=1, nome="Categoria1"))
        inserir_categoria(Categoria(id=2, nome="Categoria2"))
        for i in range(4):
            inserir_topico(Topico(id=0, nome=f"Cat1-{i+1}", idCategoria=1))
        for i in range(2):
            inserir_topico(Topico(id=0, nome=f"Cat2-{i+1}", idCategoria=2))
        qtd_cat1 = obter_quantidade_topicos_por_categoria(1)
        qtd_cat2 = obter_quantidade_topicos_por_categoria(2)
        assert qtd_cat1 == 4, "Categoria 1 deveria ter 4 tópicos"
        assert qtd_cat2 == 2, "Categoria 2 deveria ter 2 tópicos"

    def test_obter_quantidade_topicos_por_nome(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        inserir_categoria(Categoria(id=1, nome="Categoria1"))
        inserir_topico(Topico(id=0, nome="Python", idCategoria=1))
        qtd = obter_quantidade_topicos_por_nome("Python")
        assert qtd == 1, "Deveria existir 1 tópico com o nome Python"

    def test_obter_quantidade_topicos_por_id(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        inserir_categoria(Categoria(id=1, nome="Categoria1"))
        inserir_topico(Topico(id=0, nome="Python", idCategoria=1))
        topico = obter_topico_por_nome("Python")
        qtd = obter_quantidade_topicos_por_id(topico.id)
        assert qtd == 1, "Deveria existir 1 tópico com o id do tópico"

    def test_atualizar_topico_por_id(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        inserir_categoria(Categoria(id=1, nome="Categoria1"))
        inserir_categoria(Categoria(id=2, nome="Categoria2"))
        inserir_topico(Topico(id=0, nome="Python", idCategoria=1))
        topicos = obter_topicos()
        topico = topicos[0]
        topico.nome = "Python Atualizado"
        topico.idCategoria = 2
        resultado = atualizar_topico_por_id(topico.id, topico.nome, topico.idCategoria)
        assert resultado is True, "Deveria atualizar o tópico"
        topico_atualizado = obter_topico_por_id(topico.id)
        assert topico_atualizado.nome == "Python Atualizado", "Nome não atualizado"
        assert topico_atualizado.idCategoria == 2, "Categoria não atualizada"

    def test_excluir_topico_por_id(self, test_db):
        criar_tabela_categoria()
        criar_tabela_topico()
        inserir_categoria(Categoria(id=1, nome="Categoria1"))
        inserir_topico(Topico(id=0, nome="Para Excluir", idCategoria=1))
        topicos = obter_topicos()
        id_topico = topicos[0].id
        resultado = excluir_topico_por_id(id_topico)
        assert resultado is True, "Deveria retornar True na exclusão"
        topico = obter_topico_por_id(id_topico)
        assert topico is None, "Tópico deveria estar excluído"
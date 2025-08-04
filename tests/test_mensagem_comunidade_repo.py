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
        criar_tabela_comunidade()
        #Act
        resultado = criar_tabela_mensagem_comunidade()

        # Assert
        assert resultado is True, "A tabela não foi criada"

    def test_inserir_mensagem_comunidade(self, test_db):
    # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        criar_tabela_mensagem_comunidade()

        # Act
        usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)

        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)

        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)

        curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)

        curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)

        comunidade = Comunidade(0, curso_obj, "Comunidade", 3, ["João", "Lucas", "Pedro"])
        comunidade_inserida = inserir_comunidade(comunidade)

        matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
        matricula_inserida = inserir_matricula_pegar_id(matricula)

        mensagem_comunidade = MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Pessoas são Legais", "12-04-2025", "11:47", True)
        mensagem_comunidade_inserida = inserir_mensagem_comunidade(mensagem_comunidade)

        mensagem_comunidade_db = obter_mensagem_comunidade_por_id(mensagem_comunidade_inserida)

        # Assert
        assert mensagem_comunidade_db is not None, "Mensagem comunidade não foi inserida no banco de dados"
        assert mensagem_comunidade_db.id is not None, "Mensagem comunidade não recebeu um ID do banco"
        assert mensagem_comunidade_db.idMatricula == mensagem_comunidade.idMatricula, "ID da matrícula não corresponde"
        assert mensagem_comunidade_db.idComunidade == mensagem_comunidade.idComunidade, "ID da comunidade não corresponde"
        assert mensagem_comunidade_db.conteudo == mensagem_comunidade.conteudo, "Conteúdo da mensagem não corresponde"
        assert mensagem_comunidade_db.dataEnvio == mensagem_comunidade.dataEnvio, "Data de envio não corresponde"
        assert mensagem_comunidade_db.horaEnvio == mensagem_comunidade.horaEnvio, "Hora de envio não corresponde"
        assert mensagem_comunidade_db.visualizacao == mensagem_comunidade.visualizacao, "Status de visualização não corresponde"

    def test_obter_mensagens_comunidade(self, test_db):
    # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        criar_tabela_mensagem_comunidade()

        usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)

        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)

        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)

        curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)

        comunidade = Comunidade(0, curso_obj, "Comunidade", 3, ["João", "Lucas", "Pedro"])
        comunidade_inserida = inserir_comunidade(comunidade)

        matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
        matricula_inserida = inserir_matricula_pegar_id(matricula)

        mensagem1 = MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Mensagem 1", "12-04-2025", "11:47", True)
        mensagem2 = MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Mensagem 2", "12-04-2025", "11:48", False)

        inserir_mensagem_comunidade(mensagem1)
        inserir_mensagem_comunidade(mensagem2)

        # Act
        mensagens = obter_mensagens_comunidade()

        # Assert
        assert len(mensagens) >= 2, "Não foram retornadas mensagens suficientes"

        conteudos = [m.conteudo for m in mensagens]
        assert "Mensagem 1" in conteudos
        assert "Mensagem 2" in conteudos

        visualizacoes = {m.conteudo: m.visualizacao for m in mensagens}
        assert visualizacoes["Mensagem 1"] is True
        assert visualizacoes["Mensagem 2"] is False

    def test_obter_mensagem_comunidade_paginado(self, test_db):
    # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        criar_tabela_mensagem_comunidade()

        usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)

        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)

        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)

        curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)

        comunidade = Comunidade(0, curso_obj, "Comunidade", 3, ["João", "Lucas", "Pedro"])
        comunidade_inserida = inserir_comunidade(comunidade)

        matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
        matricula_inserida = inserir_matricula_pegar_id(matricula)

        # Inserir 5 mensagens
        for i in range(1, 6):
            mensagem = MensagemComunidade(
                0,
                matricula_inserida,
                comunidade_inserida,
                f"Mensagem {i}",
                "12-04-2025",
                f"11:4{i}",
                i % 2 == 0
            )
            inserir_mensagem_comunidade(mensagem)

        # Act
        mensagens_pg1 = obter_mensagem_comunidade_paginado(pg_num=1, pg_size=2)
        mensagens_pg2 = obter_mensagem_comunidade_paginado(pg_num=2, pg_size=2)
        mensagens_pg3 = obter_mensagem_comunidade_paginado(pg_num=3, pg_size=2)

        # Assert
        assert len(mensagens_pg1) == 2, "Página 1 deveria conter 2 mensagens"
        assert len(mensagens_pg2) == 2, "Página 2 deveria conter 2 mensagens"
        assert len(mensagens_pg3) == 1, "Página 3 deveria conter 1 mensagem"

        conteudos_pg1 = [m.conteudo for m in mensagens_pg1]
        conteudos_pg2 = [m.conteudo for m in mensagens_pg2]
        conteudos_pg3 = [m.conteudo for m in mensagens_pg3]

        assert conteudos_pg1 == ["Mensagem 1", "Mensagem 2"]
        assert conteudos_pg2 == ["Mensagem 3", "Mensagem 4"]
        assert conteudos_pg3 == ["Mensagem 5"]


    def test_atualizar_mensagem_comunidade(self, test_db):
    # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        criar_tabela_mensagem_comunidade()

        usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)

        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)

        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)

        curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)

        comunidade = Comunidade(0, curso_obj, "Comunidade", 3, ["João", "Lucas", "Pedro"])
        comunidade_inserida = inserir_comunidade(comunidade)

        matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
        matricula_inserida = inserir_matricula_pegar_id(matricula)

        # Inserindo a mensagem original
        mensagem_original = MensagemComunidade(
            0, matricula_inserida, comunidade_inserida,
            "Mensagem Original", "12-04-2025", "11:47", False
        )
        mensagem_id = inserir_mensagem_comunidade(mensagem_original)

        # Act: atualizar a mensagem
        mensagem_atualizada = MensagemComunidade(
            0, matricula_inserida, comunidade_inserida,
            "Mensagem Atualizada", "13-04-2025", "12:00", True
        )
        sucesso = atualizar_mensagem_comunidade(mensagem_atualizada, mensagem_id)

        # Obter do banco
        mensagem_db = obter_mensagem_comunidade_por_id(mensagem_id)

        # Assert
        assert sucesso is True, "A função deveria retornar True após atualização"
        assert mensagem_db.conteudo == "Mensagem Atualizada", "Conteúdo não foi atualizado corretamente"
        assert mensagem_db.dataEnvio == "13-04-2025", "Data de envio não foi atualizada"
        assert mensagem_db.horaEnvio == "12:00", "Hora de envio não foi atualizada"
        assert mensagem_db.visualizacao is True, "Visualização não foi atualizada"

        def test_obter_mensagem_comunidade_por_termo_paginado(self, test_db):
        # Arrange
            criar_tabela_usuario()
            criar_tabela_cliente()
            criar_tabela_matricula()
            criar_tabela_professor()
            criar_tabela_curso()
            criar_tabela_comunidade()
            criar_tabela_mensagem_comunidade()

            usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
            usuario_inserido = inserir_usuario(usuario)
            cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
            cliente_inserido = inserir_cliente(cliente, usuario_inserido)
            professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
            professor_inserido = inserir_professor(professor, cliente_inserido)
            curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
            curso_inserido = inserir_curso(curso)
            curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
            comunidade = Comunidade(0, curso_obj, "Comunidade", 3, ["João", "Lucas", "Pedro"])
            comunidade_inserida = inserir_comunidade(comunidade)
            matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
            matricula_inserida = inserir_matricula_pegar_id(matricula)

            inserir_mensagem_comunidade(MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Legal demais", "12-04-2025", "11:47", True))
            inserir_mensagem_comunidade(MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Muito bom!", "12-04-2025", "11:48", False))

            # Act
            resultados = obter_mensagem_comunidade_por_termo_paginado("Legal", 1, 10)

            # Assert
            assert len(resultados) == 1
            assert resultados[0].conteudo == "Legal demais"

    def test_obter_mensagem_comunidade_por_id(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        criar_tabela_mensagem_comunidade()

        usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        comunidade = Comunidade(0, curso_obj, "Comunidade", 3, ["João", "Lucas", "Pedro"])
        comunidade_inserida = inserir_comunidade(comunidade)
        matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
        matricula_inserida = inserir_matricula_pegar_id(matricula)

        mensagem = MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Conteúdo", "12-04-2025", "11:47", True)
        id_inserido = inserir_mensagem_comunidade(mensagem)

        # Act
        resultado = obter_mensagem_comunidade_por_id(id_inserido)

        # Assert
        assert resultado is not None
        assert resultado.conteudo == "Conteúdo"

    def test_obter_mensagem_comunidade_por_matricula(self, test_db):
        # Arrange (reaproveita a estrutura anterior)
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        criar_tabela_mensagem_comunidade()

        usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        comunidade = Comunidade(0, curso_obj, "Comunidade", 3, ["João", "Lucas", "Pedro"])
        comunidade_inserida = inserir_comunidade(comunidade)
        matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
        matricula_inserida = inserir_matricula_pegar_id(matricula)

        inserir_mensagem_comunidade(MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Mensagem", "12-04-2025", "11:47", True))

        # Act
        resultados = obter_mensagem_comunidade_por_matricula("claudio", 1, 10)

        # Assert
        assert any("Mensagem" in m.conteudo for m in resultados)

    def test_obter_mensagem_comunidade_por_comunidade(self, test_db):
        # Arrange (mesmo padrão)
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        criar_tabela_mensagem_comunidade()

        usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        comunidade = Comunidade(0, curso_obj, "Comunidade Legal", 3, ["João", "Lucas", "Pedro"])
        comunidade_inserida = inserir_comunidade(comunidade)
        matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
        matricula_inserida = inserir_matricula_pegar_id(matricula)

        inserir_mensagem_comunidade(MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Mensagem", "12-04-2025", "11:47", True))

        # Act
        resultados = obter_mensagem_comunidade_por_comunidade("Legal", 1, 10)

        # Assert
        assert any("Mensagem" in m.conteudo for m in resultados)

    def test_excluir_mensagem_comunidade(self, test_db):
        # Arrange
        criar_tabela_usuario()
        criar_tabela_cliente()
        criar_tabela_matricula()
        criar_tabela_professor()
        criar_tabela_curso()
        criar_tabela_comunidade()
        criar_tabela_mensagem_comunidade()

        usuario = Usuario(0, "claudio", "claudio@g.com", "123", "1234", "12-06-2025")
        usuario_inserido = inserir_usuario(usuario)
        cliente = Cliente(0, "", "", "", "", "", "12-06-2025", True, [], True)
        cliente_inserido = inserir_cliente(cliente, usuario_inserido)
        professor = Professor(0, "", "", "", "", "", "", True, [], True, ["python"], 12, "12-06-2025")
        professor_inserido = inserir_professor(professor, cliente_inserido)
        curso = Curso(0, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        curso_inserido = inserir_curso(curso)
        curso_obj = Curso(curso_inserido, "Python", professor_inserido, 12.99, "não sei", "12:56", "Bom", "12-06-2025", True)
        comunidade = Comunidade(0, curso_obj, "Comunidade", 3, ["João", "Lucas", "Pedro"])
        comunidade_inserida = inserir_comunidade(comunidade)
        matricula = Matricula(0, cliente_inserido, curso_inserido, "Bom", "Bom", "Bom", "12-06-2025")
        matricula_inserida = inserir_matricula_pegar_id(matricula)

        mensagem = MensagemComunidade(0, matricula_inserida, comunidade_inserida, "Será excluída", "12-04-2025", "11:47", True)
        id_mensagem = inserir_mensagem_comunidade(mensagem)

        # Act
        excluir_mensagem_comunidade(id_mensagem)
        resultado = obter_mensagem_comunidade_por_id(id_mensagem)

        # Assert
        assert resultado is None, "Mensagem deveria ter sido excluída"

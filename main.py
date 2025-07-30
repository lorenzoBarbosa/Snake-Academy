from fastapi.responses import HTMLResponse
from faker import Faker
import faker_commerce
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tabulate
import uvicorn

from data.admin import admin_repo
from data.aula import aula_repo
from data.chamado import chamado_repo
from data.cliente import cliente_repo
from data.comentario_curso import comentario_curso_repo
from data.comunidade import comunidade_repo
from data.matricula import matricula_repo
from data.mensagem import mensagem_repo
from data.mensagem_comunidade import mensagem_comunidade_repo
from data.modulo import modulo_repo
from data.professor import professor_repo
from data.resposta_chamado import resposta_chamado_repo
from data.usuario import usuario_repo
from data.curso import curso_repo
from data.progresso import progresso_repo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

fake = Faker()
fake.add_provider(faker_commerce.Provider)

resposta= input("Deseja criar as tabelas e inserir os dados:")

if resposta == "sim" or resposta =="s" or resposta == "SIM" or resposta == "S":
    usuario_repo.criar_tabela_usuario()
    cliente_repo.criar_tabela_cliente()
    admin_repo.criar_tabela_admin()
    professor_repo.criar_tabela_professor()
    chamado_repo.criar_tabela_chamado()
    resposta_chamado_repo.criar_tabela_rchamado()
    curso_repo.criar_tabela_curso()
    matricula_repo.criar_tabela_matricula()
    modulo_repo.criar_tabela_modulo()
    aula_repo.criar_tabela_aula()
    progresso_repo.criar_tabela_progresso()
    comentario_curso_repo.criar_tabela_comentario_curso()
    comunidade_repo.criar_tabela_comunidade()
    mensagem_comunidade_repo.criar_tabela_mensagem_comunidade()
    mensagem_repo.criar_tabela_mensagem()

    for _ in range(30):
        usuario_repo.inserir_usuario(
            {
                "nome": fake.name(),
                "email": fake.email(),
                "senha": fake.password(),
                "telefone": fake.phone_number(),
                "dataCriacao": fake.date_time_this_decade()
            }
        )

    for i in range(15):
        cliente_repo.inserir_cliente(
            {
                "dataUltimoAcesso": fake.date_time_this_decade(),
                "statusConta": fake.random_element(elements=(False, True)),
                "historicoCursos": [],
                "indentificacaoProfessor": fake.random_element(elements=(False, True))
            },
            id = i + 1
        )

    for a in range(5):
        admin_repo.inserir_admin({
            "nivelAcesso": fake.random_element(elements=(1, 2, 3, 4, 5))
            },
            id= a + 1
        )

    for p in range(15):
        professor_repo.inserir_professor(
            {
                "cursosPostados": [],
                "quantidadeAlunos": fake.random_int(min=0, max=100),
                "dataCriacaoProfessor": fake.date_time_this_decade()
            },
            id = p + 1
        )

    for _ in range(10):
        chamado_repo.gerar_chamado(
            {
                "idUsuario": fake.random_int(min=1, max=30),
                "descricao": fake.text(max_nb_chars=200),
                "dataEnvio": fake.date_time_this_decade(),
                "horaEnvio": fake.time(),
                "visualizacao": fake.random_element(elements=(False, True))
            }
        )

    for r in range(6):
        resposta_chamado_repo.gerar_rchamado(
            {
                "idAdmin": fake.random_int(min=1, max=5),
                "idChamado": fake.random_int(min=1, max=10),
                "descricao": fake.text(max_nb_chars=200),
                "dataEnvio": fake.date_time_this_decade(),
                "horaEnvio": fake.time(),
                "visualizacao": fake.random_element(elements=(False, True))
            }
        )

    for _ in range(20):
        curso_repo.inserir_curso(
            {
                "nome": fake.ecommerce_name(),
                "idProfessor": fake.random_int(min=1, max=15),
                "custo": fake.random_int(min=100, max=1000),
                "descricaoCurso": fake.text(max_nb_chars=500),
                "duracaoCurso": fake.random_int(min=1, max=12),
                "avaliacao": fake.random_int(min=1, max=5),
                "dataCriacao": fake.date_time_this_decade(),
                "statusCurso": fake.random_element(elements=(False, True))
            }
        )

    for _ in range(15):
        matricula_repo.inserir_matricula(
            {
                "idCliente": fake.random_int(min=1, max=15),
                "idCurso": fake.random_int(min=1, max=20),
                "statusMatricula": fake.random_element(elements=(False, True)),
                "desempenho": fake.random_int(min=0, max=100),
                "frequencia": fake.random_int(min=0, max=100),
                "dataMatricula": fake.date_time_this_decade()
            }
        )

    for _ in range(15):
        modulo_repo.inserir_modulo(
            {
                "idCurso": fake.random_int(min=1, max=15),
                "titulo": fake.text(max_nb_chars=20),
                "descricaoModulo": fake.text(max_nb_chars=200),
                "listaAulas": [],
                "listaExercicios": []
            }
        )

    for _ in range(30):
        aula_repo.inserir_aula(
            {
                "idModulo": fake.random_int(min=1, max=15),
                "titulo": fake.name(),
                "descricaoAula": fake.text(max_nb_chars=200),
                "duracaoAula": fake.time(),
                "tipo": fake.random_element(elements=("video", "texto", "audio")),
                "ordem": fake.random_int(min=1, max=100),
                "dataDisponibilidade": fake.date_time_this_decade()
            }
        )

    for p in range(30):
        statusAula = fake.random_element(elements=("Incompleto", "Completo"))
        if statusAula == "Completo":
            porcentagemConclusao = 100
        else:
            porcentagemConclusao = fake.random_int(min=0, max=99)
        progresso_repo.inserir_progresso(
            {
                "idAula": p + 1,
                "idMatricula": fake.random_int(min=1, max=15),
                "dataInicio": fake.date_time_this_decade(),
                "dataFim": fake.date_time_this_decade(),
                "statusAula": statusAula,
                "porcentagemConclusao": porcentagemConclusao
            }
        )

    for _ in range(30):
        comentario_curso_repo.gerar_comentario_curso(
            {
                "idAdmin": fake.random_int(min=1, max=5),
                "idMatricula": fake.random_int(min=1, max=15),
                "conteudo": fake.text(max_nb_chars=200),
                "dataEnvio": fake.date_time_this_decade(),
                "dataSupervisaoAdmin": fake.date_time_this_decade()
            }
        )

    for _ in range(10):
        comunidade_repo.inserir_comunidade(
            {
                "idCurso": fake.random_int(min=1, max=20),
                "nome": fake.name(),
                "quantidadeParticipantes": fake.random_int(min=1, max=100),
                "listaParticipantes": []
            }
        )

    for _ in range(10):
        mensagem_comunidade_repo.inserir_mensagem_comunidade(
            {
                "idMatricula": fake.random_int(min=1, max=15),
                "idComunidade": fake.random_int(min=1, max=10),
                "conteudo": fake.text(max_nb_chars=200),
                "dataEnvio": fake.date_time_this_decade(),
                "horaEnvio": fake.time()
            }
        )

    for _ in range(30):
        idRemetente = fake.random_int(min=1, max=30)
        idDestinatario = fake.random_int(min=1, max=30)
        while idRemetente == idDestinatario:
            idDestinatario = fake.random_int(min=1, max=30)
        mensagem_repo.inserir_mensagem(
            {
                "idRemetente": idRemetente,
                "idDestinatario": idDestinatario,
                "conteudo": fake.text(max_nb_chars=200),
                "dataEnvio": fake.date_time_this_decade(),
                "horaEnvio": fake.time(),
                "visualizacao": fake.random_element(elements=(False, True))
            }
        )


administradores = admin_repo.obter_todos_admins()
print("-"*200)
print("ADMINS")
for admin in administradores:
    print(f"ID: {admin.id}, Nível de Acesso: {admin.nivelAcesso}")
print("-"*200)
print()

email = "clarkphillip@example.org"
administrador = admin_repo.obter_admin_por_email(email)
print("-"*200)
print(f"ADMIN: {email}")
if administrador:
    for attr, value in vars(administrador).items():
        print(f"{attr}: {value}", end="| ")
else:
    print("Administrador não encontrado.")
print()
print("-"*200)

id = 2
administrador = admin_repo.obter_admin_por_id(id)
print("-"*200)
print(f"ADMIN: {id}")
if administrador:
    for attr, value in vars(administrador).items():
        print(f"{attr}: {value}", end="| ")
else:
    print("Administrador não encontrado.")
print()
print("-"*200)

pg_num = 1
pg_size = 3
administrador_paginado = admin_repo.obter_admin_paginado(pg_num, pg_size)
print("-"*200)
print(f"ADMIN PAGINADO:")
for adminstrador in administrador_paginado:
        for atributo, valor in vars(adminstrador).items():
            print(f"{atributo}: {valor}", end="|")
        print()            
print()
print("-"*200)

pg_num = 1
pg_size = 3
termo = "cla"
adminstrador_termo = admin_repo.obter_admin_por_termo_paginado(termo, pg_num, pg_size)
print("-"*200)
print(f"ADMIN PAGINADO:")
for adminstrador in adminstrador_termo:
        for atributo, valor in vars(adminstrador).items():
            print(f"{atributo}: {valor}", end="|")
        print()            
print()
print("-"*200)





    # Lista de algumas funções comuns da biblioteca Faker
    # faker_funcoes = [
    #     "name()",
    #     "address()",
    #     "email()",
    #     "phone_number()",
    #     "date_time_this_decade()",
    #     "text()",
    #     "random_int()",
    #     "random_element()",
    #     "password()",
    #     "ecommerce_name()"
    # ]

app.get("/")
async def get_root():
    response = HTMLResponse(
        content="<h1>Bem-vindo à Loja Virtual do Snake Academy!</h1>",
        status_code=200
    )
    return response

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
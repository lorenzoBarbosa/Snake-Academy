from faker import Faker
import faker_commerce
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tabulate
import uvicorn

from data.admin import admin_repo
from data.chamado import chamado_repo
from data.cliente import cliente_repo
from data.matricula import matricula_repo
from data.professor import professor_repo
from data.resposta_chamado import resposta_chamado_repo
from data.usuario import usuario_repo
from data.curso import curso_repo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

fake = Faker()
fake.add_provider(faker_commerce.Provider)

usuario_repo.criar_tabela_usuario()
cliente_repo.criar_tabela_cliente()
admin_repo.criar_tabela_admin()
professor_repo.criar_tabela_professor()
chamado_repo.criar_tabela_chamado()
resposta_chamado_repo.criar_tabela_rchamado()
curso_repo.criar_tabela_curso()
matricula_repo.criar_tabela_matricula()

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

from faker import Faker
import faker_commerce
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tabulate
import uvicorn

from data.admin import admin_repo
from data.cliente import cliente_repo
from data.professor import professor_repo
from data.usuario import usuario_repo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

fake = Faker()
fake.add_provider(faker_commerce.Provider)

usuario_repo.criar_tabela_usuario()
cliente_repo.criar_tabela_cliente()
admin_repo.criar_tabela_admin()
professor_repo.criar_tabela_professor()

for _ in range(10):
    usuario_repo.inserir_usuario(usuario={
        "nome": fake.name(),
        "email": fake.email(),
        "senha": fake.password(),
        "telefone": fake.phone_number(),
        "dataCriacao": fake.date()})

for j in range(6):
    cliente_repo.inserir_cliente(cliente={
        "dataUltimoAcesso":fake.date(),
        "statusConta": False,
        "historicoCursos": [],
        "indentificacaoProfessor": False},
        id= j + 1
    )

for a in range(6):
    admin_repo.inserir_admin(admin={
        "nivelAcesso": fake.random_int(min=1, max=5)},
        id= a + 1
    )

for p in range(3):
    professor_repo.inserir_professor(professor={
        "cursosPostados": [],
        "quantidadeAlunos": fake.random_int(min=0, max=100),
        "dataCriacaoProfessor": fake.date()},
        id= p + 1
    )

professores = professor_repo.obter_todos_professors()

titulos = {
    "id:": "ID",
    "nome": "Nome",
    "email": "Email",
    "senha": "Senha",
    "telefone": "Telefone",
    "dataCriacao": "Data de Criação",
    "dataUltimoAcesso": "Data Último Acesso",
    "statusConta": "Status da Conta",
    "historicoCursos": "Histórico de Cursos",
    "indentificacaoProfessor": "Identificação Professor"
}

for professor in professores:
    print("id:", professor.id)
    print("nome:", professor.nome)
    print("email:", professor.email)
    print("senha:", professor.senha)
    print("telefone:", professor.telefone)
    print("dataCriacao:", professor.dataCriacao)
    print("dataUltimoAcesso:", professor.dataUltimoAcesso)
    print("statusConta:", professor.statusConta)
    print("historicoCursos:", professor.historicoCursos)
    print("indentificacaoProfessor:", professor.indentificacaoProfessor)
    print("cursosPostados:", professor.cursosPostados)
    print("quantidadeAlunos:", professor.quantidadeAlunos)
    print("dataCriacaoProfessor:", professor.dataCriacaoProfessor)
    print("-" * 40)
    print()







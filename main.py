from faker import Faker
import faker_commerce
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import tabulate
import uvicorn

from data.admin import admin_repo
from data.cliente import cliente_repo
from data.usuario import usuario_repo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

fake = Faker()
fake.add_provider(faker_commerce.Provider)

usuario_repo.criar_tabela_usuario()
cliente_repo.criar_tabela_cliente()
admin_repo.criar_tabela_admin()

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

clientes= cliente_repo.obter_todos_clientes()
admins = admin_repo.obter_todos_admins()
usuarios = usuario_repo.obter_todos_usuarios()

usuario = usuario_repo.obter_usuario_por_email("")
admin = admin_repo.obter_admin_por_email("")
cliente = cliente_repo.obter_cliente_por_email("")











# titulos = {
#     "id:": "ID",
#     "nome": "Nome",
#     "email": "Email",
#     "senha": "Senha",
#     "telefone": "Telefone",
#     "dataCriacao": "Data de Criação",
#     "dataUltimoAcesso": "Data Último Acesso",
#     "statusConta": "Status da Conta",
#     "historicoCursos": "Histórico de Cursos",
#     "indentificacaoProfessor": "Identificação Professor"
# }








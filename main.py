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

usuario2 = usuario_repo.obter_usuario_por_id(4)
admin2 = admin_repo.obter_admin_por_id(3)
cliente2 = cliente_repo.obter_cliente_por_id(1)

usuarios_paginados = usuario_repo.obter_usuario_paginado(1, 5)
admin_paginado = admin_repo.obter_admin_paginado(1, 5)
cliente_paginado = cliente_repo.obter_cliente_paginado(1, 5)

# usuario_repo.atualizar_usuario_por_email(
#     usuario={
#         "nome": "claudio",
#         "email": "claudio@gmail.com",
#         "senha": "123456",
#         "telefone": "123456789",
#         "dataCriacao": "2023-10-01"
#     }, email="")

# admin_repo.atualizar_admin_por_email(
#     admin={
#         "nivelAcesso": 3
#     }, email="")

# cliente_repo.atualizar_cliente_por_email(
#     cliente={
#         "dataUltimoAcesso": "2023-10-01",
#         "statusConta": True,
#         "historicoCursos": ["Curso 1", "Curso 2"],
#         "indentificacaoProfessor": True
#     }, email="")

cliente_repo.atualizar_cliente_por_id(
    cliente={
        "dataUltimoAcesso": "2023-10-01",
        "statusConta": True,
        "historicoCursos": ["Curso 1", "Curso 2"],
        "indentificacaoProfessor": True
    }, id=1)

admin_repo.atualizar_admin_por_id(
    admin={
        "nivelAcesso": 4
    }, id=1)

qtd_usu = usuario_repo.obter_quantidade_usuario()
qtd_cliente = cliente_repo.obter_quantidade_clientes()
qtd_admin = admin_repo.obter_quantidade_admins()

if usuario_repo.excluir_usuario_por_email("claudio@gmail.com"):
    print("Usuário excluído com sucesso.")

# if admin_repo.excluir_admin_por_email("claudio@gmail.com"):
#     print("Administrador excluído com sucesso.")

# if cliente_repo.excluir_cliente_por_email("claudio@gmail.com"):
#     print("Cliente excluído com sucesso.")

print(usuario2)
print(admin2)
print(cliente2)
print("-"*40)
print(usuarios_paginados)
print(admin_paginado)
print(cliente_paginado)
print("-"*40)








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








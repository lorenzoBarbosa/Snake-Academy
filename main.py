from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from data.admin import admin_repo
from data.cliente import cliente_repo
from data.usuario import usuario_repo

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

usuario_repo.criar_tabela_usuario()
cliente_repo.criar_tabela_cliente()
admin_repo.criar_tabela_admin()

usuario_repo.inserir_usuario(usuario={
    "nome": "João Silva",
    "email": "jhonatanm@gmail.com",
    "senha": "senha123",
    "telefone": "1234567890",
    "dataCriacao": "2023-10-01"})

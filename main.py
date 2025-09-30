import secrets
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from starlette.middleware.sessions import SessionMiddleware

from data.admin import admin_repo
from data.aula import aula_repo
from data.banner import banner_repo
from data.categoria import categoria_repo
from data.chamado import chamado_repo
from data.cliente import cliente_repo
from data.comentario_curso import comentario_curso_repo
from data.comunidade import comunidade_repo
from data.curso import curso_repo
from data.matricula import matricula_repo
from data.mensagem import mensagem_repo
from data.mensagem_comunidade import mensagem_comunidade_repo
from data.modulo import modulo_repo
from data.professor import professor_repo
from data.progresso import progresso_repo
from data.resposta_chamado import resposta_chamado_repo
from data.topico import topico_repo
from data.usuario import usuario_repo
from routes.admin_routes.administrador_routes import router as administrador_router
from routes.admin_routes.alterar_categoria_routes import router as alterar_categoria_router
from routes.admin_routes.alterar_banners_routes import router as alterar_banner_router
from routes.admin_routes.banners_routes import router as banners_router
from routes.admin_routes.cadastrar_routes import router as cadastrar_router
from routes.admin_routes.categorias_routes import router as categorias_router
from routes.admin_routes.comentarios_routes import router as comentarios_router
from routes.admin_routes.confirmar_alteracao_status_admin_routes import router as confirmar_alteracao_status_admin_router
from routes.admin_routes.confirmar_alteracao_status_curso_routes import router as confirmar_alteracao_status_curso_router
from routes.admin_routes.curso_admin_routes import router as curso_admin_router
from routes.admin_routes.denuncias_routes import router as denuncias_router
from routes.admin_routes.detalhes_usuario_routes import router as detalhes_usuario_router
from routes.admin_routes.excluir_categoria_routes import router as excluir_categoria_router
from routes.admin_routes.excluir_routes import router as excluir_router
from routes.admin_routes.inserir_categoria_routes import router as inserir_categoria_router
from routes.admin_routes.moderar_comentario_routes import router as moderar_comentario_router
from routes.admin_routes.moderar_denuncia_routes import router as moderar_denuncia_router
from routes.admin_routes.notificar_usuario_routes import router as notificar_usuario_router
from routes.admin_routes.usuarios_routes import router as usuarios_router

from routes.public_routes.cadastro_routes import router as cadastro_router
from routes.public_routes.home_routes import router as home_router
from routes.public_routes.login_routes import router as login_router
from routes.public_routes.detalhes_curso_routes import router as detalhes_curso_router
from routes.public_routes.confirmacao_cadastro_routes import router as confirmacao_cadastro_router
from routes.public_routes.cursos_routes import router as cursos_router
from routes.public_routes.redefinir_senha_routes import router as restaurar_senha_router
from routes.public_routes.validacao_email_routes import router as validacao_email_router
from routes.public_routes.codigo_enviado_routes import router as codigo_enviado_router

from routes.cliente_routes.cliente_routes import router as cliente_router
from routes.cliente_routes.editar_perfil_routes import router as editar_perfil_router
from routes.cliente_routes.excluir_perfil_routes import router as excluir_perfil_router
from routes.cliente_routes.cursos_matriculados_routes import router as cursos_matriculados_router
from routes.cliente_routes.pagamento_curso_routes import router as pagamento_curso_router
from routes.cliente_routes.tela_pagamento_routes import router as tela_pagamento_router
from routes.cliente_routes.carrinho_routes import router as carrinho_router
from routes.cliente_routes.alterar_senha_routes import router as alterar_senha_router
from routes.cliente_routes.cursos_matriculados.aulas_routes import router as aulas_router
from routes.cliente_routes.cursos_matriculados.detalhes_aula_routes import router as detalhes_aula_router
from routes.cliente_routes.cursos_matriculados.detalhes_curso_routes import router as detalhes_curso_cliente_router
from routes.cliente_routes.cursos_matriculados.modulos_routes import router as modulo_router

from routes.professor_routes.professor_routes import router as professor_router
from routes.professor_routes.comunicacao_routes import router as comunicacao_router
from routes.professor_routes.duvida_routes import router as duvida_router
from routes.professor_routes.cursos.cursos_routes import router as cursos_professor_router
from routes.professor_routes.cursos.detalhes_curso.detalhes_curso_routes import router as detalhes_curso_professor_router
from routes.professor_routes.cursos.detalhes_curso.avaliacoes_routes import router as avaliacoes_router
from routes.professor_routes.cursos.detalhes_curso.duvidas_routes import router as duvidas_router
from routes.professor_routes.cursos.detalhes_curso.detalhes_duvida_routes import router as detalhes_duvida_router
from routes.professor_routes.cursos.detalhes_curso.modificar_curso_routes import router as modificar_curso_router
from routes.professor_routes.cursos.detalhes_curso.modificar_modulo_routes import router as modificar_modulo_router
from routes.professor_routes.cursos.excluir_curso_routes import router as excluir_curso_router
from routes.professor_routes.cursos.criar_curso_routes import router as criar_curso_router
from routes.professor_routes.cursos.criar_modulo_routes import router as criar_modulo_router
from routes.professor_routes.cadastro_professor_routes import router as cadastro_professor_router
from util.criar_admin import criar_admin_padrao

admin_repo.criar_tabela_admin()
aula_repo.criar_tabela_aula()
banner_repo.criar_tabela_banner()
categoria_repo.criar_tabela_categoria()
chamado_repo.criar_tabela_chamado()
cliente_repo.criar_tabela_cliente()
comentario_curso_repo.criar_tabela_comentario_curso()
comunidade_repo.criar_tabela_comunidade()
curso_repo.criar_tabela_curso()
matricula_repo.criar_tabela_matricula()
mensagem_repo.criar_tabela_mensagem()
mensagem_comunidade_repo.criar_tabela_mensagem_comunidade()
modulo_repo.criar_tabela_modulo()
professor_repo.criar_tabela_professor()
progresso_repo.criar_tabela_progresso()
resposta_chamado_repo.criar_tabela_rchamado()
topico_repo.criar_tabela_topico()
usuario_repo.criar_tabela_usuario()


app = FastAPI()

# Gerar chave secreta (em produção, use variável de ambiente!)
SECRET_KEY = secrets.token_urlsafe(32)

# Adicionar middleware de sessão
app.add_middleware(
    SessionMiddleware, 
    secret_key=SECRET_KEY,
    max_age=3600,  # Sessão expira em 1 hora
    same_site="lax",
    https_only=False  # Em produção, mude para True com HTTPS
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(cadastro_router)
app.include_router(home_router)
app.include_router(login_router)
app.include_router(detalhes_curso_router)
app.include_router(confirmacao_cadastro_router)
app.include_router(cursos_router)
app.include_router(restaurar_senha_router)
app.include_router(validacao_email_router)
app.include_router(cliente_router)
app.include_router(editar_perfil_router)
app.include_router(excluir_perfil_router)
app.include_router(cursos_matriculados_router)
app.include_router(pagamento_curso_router)
app.include_router(tela_pagamento_router)
app.include_router(carrinho_router)
app.include_router(alterar_senha_router)
app.include_router(aulas_router)
app.include_router(detalhes_aula_router)
app.include_router(detalhes_curso_cliente_router)
app.include_router(modulo_router)
app.include_router(professor_router)
app.include_router(comunicacao_router)
app.include_router(duvida_router)
app.include_router(cursos_professor_router)
app.include_router(detalhes_curso_professor_router)
app.include_router(avaliacoes_router)
app.include_router(duvidas_router)
app.include_router(detalhes_duvida_router)
app.include_router(modificar_curso_router)
app.include_router(modificar_modulo_router)
app.include_router(excluir_curso_router)
app.include_router(criar_curso_router)
app.include_router(criar_modulo_router)
app.include_router(administrador_router)
app.include_router(alterar_categoria_router)
app.include_router(alterar_banner_router)
app.include_router(banners_router)
app.include_router(cadastrar_router)
app.include_router(categorias_router)
app.include_router(comentarios_router)
app.include_router(confirmar_alteracao_status_admin_router)
app.include_router(confirmar_alteracao_status_curso_router)
app.include_router(curso_admin_router)
app.include_router(denuncias_router)
app.include_router(detalhes_usuario_router)
app.include_router(excluir_categoria_router)
app.include_router(excluir_router)
app.include_router(inserir_categoria_router)
app.include_router(moderar_comentario_router)
app.include_router(moderar_denuncia_router)
app.include_router(notificar_usuario_router)
app.include_router(usuarios_router)
app.include_router(codigo_enviado_router)
app.include_router(cadastro_professor_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
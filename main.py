from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
from routes.public_routes.cadastro_routes import router as cadastro_router
from routes.public_routes.home_routes import router as home_router
from routes.public_routes.login_routes import router as login_router
from routes.public_routes.detalhes_curso_routes import router as detalhes_curso_router
from routes.public_routes.confirmacao_cadastro_routes import router as confirmacao_cadastro_router
from routes.public_routes.cursos_routes import router as cursos_router
from routes.public_routes.recuperar_senha_routes import router as recuperar_senha_router
from routes.public_routes.redefinir_senha_routes import router as restaurar_senha_router
from routes.public_routes.validacao_email_routes import router as validacao_email_router

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


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(cadastro_router)
app.include_router(home_router)
app.include_router(login_router)
app.include_router(detalhes_curso_router)
app.include_router(confirmacao_cadastro_router)
app.include_router(cursos_router)
app.include_router(recuperar_senha_router)
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


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
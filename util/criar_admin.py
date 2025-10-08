from data.admin import admin_repo
from data.admin.admin_model import Admin
from util.security import criar_hash_senha
from data.usuario import usuario_repo
from data.usuario.usuario_model import Usuario

def criar_admin_padrao():
    """Cria um usuário administrador padrão se não existir"""
    
    # Verificar se já existe algum admin
    admins = usuario_repo.obter_usuario_por_perfil("admin")
    
    if not admins:
        # Criar admin padrão
        senha_hash = criar_hash_senha("admin123")
        usuario = Usuario(
            id=0,
            nome="Administrador",
            email="admin@admin.com",
            senha=senha_hash,
            telefone="123456789",
            dataNascimento="2000-01-01",
            perfil="admin",
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None,
            foto=None
        )
        resultado = usuario_repo.inserir_usuario(usuario)
        admin = Admin(
            id=0,
            nome="Administrador",
            email="admin@admin.com",
            senha=senha_hash,
            telefone="123456789",
            dataNascimento="2000-01-01",
            perfil="admin",
            token_redefinicao=None,
            data_token=None,
            data_cadastro=None,
            foto=None,
            nivelAcesso=1
        )
        resultado_admin = admin_repo.inserir_admin(admin, resultado)
        if resultado and resultado_admin:
            print("Admin padrão criado com sucesso!")
            print("E-mail: admin@admin.com")
            print("Senha: admin123")
            print("IMPORTANTE: Altere a senha após o primeiro login!")
            return True
        else:
            print("Falha ao criar o admin padrão.")
            return False
    
    return False

if __name__ == "__main__":
    criar_admin_padrao()
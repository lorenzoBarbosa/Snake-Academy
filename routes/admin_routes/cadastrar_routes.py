import os
from fastapi import APIRouter, File, Request, UploadFile
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

from data.banner import banner_repo
from data.banner.banner_model import Banner
from util.auth_decorator import requer_autenticacao


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/banners/cadastrar")
@requer_autenticacao(["admin"])
async def get_cadastrar(request: Request, usuario_logado: dict = None):
    response = templates.TemplateResponse("admin/banners/cadastrar.html", {"request": request, "usuario": usuario_logado})
    return response

@router.post("/admin/banners/cadastrar")
@requer_autenticacao(["admin"])
async def post_cadastrar(request: Request, usuario_logado: dict = None, foto: UploadFile = File(...), imagem: str = Form(...)):
    banner = Banner(id=0, idAdmin=usuario_logado['id'], status=True, imagem=imagem)
    banner_repo.inserir_banner(banner)
    # 1. Validar tipo de arquivo
    tipos_permitidos = ["image/jpeg", "image/png", "image/jpg", "image/svg+xml"]
    if foto.content_type not in tipos_permitidos:
        banner_repo.deletar_banner(banner.id)
        return templates.TemplateResponse("admin/banners/cadastrar.html",{"request": request, "usuario": usuario_logado, "erro": f"Erro ao cadastrar imagem, tipo incorreto de extensão da imagem. Tente novamente."})

    # 2. Criar diretório se não existir
    upload_dir = "static/uploads/carrossel"
    os.makedirs(upload_dir, exist_ok=True)

    banner = banner_repo.obter_banner_por_imagem(imagem)
    # 3. Gerar nome único para evitar conflitos
    import secrets
    extensao = foto.filename.split(".")[-1]
    nome_arquivo = f"{banner.id}_{secrets.token_hex(8)}.{extensao}"
    caminho_arquivo = os.path.join(upload_dir, nome_arquivo)

    # 4. Salvar arquivo no sistema
    try:
        conteudo = await foto.read()  # ← Lê conteúdo do arquivo
        with open(caminho_arquivo, "wb") as f:
            f.write(conteudo)

        # 5. Salvar caminho no banco de dados
        caminho_relativo = f"/static/uploads/carrossel/{nome_arquivo}"
        banner.imagem = caminho_relativo
        banner_repo.atualizar_banner(banner)

    except Exception as e:
        banner_repo.deletar_banner(banner.id)
        return templates.TemplateResponse("admin/banners/cadastrar.html",{"request": request, "usuario": usuario_logado, "erro": f"Erro ao salvar a foto. Tente novamente. {e}"})

    return templates.TemplateResponse("admin/banners/cadastrar.html",{"request": request, "usuario": usuario_logado, "sucesso": f"Banner cadastrado com sucesso!"})

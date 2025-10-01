import os
from fastapi import APIRouter, File, Request, UploadFile
from fastapi.params import Form
from fastapi.templating import Jinja2Templates

from data.banner import banner_repo
from data.banner.banner_model import Banner
from util.auth_decorator import requer_autenticacao

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/admin/banners/alterar/{banner_id}")
@requer_autenticacao(["admin"])
async def get_alterar(request: Request, usuario_logado: dict = None, banner_id: int = None):
    banner = banner_repo.obter_banner_por_id(banner_id)
    response = templates.TemplateResponse("admin/banners/alterar.html", {"request": request, "usuario": usuario_logado, "banner": banner})
    return response

@router.post("/admin/banners/alterar/{banner_id}")
@requer_autenticacao(["admin"])
async def post_alterar(request: Request, usuario_logado: dict = None, banner_id: int = None, nome: str = Form(...), status: bool = Form(...), foto: UploadFile = File(None)):
     # 1. Validar tipo de arquivo
    tipos_permitidos = ["image/jpeg", "image/png", "image/jpg", "image/svg+xml"]
    banner = banner_repo.obter_banner_por_id(banner_id)
    if foto.content_type not in tipos_permitidos:
        return templates.TemplateResponse("admin/banners/alterar.html",{"request": request, "usuario": usuario_logado, "erro": f"Erro ao cadastrar imagem, tipo incorreto de extensão da imagem. Tente novamente.", "banner": banner})

    # 2. Criar diretório se não existir
    upload_dir = "static/uploads/carrossel"
    os.makedirs(upload_dir, exist_ok=True)

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
        banner_atualizado = Banner(id=banner.id, idAdmin=banner.idAdmin, status=status, imagem=caminho_relativo)
        banner_repo.atualizar_banner(banner_atualizado)

    except Exception as e:
        return templates.TemplateResponse("admin/banners/alterar.html",{"request": request, "usuario": usuario_logado, "erro": f"Erro ao salvar a foto. Tente novamente. {e}", "banner": banner})

    return templates.TemplateResponse("admin/banners/alterar.html",{"request": request, "usuario": usuario_logado, "sucesso": f"Banner alterado com sucesso!", "banner": banner})
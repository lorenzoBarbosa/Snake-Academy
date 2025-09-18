// código

document.addEventListener("DOMContentLoaded", function () {
  function algumaFuncao(){
    console.log("Alguma função");
  }
  
  const senhaInput = document.getElementById("senha_nova");
  const barra = document.getElementById("nivel-forca");
  const texto = document.getElementById("texto-forca");

  if (!senhaInput || !barra || !texto) return;

  senhaInput.addEventListener("input", function () {
    const senha = senhaInput.value;
    let forca = 0;

    if (senha.length >= 8) forca++;
    if (/[A-Z]/.test(senha)) forca++;
    if (/[a-z]/.test(senha)) forca++;
    if (/\d/.test(senha)) forca++;
    if (/[^A-Za-z0-9]/.test(senha)) forca++;

    let cor = "";
    let largura = "";
    let mensagem = "";

    switch (forca) {
      case 0:
      case 1:
      case 2:
        cor = "red";
        largura = "30%";
        mensagem = "Senha fraca";
        break;
      case 3:
      case 4:
        cor = "orange";
        largura = "70%";
        mensagem = "Senha média";
        break;
      case 5:
        cor = "green";
        largura = "100%";
        mensagem = "Senha forte";
        break;
    }

    barra.style.width = largura;
    barra.style.backgroundColor = cor;
    texto.textContent = mensagem;
  });
});


// Preview de foto de perfil
document.addEventListener('DOMContentLoaded', function() {
    const fotoInput = document.getElementById('foto');
    const fotoAtual = document.getElementById('foto-atual');
    const previewContainer = document.getElementById('preview-foto-container');
    const previewFoto = document.getElementById('preview-foto');
    const btnAlterar = document.getElementById('btn-alterar');
    const btnCancelar = document.getElementById('btn-cancelar');

    fotoInput.addEventListener('change', function(e) {
        const file = e.target.files[0];

        if (file) {
            // Verificar se é uma imagem
            if (file.type.startsWith('image/')) {
                const reader = new FileReader();

                reader.onload = function(e) {
                    // Esconder foto atual e mostrar preview
                    fotoAtual.style.display = 'none';
                    previewFoto.src = e.target.result;
                    previewContainer.style.display = 'block';

                    // Habilitar botão e mostrar opções
                    btnAlterar.disabled = false;
                    btnAlterar.innerHTML = '<i class="bi-check"></i> Confirmar Alteração';
                    btnCancelar.style.display = 'inline-block';
                };

                reader.readAsDataURL(file);  // ← Converte arquivo em URL para preview
            } else {
                alert('Por favor, selecione apenas arquivos de imagem.');
                cancelarSelecao();
            }
        } else {
            cancelarSelecao();
        }
    });
});

function cancelarSelecao() {
    const fotoInput = document.getElementById('foto');
    const fotoAtual = document.getElementById('foto-atual');
    const previewContainer = document.getElementById('preview-foto-container');
    const btnAlterar = document.getElementById('btn-alterar');
    const btnCancelar = document.getElementById('btn-cancelar');

    // Limpar seleção e voltar ao estado inicial
    fotoInput.value = '';
    fotoAtual.style.display = 'block';
    previewContainer.style.display = 'none';
    btnAlterar.disabled = true;
    btnAlterar.innerHTML = '<i class="bi-camera"></i> Alterar Foto';
    btnCancelar.style.display = 'none';
}

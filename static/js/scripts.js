//function algumaFuncao(){
//    console.log("Alguma função");
//}
// código

document.addEventListener("DOMContentLoaded", function () {
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

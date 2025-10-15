// TIPOS DE CURSOS / OBJETIVOS APRENDIZADO (só executa se existir na página)
const botoes = document.querySelectorAll('.tipos-cursos, .objetivos-aprendizado');
if (botoes.length > 0) {
    botoes.forEach(botao => {
        botao.addEventListener('click', () => {
            botoes.forEach(b => b.classList.remove('ativo'));
            botao.classList.add('ativo');
        });
    });
}

// CONTROLES DO CARROSSEL (só executa se carrossel existir)
const carrossel = document.querySelector('.carrossel-itens');
const btnEsquerda = document.querySelector('.esquerda');
const btnDireita = document.querySelector('.direita');

if (carrossel && btnEsquerda && btnDireita) {
    btnEsquerda.addEventListener('click', () => {
        carrossel.scrollBy({ left: -220, behavior: 'smooth' });
    });

    btnDireita.addEventListener('click', () => {
        carrossel.scrollBy({ left: 220, behavior: 'smooth' });
    });
}

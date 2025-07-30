const botoes = document.querySelectorAll('.tipos-cursos');

botoes.forEach(botao => {
    botao.addEventListener('click', () => {
        // Remove a classe 'ativo' de todos os botões
        botoes.forEach(b => b.classList.remove('ativo'));

        // Adiciona a classe 'ativo' apenas ao botão clicado
        botao.classList.add('ativo');
    });
});

const carrossel = document.querySelector('.carrossel-itens');
const btnEsquerda = document.querySelector('.esquerda');
const btnDireita = document.querySelector('.direita');

btnEsquerda.addEventListener('click', () => {
    carrossel.scrollBy({ left: -220, behavior: 'smooth' });
});

btnDireita.addEventListener('click', () => {
    carrossel.scrollBy({ left: 220, behavior: 'smooth' });
});
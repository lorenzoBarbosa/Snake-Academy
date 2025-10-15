describe('Cadastro na Snake Academy', () => {
  beforeEach(() => {
    // Ajuste a URL para o endpoint correto da sua aplicação
    cy.visit('/cadastro');
  });

  it('Deve preencher e enviar o formulário de cadastro corretamente', () => {
    // Preenche o campo email
    cy.get('input[name="email"]')
      .type('teste@exemplo.com')
      .should('have.value', 'teste@exemplo.com');
    
    // Preenche o campo nome
    cy.get('input[name="nome"]')
      .type('João da Silva')
      .should('have.value', 'João da Silva');
    
    // Preenche o campo telefone (formato (00) 00000-0000)
    cy.get('input[name="telefone"]')
      .type('(11) 91234-5678')
      .should('have.value', '(11) 91234-5678');
    
    // Preenche a data de nascimento
    cy.get('input[name="data_nascimento"]')
      .type('1990-01-01')
      .should('have.value', '1990-01-01');
    
    // A senha
    cy.get('input[name="senha"]')
      .type('senhaSegura123')
      .should('have.value', 'senhaSegura123');
    
    // Confirmar senha
    cy.get('input[name="confirmar_senha"]')
      .type('senhaSegura123')
      .should('have.value', 'senhaSegura123');
    
    // Submete o formulário
    // Submete o formulário
cy.get('[data-cy="btn-cadastrar"]').should('exist').click();

    // Verifica que não há alertas de erro
    cy.get('.alert-danger').should('not.exist');
    
    // Aqui você pode colocar outras verificações após o envio, como URL ou mensagem de sucesso
    // Exemplo:
    // cy.url().should('include', '/dashboard');
  });
});

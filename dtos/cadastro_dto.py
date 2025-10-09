from datetime import date, datetime
import re
from pydantic import BaseModel, field_validator


class CadastroDTO(BaseModel):
    nome: str 
    email: str
    senha: str 
    confirmar_senha: str 
    telefone: str
    data_nascimento: str

    @field_validator("email")
    @classmethod
    def validar_email(cls, email):
        if not email:
           raise ValueError("O campo email é obrigatório.")
        if '@' not in email or '.' not in email:
           raise ValueError("Eemail inválido.")
        return email

    @field_validator('senha')
    @classmethod
    def validar_senha_forte(cls, senha):
        if not senha:
            raise ValueError('Senha é obrigatória.')
        if len(senha) < 6:
            raise ValueError('Senha deve ter no mínimo 6 caracteres')
        if not any(c.isdigit() for c in senha):
            raise ValueError('Senha deve conter pelo menos um número')
        return senha

    @field_validator('confirmar_senha')
    @classmethod
    def senhas_devem_coincidir(cls, confirmar_senha, values):
        senha = values.data.get('senha')
        if not confirmar_senha:
            raise ValueError('Confirmação de senha é obrigatória.')
        if senha and confirmar_senha != senha:
            raise ValueError('Senhas não coincidem.')
        return confirmar_senha

    @field_validator("nome")
    @classmethod
    def validar_nome(cls, nome):
        if not nome:
            raise ValueError("O campo nome é obrigatório.")
        if len(nome) < 3 or len(nome) > 50:
            raise ValueError("O campo nome deve ter entre 3 e 50 caracteres.")
        if len(nome.split()) < 2:
            raise ValueError('Nome deve ter pelo menos 2 palavras.')
        return nome

    @field_validator("telefone")
    @classmethod
    def validar_telefone(cls, telefone):
        if not telefone:
            raise ValueError("O campo telefone é obrigatório.")
        

        # Verifica se contém apenas números, espaços, parênteses, traços ou '+'
        if re.search(r'[^0-9\s\-\(\)\+]', telefone):
            raise ValueError("Telefone contém caracteres inválidos.")
    
        # Remove tudo que não for número
        numero = re.sub(r'\D', '', telefone)

        if len(numero) not in (10, 11):
            raise ValueError("Número de telefone inválido.")
        return numero

    @field_validator("data_nascimento")
    @classmethod
    def validar_data_nascimento(cls, data_nascimento):
        if data_nascimento is None:
            raise ValueError("Preencha sua data de nascimento.")

        data_nascimento = data_nascimento.strip()

        try:
            data = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Formato inválido. Use DD/MM/AAAA.")
        
        if data > date.today():
            raise ValueError("Data de nascimento não pode ser no futuro.")
        
        # Validar idade máxima (120 anos ou mínima[futuramente])
        idade = (date.today() - data).days // 365
        if idade > 120:
            raise ValueError("Idade inválida. Informe uma data correta.")

        return data
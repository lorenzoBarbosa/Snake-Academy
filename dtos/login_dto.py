from pydantic import BaseModel, field_validator


class LoginDTO (BaseModel):
   email: str
   senha: str

   @field_validator("email")
   @classmethod
   def validar_email(cls, email):
        if not email:
           raise ValueError("O campo email é obrigatório.")
        if '@' not in email or '.' not in email:
           raise ValueError("O campo email deve ser um email válido.")
        return email
   
   @field_validator("senha")
   @classmethod
   def validar_senha(cls, senha):
       if not senha:
           raise ValueError("O campo senha é obrigatório.")
       if len(senha) < 6:
           raise ValueError("O campo senha deve ter pelo menos 6 caracteres.")
       return senha

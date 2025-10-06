import re
from datetime import datetime, date
from decimal import Decimal
from typing import Optional, Any


class ValidacaoError(ValueError):
    pass


def validar_telefone(telefone: str) -> str:
    if not telefone:
        raise ValidacaoError('Telefone é obrigatório')

    # Remover caracteres especiais
    telefone_limpo = re.sub(r'[^0-9]', '', telefone)

    if len(telefone_limpo) < 10 or len(telefone_limpo) > 11:
        raise ValidacaoError('Telefone deve ter 10 ou 11 dígitos')

    # Validar DDD
    ddd = telefone_limpo[:2]
    if not (11 <= int(ddd) <= 99):
        raise ValidacaoError('DDD inválido')

    return telefone_limpo


def validar_data_nascimento(data_str: Optional[str], idade_minima: int = 18) -> Optional[str]:
    if not data_str:
        return None

    # Validar formato ISO (YYYY-MM-DD)
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', data_str):
        raise ValidacaoError('Data deve estar no formato YYYY-MM-DD')

    try:
        data_nasc = datetime.strptime(data_str, '%Y-%m-%d').date()
        hoje = date.today()

        if data_nasc > hoje:
            raise ValidacaoError('Data de nascimento não pode ser futura')

        # Verificar idade mínima
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        if idade < idade_minima:
            raise ValidacaoError(f'Idade mínima é {idade_minima} anos')

        # Verificar se não é uma idade absurda (mais de 120 anos)
        if idade > 120:
            raise ValidacaoError('Data de nascimento muito antiga')

    except ValueError as e:
        if "does not match format" in str(e):
            raise ValidacaoError('Data inválida')
        raise ValidacaoError(str(e))

    return data_str


def validar_nome_pessoa(nome: str, min_chars: int = 2, max_chars: int = 100) -> str:
    if not nome or not nome.strip():
        raise ValidacaoError('Nome é obrigatório')

    # Verificar se contém pelo menos duas palavras
    palavras = nome.split()
    if len(palavras) < 2:
        raise ValidacaoError('Nome deve conter pelo menos nome e sobrenome')

    # Remover espaços extras
    nome_limpo = ' '.join(palavras)

    if len(nome_limpo) < min_chars:
        raise ValidacaoError(f'Nome deve ter pelo menos {min_chars} caracteres')

    if len(nome_limpo) > max_chars:
        raise ValidacaoError(f'Nome deve ter no máximo {max_chars} caracteres')

    # Verificar se contém apenas letras, espaços e acentos
    if not re.match(r'^[a-zA-ZÀ-ÿ\s]+$', nome_limpo):
        raise ValidacaoError('Nome deve conter apenas letras e espaços')

    return nome_limpo


def validar_texto_obrigatorio(texto: str, campo: str, min_chars: int = 1, max_chars: int = 1000) -> str:
    if not texto or not texto.strip():
        raise ValidacaoError(f'{campo} é obrigatório')

    # Remover espaços extras
    texto_limpo = ' '.join(texto.split())

    if len(texto_limpo) < min_chars:
        raise ValidacaoError(f'{campo} deve ter pelo menos {min_chars} caracteres')

    if len(texto_limpo) > max_chars:
        raise ValidacaoError(f'{campo} deve ter no máximo {max_chars} caracteres')

    return texto_limpo


def validar_texto_opcional(texto: Optional[str], max_chars: int = 1000) -> Optional[str]:
    if not texto:
        return None

    # Remover espaços extras
    texto_limpo = ' '.join(texto.split()) if texto.strip() else None

    if texto_limpo and len(texto_limpo) > max_chars:
        raise ValidacaoError(f'Texto deve ter no máximo {max_chars} caracteres')

    return texto_limpo


def validar_valor_monetario(valor: Any, campo: str = "Valor", obrigatorio: bool = True, min_valor: Decimal = Decimal('0')) -> Optional[Decimal]:
    if valor is None:
        if obrigatorio:
            raise ValidacaoError(f'{campo} é obrigatório')
        return None

    try:
        valor_decimal = Decimal(str(valor))
    except:
        raise ValidacaoError(f'{campo} deve ser um número válido')

    if valor_decimal < min_valor:
        if min_valor == 0:
            raise ValidacaoError(f'{campo} não pode ser negativo')
        else:
            raise ValidacaoError(f'{campo} deve ser maior ou igual a {min_valor}')

    # Verificar se tem no máximo 2 casas decimais
    if valor_decimal != round(valor_decimal, 2):
        raise ValidacaoError(f'{campo} deve ter no máximo 2 casas decimais')

    # Verificar se não é um valor absurdamente alto
    if valor_decimal > Decimal('9999999.99'):
        raise ValidacaoError(f'{campo} não pode ser superior a R$ 9.999.999,99')

    return valor_decimal


def validar_numero_inteiro(numero: Any, campo: str = "Número", obrigatorio: bool = True, min_valor: int = 0, max_valor: int = 9999) -> Optional[int]:
    if numero is None:
        if obrigatorio:
            raise ValidacaoError(f'{campo} é obrigatório')
        return None

    try:
        numero_int = int(numero)
    except:
        raise ValidacaoError(f'{campo} deve ser um número inteiro válido')

    if numero_int < min_valor:
        raise ValidacaoError(f'{campo} deve ser maior ou igual a {min_valor}')

    if numero_int > max_valor:
        raise ValidacaoError(f'{campo} deve ser menor ou igual a {max_valor}')

    return numero_int

def validar_senha(senha: Optional[str], min_chars: int = 6, max_chars: int = 128, obrigatorio: bool = True) -> Optional[str]:
    if not senha:
        if obrigatorio:
            raise ValidacaoError('Senha é obrigatória')
        return None

    if len(senha) < min_chars:
        raise ValidacaoError(f'Senha deve ter pelo menos {min_chars} caracteres')

    if len(senha) > max_chars:
        raise ValidacaoError(f'Senha deve ter no máximo {max_chars} caracteres')

    return senha


def validar_senhas_coincidem(senha: str, confirmar_senha: str) -> str:
    if senha != confirmar_senha:
        raise ValidacaoError('As senhas não coincidem')

    return confirmar_senha


def converter_checkbox_para_bool(valor: Any) -> bool:
    if isinstance(valor, bool):
        return valor
    if isinstance(valor, str):
        return valor.lower() in ['on', 'true', '1', 'yes']
    return bool(valor)


def validar_enum_valor(valor: Any, enum_class, campo: str = "Campo") -> Any:
    if isinstance(valor, str):
        try:
            return enum_class(valor.upper())
        except ValueError:
            valores_validos = [item.value for item in enum_class]
            raise ValidacaoError(f'{campo} deve ser uma das opções: {", ".join(valores_validos)}')

    if valor not in enum_class:
        valores_validos = [item.value for item in enum_class]
        raise ValidacaoError(f'{campo} deve ser uma das opções: {", ".join(valores_validos)}')

    return valor


class ValidadorWrapper:
    @staticmethod
    def criar_validador(funcao_validacao, campo_nome: str = None, **kwargs):
        def validador(valor):
            try:
                if campo_nome:
                    return funcao_validacao(valor, campo_nome, **kwargs)
                else:
                    return funcao_validacao(valor, **kwargs)
            except ValidacaoError as e:
                raise ValueError(str(e))
        return validador

    @staticmethod
    def criar_validador_opcional(funcao_validacao, campo_nome: str = None, **kwargs):
        def validador(valor):
            if valor is None or (isinstance(valor, str) and not valor.strip()):
                return None
            try:
                if campo_nome:
                    return funcao_validacao(valor, campo_nome, **kwargs)
                else:
                    return funcao_validacao(valor, **kwargs)
            except ValidacaoError as e:
                raise ValueError(str(e))
        return validador


VALIDADOR_NOME = ValidadorWrapper.criar_validador(validar_nome_pessoa, "Nome")
VALIDADOR_TELEFONE = ValidadorWrapper.criar_validador(validar_telefone, "Telefone")
VALIDADOR_SENHA = ValidadorWrapper.criar_validador(validar_senha, "Senha")
VALIDADOR_EMAIL = ValidadorWrapper.criar_validador_opcional(lambda v, c: v, "Email")
VALIDADOR_DATA_NASCIMENTO = ValidadorWrapper.criar_validador_opcional(validar_data_nascimento, "Data de nascimento", idade_minima=18)
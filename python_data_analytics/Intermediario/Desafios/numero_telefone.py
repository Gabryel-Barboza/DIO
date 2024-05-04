# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


def validate_numero_telefone(phone_number):
    pattern = r"\([0-9]{2}\)[ ][9][0-9]{4}[-][0-9]{4}"
   
    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number):  
      return "Número de telefone válido."
    else:
      return "Número de telefone inválido."
    

# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  
result = validate_numero_telefone(phone_number)


# Imprime o resultado:
print(result)
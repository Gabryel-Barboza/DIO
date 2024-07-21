# Boas práticas Python PEP8
# Leia sobre na documentação python

import os
import sys

frutas = [
    "maçã",
    "pera",
    "laranja",
    "uva",
    "melão",
    "melância",
    "morango",
    "abacate",
    "banana",
    "romã",
    "pêssego",
]


def somar(argumento_1, argumento_2):
    return argumento_1 + argumento_2


def subtrair(num_1, num_2):
    return num_1 - num_2


soma = somar(5, 9)

# Algumas recomendações são 4 espaços para a identação, limitar as linhas a 79 caracteres, usar nomes em snake_case para funções e variáveis e CamelCase para classes.

# Ferramentas de estilo como flake8 para seguir as recomendações
# São chamados de inspecionadores, ou linters
# Formatação manual
"""
pip install flake8
flake8 arquivo.py
"""
# Formatters
# Formatação automática de código com Black
"""
pip install black
black arquivo.py
"""
# Ordenação de imports com Isort
"""
pip install isort
isort arquivo.py
"""
# O VsCode também disponibiliza plugins para retirar a necessidade do terminal
# Podendo ser realizada a formatação apenas salvando o arquivo
# Realize a instalação e configuração disponível na página

# Criando distribuições e subindo para o repositório PyPi
# Para criar distribuições, primeiro mantenha uma hierarquia de projeto convencional
'''
nome_pacote-package ou project
    nome_pacote
        __init__.py   - Arquivos init sinalizam um pacote python, podem estar vazios
        nome_módulo
            __init__.py
            file.py
            file.py
        nome_módulo.py
            __init__.py
            file.py
'''

# Crie na pasta do projeto um README.md e um Requirements.txt (Opcionais)
# Crie um setup.py com a seguinte estrutura: (descontinuado, ver formas modernas de construir dists)
'''
from setuptools import find_packages, setup
from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "README.md", "r") as f: # Ler arquivos criados anteriormente
    description = f.read()


with open(ROOT_PATH / "requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="sqlite2mongo",
    version="0.0.1",
    author="Gabryel_brz",
    author_email="gabryelbuildbarboza@gmail.com",
    description="Package created for learning purposes. Extract from a SQLite database and Insert into MongoDB Cloud",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/Gabryel-Barboza/DIO/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
    )
'''

# Criar distribuições, instale o setuptools e twine
# python setup.py sdist bdist_wheel (2 distribuições para compatibilidade)
# Crie conta em ambos Test PyPi e PyPi para subir as distribuições
# Test PyPi: python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# PyPi: python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


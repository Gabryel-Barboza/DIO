# Pacotes
# São módulos com códigos criados por terceiros
# Existem pacotes builtin no Python, porém é possivel instalar outros com o gerenciador PIP
# O gerenciador PIP instala e remove pacotes, que são encontrados no PyPI (Python Package Index).
# PyPI.org
''' 
pip install pacote
pip uninstall pacote
pip list
'''

# Outro conceito importante é o de Ambientes Virtuais, que permitem isolar os pacotes em um ambiente e não interferir na instalação padrão. Evita conflitos de versão entre projetos
# python3 -m venv myenv : Cria um diretório para ambiente virtual com nome myenv
# myenv/Scripts/activate : Ativa o ambiente virtual no Windows
# source myenv/bin/activate : Ativa o ambiente virtual no Linux
# Deactivate desativa o ambiente virtual

# Consulte a documentação python para ambientes virtuais


# O pip é um gerenciador de pacotes simples, um exemplo disso é quando ocorre a desinstalação de algum módulo e suas dependências precisam ser desinstaladas manualmente.
# Nesses casos, pode-se utilizar gerenciadores de pacotes de terceiros

# Pipenv
''' 
pip install pipenv - instalar o gerenciador de pacote
pipenv install django - utilizando o pipenv para instalar o módulo django
pipenv graph - lista todos os módulos e suas dependências
pipenv lock - cria um arquivo PIP.lock para registrar todos os módulos e dependências, é criado automaticamente por padrão
pipenv uninstall django - desinstala o pacote
pipenv clean - remove todas as dependências não utilizadas
pipenv install - cria um ambiente virtual
'''

# Poetry
# Além do gerenciamento de pacotes, permite o empacotamento e publicação de pacotes no PyPI

'''
pip install poetry - instalar poetry
poetry new myproject - criar um novo projeto com nome myproject
poetry init - inicializar ambiente virtual
poetry install - instalar ambiente virtual
poetry add numpy - instalar numpy
poetry remove numpy - desinstalar numpy
'''


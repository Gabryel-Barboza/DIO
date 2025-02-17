from setuptools import find_packages, setup
from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "README.md", "r") as f:
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


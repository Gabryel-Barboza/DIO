# Criando configuração padrão do flask para cada cenário
import os


# Configura variáveis de ambiente e o caminho do database
class Config:
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.sqlite'
    JWT_SECRET_KEY = 'super-secret'


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SECRET_KEY = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    JWT_SECRET_KEY = 'test'

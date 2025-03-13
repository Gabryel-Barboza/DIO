from pydantic_settings import BaseSettings, SettingsConfigDict


# Recuperando variáveis ambiente com pydantic
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', extra='ignore', env_file_encoding='utf-8'
    )

    database_url: str
    environment: str = 'production'


settings = Settings()

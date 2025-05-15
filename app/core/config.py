from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    news_api_key: str
    news_api_url: str

    model_config = SettingsConfigDict(env_file = ".env")

settings = Settings()

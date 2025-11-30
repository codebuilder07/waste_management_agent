from pydantic import BaseSettings

class Settings(BaseSettings):
    GOOGLE_ADK_API_KEY: str
    GOOGLE_ADK_ENDPOINT: str = "https://api.google.com/adk"
    TIMEOUT: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
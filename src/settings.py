from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./sql_temperature.db"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()

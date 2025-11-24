from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./metrics.db"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Personal Metrics Dashboard"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

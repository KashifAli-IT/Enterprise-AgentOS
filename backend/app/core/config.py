
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "Enterprise AgentOS"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"

    # Local development default; override through AGENTOS_DATABASE_URL.
    database_url: str = (
        "postgresql+psycopg://agentos:agentos_dev_password"
        "@localhost:5432/agentos"
    )

    model_config = SettingsConfigDict(
        env_prefix="AGENTOS_",
        case_sensitive=False,
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance."""
    return Settings()

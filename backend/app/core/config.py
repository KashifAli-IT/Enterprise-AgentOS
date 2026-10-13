from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "Enterprise AgentOS"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_prefix="AGENTOS_",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached settings instance."""
    return Settings()

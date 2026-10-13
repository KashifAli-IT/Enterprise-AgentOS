
from app.core.config import get_settings
from app.db.session import SessionFactory, engine


def test_database_url_uses_postgresql() -> None:
    assert get_settings().database_url.startswith(
        "postgresql+psycopg://"
    )


def test_database_engine_is_async() -> None:
    assert engine.dialect.name == "postgresql"
    assert engine.dialect.is_async is True


def test_session_factory_uses_async_sessions() -> None:
    assert SessionFactory.kw["expire_on_commit"] is False

from collections.abc import Generator

import pytest
from hypothesis import HealthCheck
from hypothesis import settings as hypothesis_settings
from sqlmodel import Session, SQLModel, create_engine, text

from gridify.settings import settings

engine = create_engine(settings.get_test_database_uri())

hypothesis_settings.register_profile(
    "default", suppress_health_check=[HealthCheck.function_scoped_fixture]
)
hypothesis_settings.load_profile("default")


def create_worker_database() -> None:
    general_db_uri = settings.get_test_database_uri("gridify_test")
    general_db_engine = create_engine(general_db_uri)
    db_name = settings.get_test_database_uri().split("/")[-1]
    with general_db_engine.connect() as conn:
        conn.execution_options(isolation_level="AUTOCOMMIT")
        try:
            conn.execute(text(f"CREATE DATABASE {db_name}"))
        except Exception:
            pass


def override_get_db() -> Generator[Session, None, None]:
    with Session(engine) as db:
        yield db


@pytest.fixture(scope="session", autouse=True)
def setup_test_databases() -> Generator[None, None, None]:
    create_worker_database()
    SQLModel.metadata.create_all(bind=engine)
    yield
    SQLModel.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def session() -> Generator[Session, None, None]:
    yield from override_get_db()

import os
from typing import Literal

from pydantic import Field, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    NETWORK_URL: str = "0.0.0.0"
    PORT: int = 5000
    ENVIRONMENT: Literal["local", "production", "test"] = "local"

    # defaults used for testing
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "gridify"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )

    @computed_field  # type: ignore[prop-decorator]
    @property
    def DATABASE_URI(self) -> MultiHostUrl:  # noqa: N802
        return MultiHostUrl.build(
            scheme="postgresql+psycopg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    def get_test_database_uri(self, name: str | None = None) -> str:
        worker_id = os.getenv("PYTEST_XDIST_WORKER", "gw0")
        db_name = name or f"gridify_test_{worker_id}"
        return str(
            MultiHostUrl.build(
                scheme="postgresql+psycopg",
                username="postgres",
                password="gridify-password",
                host="localhost",
                port=5433,
                path=db_name,
            )
        )

    LAST_FM_API_KEY: str = Field(default="")


settings = Settings()  # type: ignore

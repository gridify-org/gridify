from typing import Literal

from pydantic import computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    NETWORK_URL: str = "0.0.0.0"
    PORT: int = 5000
    ENVIRONMENT: Literal["local", "production"] = "local"

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "gridify"
    POSTGRES_PASSWORD: str = "gridify_password"
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


settings = Settings()

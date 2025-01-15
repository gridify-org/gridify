from typing import TypeVar
from uuid import UUID

from sqlmodel import SQLModel

SQLModelT = TypeVar("SQLModelT", bound=SQLModel)

IDType = UUID

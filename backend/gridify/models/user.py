from sqlmodel import Field, SQLModel  # type: ignore

from gridify.typings import IDType
from gridify.utils import id_default_factory


class UserBase(SQLModel):
    username: str
    first_name: str
    last_name: str
    email: str
    password: str


class User(UserBase, table=True):  # type: ignore[call-arg]
    id: IDType = Field(default_factory=id_default_factory, primary_key=True)

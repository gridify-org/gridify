from sqlmodel import Field, SQLModel  # type: ignore

from gridify.typings import IDType
from gridify.utils import id_default_factory


class RatingBase(SQLModel):
    rating: int


class Rating(RatingBase):
    id: IDType = Field(default_factory=id_default_factory, primary_key=True)
    rating: int = Field(default=0, ge=0, le=100)

from sqlmodel import Field  # type: ignore

from gridify.models.rating import Rating, RatingBase


class SongRatingBase(RatingBase):
    title: str
    track_number: int = Field(ge=1)
    duration_seconds: int = Field(ge=0)


class SongRating(SongRatingBase, Rating, table=True): ...

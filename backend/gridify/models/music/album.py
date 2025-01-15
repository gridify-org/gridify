from datetime import date

from gridify.models.rating import Rating, RatingBase


class AlbumRatingBase(RatingBase):
    title: str
    release_date: date


class AlbumRating(AlbumRatingBase, Rating, table=True):  # type: ignore[call-arg]
    ...

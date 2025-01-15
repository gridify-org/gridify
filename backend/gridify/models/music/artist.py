from gridify.models.rating import Rating, RatingBase


class ArtistRatingBase(RatingBase):
    name: str


class ArtistRating(ArtistRatingBase, Rating, table=True):  # type: ignore[call-arg]
    ...

from sqlmodel import Session

from gridify.app import crud
from gridify.models.music import ArtistRating
from gridify.typings import IDType


def create_artist_rating(session: Session, artist: ArtistRating) -> ArtistRating:
    return crud.create(artist, session)


def get_artist_rating(session: Session, artist_id: IDType) -> ArtistRating | None:
    return crud.get(ArtistRating, session, artist_id)


def update_artist_rating(session: Session, artist: ArtistRating) -> ArtistRating:
    return crud.update(artist, session)


def delete_artist_rating(session: Session, artist_id: IDType) -> ArtistRating | None:
    artist = crud.get(ArtistRating, session, artist_id)
    if artist:
        crud.delete(artist, session)
    return artist

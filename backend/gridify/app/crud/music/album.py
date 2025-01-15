from sqlmodel import Session

from gridify.app import crud
from gridify.models.music import AlbumRating
from gridify.typings import IDType


def create_album_rating(session: Session, album: AlbumRating) -> AlbumRating:
    return crud.create(album, session)


def get_album_rating(session: Session, album_id: IDType) -> AlbumRating | None:
    return crud.get(AlbumRating, session, album_id)


def update_album_rating(session: Session, album: AlbumRating) -> AlbumRating:
    return crud.update(album, session)


def delete_album_rating(session: Session, album_id: IDType) -> AlbumRating | None:
    album = session.get(AlbumRating, album_id)
    if album:
        crud.delete(album, session)
    return album

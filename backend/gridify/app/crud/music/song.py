from sqlmodel import Session

from gridify.app import crud
from gridify.models.music import SongRating
from gridify.typings import IDType


def create_song_rating(session: Session, song: SongRating) -> SongRating:
    return crud.create(song, session)


def get_song_rating(session: Session, song_id: IDType) -> SongRating | None:
    return crud.get(SongRating, session, song_id)


def update_song_rating(session: Session, song: SongRating) -> SongRating:
    return crud.update(song, session)


def delete_song_rating(session: Session, song_id: IDType) -> SongRating | None:
    song = crud.get(SongRating, session, song_id)
    if song:
        crud.delete(song, session)
    return song

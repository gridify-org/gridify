from hypothesis import given
from sqlmodel import Session

from gridify.app.crud.music import song as song_crud
from gridify.models.music import SongRating
from gridify.typings import IDType
from tests.strategies import uuid_strategy


def test_create_song(session: Session) -> None:
    test_song = SongRating(
        title="Test Song", track_number=1, duration_seconds=180, rating=5
    )

    created_song = song_crud.create_song_rating(session, test_song)

    assert created_song.id is not None
    assert created_song.title == "Test Song"
    assert created_song.track_number == 1
    assert created_song.duration_seconds == 180
    assert created_song.rating == 5


def test_get_song(session: Session) -> None:
    test_song = SongRating(
        title="Test Song", track_number=1, duration_seconds=180, rating=5
    )
    created_song = song_crud.create_song_rating(session, test_song)

    retrieved_song = song_crud.get_song_rating(session, created_song.id)

    assert retrieved_song is not None
    assert retrieved_song.id == created_song.id
    assert retrieved_song.title == "Test Song"


@given(uuid=uuid_strategy())
def test_get_nonexistent_song(session: Session, uuid: IDType) -> None:
    retrieved_song = song_crud.get_song_rating(session, uuid)

    assert retrieved_song is None


def test_update_song(session: Session) -> None:
    test_song = SongRating(
        title="Test Song", track_number=1, duration_seconds=180, rating=5
    )
    created_song = song_crud.create_song_rating(session, test_song)

    created_song.title = "Updated Song"
    updated_song = song_crud.update_song_rating(session, created_song)

    assert updated_song.id == created_song.id
    assert updated_song.title == "Updated Song"


def test_delete_song(session: Session) -> None:
    test_song = SongRating(
        title="Test Song", track_number=1, duration_seconds=180, rating=5
    )
    created_song = song_crud.create_song_rating(session, test_song)

    deleted_song = song_crud.delete_song_rating(session, created_song.id)
    retrieved_song = song_crud.get_song_rating(session, created_song.id)

    assert deleted_song is not None
    assert deleted_song.id == created_song.id
    assert retrieved_song is None


@given(uuid=uuid_strategy())
def test_delete_nonexistent_song(session: Session, uuid: IDType) -> None:
    deleted_song = song_crud.delete_song_rating(session, uuid)

    assert deleted_song is None

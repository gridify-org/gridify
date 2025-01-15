from uuid import UUID

from hypothesis import given
from sqlmodel import Session

from gridify.app.crud.music import artist as artist_crud
from gridify.models.music import ArtistRating
from gridify.typings import IDType
from tests.strategies import uuid_strategy


def test_create_artist(session: Session) -> None:
    test_artist = ArtistRating(name="Test Artist", rating=5)

    created_artist = artist_crud.create_artist_rating(session, test_artist)

    assert created_artist.id is not None
    assert created_artist.name == "Test Artist"
    assert created_artist.rating == 5


def test_get_artist(session: Session) -> None:
    test_artist = ArtistRating(name="Test Artist", rating=5)
    created_artist = artist_crud.create_artist_rating(session, test_artist)

    retrieved_artist = artist_crud.get_artist_rating(session, created_artist.id)

    assert retrieved_artist is not None
    assert retrieved_artist.id == created_artist.id
    assert retrieved_artist.name == "Test Artist"


@given(uuid=uuid_strategy())
def test_get_nonexistent_artist(session: Session, uuid: IDType) -> None:
    retrieved_artist = artist_crud.get_artist_rating(session, uuid)

    assert retrieved_artist is None


def test_update_artist(session: Session) -> None:
    test_artist = ArtistRating(name="Test Artist", rating=5)
    created_artist = artist_crud.create_artist_rating(session, test_artist)

    created_artist.name = "Updated Artist"
    updated_artist = artist_crud.update_artist_rating(session, created_artist)

    assert updated_artist.id == created_artist.id
    assert updated_artist.name == "Updated Artist"


def test_delete_artist(session: Session) -> None:
    test_artist = ArtistRating(name="Test Artist", rating=5)
    created_artist = artist_crud.create_artist_rating(session, test_artist)

    deleted_artist = artist_crud.delete_artist_rating(session, created_artist.id)
    retrieved_artist = artist_crud.get_artist_rating(session, created_artist.id)

    assert deleted_artist is not None
    assert deleted_artist.id == created_artist.id
    assert retrieved_artist is None


def test_delete_nonexistent_artist(session: Session) -> None:
    deleted_artist = artist_crud.delete_artist_rating(
        session, UUID("00000000-0000-0000-0000-000000000000")
    )

    assert deleted_artist is None

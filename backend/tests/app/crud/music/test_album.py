from datetime import date

from hypothesis import given
from sqlmodel import Session

from gridify.app.crud.music import album as album_crud
from gridify.models.music import AlbumRating
from gridify.typings import IDType
from tests.strategies import uuid_strategy


def test_create_album(session: Session) -> None:
    test_album = AlbumRating(title="Test Album", release_date=date.today(), rating=5)

    created_album = album_crud.create_album_rating(session, test_album)

    assert created_album.id is not None
    assert created_album.title == "Test Album"
    assert created_album.rating == 5


def test_get_album(session: Session) -> None:
    test_album = AlbumRating(title="Test Album", release_date=date.today(), rating=5)
    created_album = album_crud.create_album_rating(session, test_album)

    retrieved_album = album_crud.get_album_rating(session, created_album.id)

    assert retrieved_album is not None
    assert retrieved_album.id == created_album.id
    assert retrieved_album.title == "Test Album"


@given(uuid=uuid_strategy())
def test_get_nonexistent_album(session: Session, uuid: IDType) -> None:
    retrieved_album = album_crud.get_album_rating(session, uuid)

    assert retrieved_album is None


def test_update_album(session: Session) -> None:
    test_album = AlbumRating(title="Test Album", release_date=date.today(), rating=5)
    created_album = album_crud.create_album_rating(session, test_album)

    created_album.title = "Updated Album"
    updated_album = album_crud.update_album_rating(session, created_album)

    assert updated_album.id == created_album.id
    assert updated_album.title == "Updated Album"


def test_delete_album(session: Session) -> None:
    test_album = AlbumRating(title="Test Album", release_date=date.today(), rating=5)
    created_album = album_crud.create_album_rating(session, test_album)

    deleted_album = album_crud.delete_album_rating(session, created_album.id)
    retrieved_album = album_crud.get_album_rating(session, created_album.id)

    assert deleted_album is not None
    assert deleted_album.id == created_album.id
    assert retrieved_album is None


@given(uuid=uuid_strategy())
def test_delete_nonexistent_album(session: Session, uuid: IDType) -> None:
    deleted_album = album_crud.delete_album_rating(session, uuid)

    assert deleted_album is None

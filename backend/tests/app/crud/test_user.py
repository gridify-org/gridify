from hypothesis import given
from sqlmodel import Session

from gridify.app.crud import user as user_crud
from gridify.models.user import User
from gridify.typings import IDType
from tests.strategies import uuid_strategy


def test_create_user(session: Session) -> None:
    test_user = User(
        username="test_user",
        first_name="Test",
        last_name="User",
        email="test@example.com",
        password="password123",
    )

    created_user = user_crud.create_user(session, test_user)

    assert created_user.id is not None
    assert created_user.username == "test_user"
    assert created_user.first_name == "Test"
    assert created_user.last_name == "User"
    assert created_user.email == "test@example.com"
    assert created_user.password == "password123"


def test_get_user(session: Session) -> None:
    test_user = User(
        username="test_user",
        first_name="Test",
        last_name="User",
        email="test@example.com",
        password="password123",
    )
    created_user = user_crud.create_user(session, test_user)

    retrieved_user = user_crud.get_user(session, created_user.id)

    assert retrieved_user is not None
    assert retrieved_user.id == created_user.id
    assert retrieved_user.username == "test_user"
    assert retrieved_user.first_name == "Test"
    assert retrieved_user.last_name == "User"
    assert retrieved_user.email == "test@example.com"
    assert retrieved_user.password == "password123"


@given(uuid=uuid_strategy())
def test_get_nonexistent_user(session: Session, uuid: IDType) -> None:
    retrieved_user = user_crud.get_user(session, uuid)

    assert retrieved_user is None


def test_update_user(session: Session) -> None:
    test_user = User(
        username="test_user",
        first_name="Test",
        last_name="User",
        email="test@example.com",
        password="password123",
    )
    created_user = user_crud.create_user(session, test_user)

    created_user.username = "updated_user"
    created_user.first_name = "Updated"
    updated_user = user_crud.update_user(session, created_user)

    assert updated_user.id == created_user.id
    assert updated_user.username == "updated_user"
    assert updated_user.first_name == "Updated"
    assert updated_user.last_name == "User"
    assert updated_user.email == "test@example.com"
    assert updated_user.password == "password123"


def test_delete_user(session: Session) -> None:
    test_user = User(
        username="test_user",
        first_name="Test",
        last_name="User",
        email="test@example.com",
        password="password123",
    )
    created_user = user_crud.create_user(session, test_user)

    deleted_user = user_crud.delete_user(session, created_user.id)
    retrieved_user = user_crud.get_user(session, created_user.id)

    assert deleted_user is not None
    assert deleted_user.id == created_user.id
    assert retrieved_user is None


@given(uuid=uuid_strategy())
def test_delete_nonexistent_user(session: Session, uuid: IDType) -> None:
    deleted_user = user_crud.delete_user(session, uuid)

    assert deleted_user is None

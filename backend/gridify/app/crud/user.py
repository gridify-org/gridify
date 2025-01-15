from sqlmodel import Session

from gridify.app import crud
from gridify.models.user import User
from gridify.typings import IDType


def create_user(session: Session, user: User) -> User:
    return crud.create(user, session)


def get_user(session: Session, user_id: IDType) -> User | None:
    return crud.get(User, session, user_id)


def update_user(session: Session, user: User) -> User:
    return crud.update(user, session)


def delete_user(session: Session, user_id: IDType) -> User | None:
    user = session.get(User, user_id)
    if user:
        crud.delete(user, session)
    return user

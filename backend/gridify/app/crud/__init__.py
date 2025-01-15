from fastapi import HTTPException
from sqlmodel import Session

from gridify.app.crud.music import album, artist, song
from gridify.typings import IDType, SQLModelT


def commit(model: SQLModelT, session: Session) -> SQLModelT:
    session.add(model)
    session.commit()
    session.refresh(model)
    return model


def get(model: type[SQLModelT], session: Session, id: IDType) -> SQLModelT | None:
    return session.get(model, id)


def create(model: SQLModelT, session: Session) -> SQLModelT:
    return commit(model, session)


def delete(model: SQLModelT, session: Session) -> SQLModelT:
    session.delete(model)
    session.commit()
    return model


def update(model: SQLModelT, session: Session) -> SQLModelT:
    try:
        session.add(model)
        session.commit()
        session.refresh(model)
        return model
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=422, detail="Unprocessable Entity") from e


__all__ = ["album", "artist", "commit", "create", "delete", "get", "song", "update"]

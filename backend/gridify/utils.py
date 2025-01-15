import uuid

from gridify.typings import IDType


def id_default_factory() -> IDType:
    return uuid.uuid4()

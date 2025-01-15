from sqlmodel import create_engine

from gridify.settings import settings

engine = create_engine(str(settings.DATABASE_URI))

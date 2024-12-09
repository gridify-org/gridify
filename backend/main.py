import uvicorn

from gridify.loggings import init_logging
from gridify.settings import settings

if __name__ == "__main__":
    init_logging()

    uvicorn.run("gridify.app:app", host=settings.NETWORK_URL, port=settings.PORT)

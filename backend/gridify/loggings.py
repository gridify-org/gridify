import logging


class FilterAsyncioLogs(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return "asyncio" not in record.name


def init_logging() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="GRIDIFY - %(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()],
    )

    all_loggers = logging.Logger.manager.loggerDict

    for logger_name in all_loggers:
        logger = logging.getLogger(logger_name)
        logger.addFilter(FilterAsyncioLogs())

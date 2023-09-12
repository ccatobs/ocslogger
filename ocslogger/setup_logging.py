import logging

from . import ocs_logfmter as OCSlogfmter

# from .config.config import settings

# if settings.LOG_LEVEL == "INFO":
#     LOG_LEVEL = logging.INFO
# elif settings.LOG_LEVEL == "DEBUG":
#     LOG_LEVEL = logging.DEBUG
# elif settings.LOG_LEVEL == "ERROR":
#     LOG_LEVEL = logging.ERROR
# elif settings.LOG_LEVEL == "WARNING":
#     LOG_LEVEL = logging.WARNING
# else:
#     LOG_LEVEL = logging.INFO

formatter = OCSlogfmter.Logfmter(
    keys=[
        "ts",
        "lvl",
        "logger",
    ],
    mapping={
        "ts": "asctime",
        "lvl": "levelname",
        "logger": "name",
    },
    extra_keys=["ip"],
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

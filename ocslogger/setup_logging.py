import logging

from . import ocs_logfmter as OCSlogfmter

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
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

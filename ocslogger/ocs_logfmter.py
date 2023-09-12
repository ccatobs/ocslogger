import datetime
import logging

import logfmter


class Logfmter(logfmter.Logfmter):
    """
    Custom log formatter class that extends logfmter.Logfmter.
    It provides a specific timestamp format and filters the allowed keys in the extra argument of logging methods.
    """

    """
    Subclass of Logfmt that
    - provides asctime as in 2023-03-16T08:14:01.437019Z
    - allows only defined keys in the extra argument of log methods
    """

    def __init__(self, extra_keys=[], *args, **kwargs) -> None:
        self._extra_keys = extra_keys
        super().__init__(*args, **kwargs)

    def formatTime(self, record, datafmt=None):
        return f"{datetime.datetime.fromtimestamp(record.created).isoformat()}Z"

    def format(self, record: logging.LogRecord) -> str:
        """Validates record for extra keys.
        Calls format method of Logfmter if only valid extra keys are present in record,
        else raises an RuntimeError.
        """
        extras = self.get_extra(record)
        for key in extras.keys():
            if not key in self._extra_keys:
                raise KeyError(f"Invalid extra key {key}")
        return super().format(record)

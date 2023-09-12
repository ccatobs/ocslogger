import logging
import unittest

import ocslogger


class TestOCSLogger(unittest.TestCase):
    def test_logger_output(self):
        # Capture logger output
        import io

        log_output = io.StringIO()
        logging.getLogger().handlers[0].stream = log_output

        logger = logging.getLogger(__name__)
        logger.info("Test message")

        output = log_output.getvalue().strip()
        self.assertIn("Test message", output)

    def test_extra_keys(self):
        # Test if using an allowed extra key does not raise an exception
        try:
            logger = logging.getLogger(__name__)
            logger.info("Test message", extra={"ip": "192.168.1.1"})
        except Exception as e:
            self.fail(f"Logging with extra key raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()

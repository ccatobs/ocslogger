
# `ocslogger`

`ocslogger` provides a standardized logging configuration for Python projects, ensuring consistent and easily parsable log outputs. Built with the logging standards in mind, it utilizes the custom `Logfmter` class to provide a structured logging format.

## Logging Standards

Logging standards are crucial in ensuring that logs are uniform, readable, and easily searchable across applications. Here's what we advocate for with `ocslogger`:

1. **Consistency**: All logs, regardless of where they're generated, should follow the same format.
2. **Structured Logging**: Logs should be machine-readable, making it easy to parse and analyze using tools.
3. **Relevance**: Log messages should be meaningful and provide context. Avoid redundant or verbose logging.
4. **Log Levels**: Properly utilize log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) to categorize log messages. This makes it easier to filter logs based on severity.

## Installation

To install `ocslogger`, navigate to the directory containing the package and run:

```bash
pip install .
```

## Usage

1. **Initialize `ocslogger`**:
    At the start of your main application or entry script, simply import the package:

    ```python
    import ocslogger
    ```

    This will configure the root logger with the custom formatter from `ocslogger`.

2. **Logging in Individual Modules**:
    In your individual modules, you can now use the standard logging approach:

    ```python
    import logging
    logger = logging.getLogger(__name__)
    logger.debug("Your debug message.")
    ```

3. **Log Extras**:
    The custom formatter allows certain keys in the `extra` argument of logging methods. Ensure you follow the allowed keys to avoid runtime errors:

    ```python
    logger.info("User logged in", extra={"ip": "192.168.1.1"})
    ```

4. **Updates**:
    For any updates to the `ocslogger` package, ensure you update the installed package in your projects to benefit from the latest features and bug fixes.

## Logging Best Practices with `ocslogger`

1. **Log Levels**: Use log levels judiciously. For example:
    - **DEBUG**: Detailed information, typically of interest only when diagnosing problems.
    - **INFO**: Confirmation that things are working as expected.
    - **WARNING**: An indication that something unexpected happened, or there might be a problem in the near future (e.g., ‘disk space low’). The software is still working as expected.
    - **ERROR**: The software has not been able to perform some function.
    - **CRITICAL**: A very serious error that may prevent the program from continuing to run.

2. **Structured Logging**: Always prefer structured logging over string formatting. This means instead of:
    ```python
    logger.info(f"User {username} logged in from {ip_address}")
    ```
    Use:
    ```python
    logger.info("User logged in", extra={"username": username, "ip": ip_address})
    ```

3. **Consistent Key Names**: When using the `extra` argument in logging methods, always use consistent key names. This makes log parsing and analysis much easier.

4. **Avoid Logging Sensitive Information**: Always sanitize your logs and ensure no sensitive data like passwords or personal information is being logged.

5. **Log Context**: Where possible, provide additional context with your logs. This can be user IDs, IP addresses, module names, or any other relevant information that can help in debugging or tracing issues.

6. **Handle Exceptions**: Always log exceptions with `logger.exception()`. This ensures the traceback is logged, making debugging easier.

## Running Tests

To ensure the reliability and correctness of `ocslogger`, a suite of tests has been included. To run these tests:

1. Ensure you have the `ocslogger` package installed:
   ```bash
   pip install path_to_ocslogger_directory
   ```

2. Navigate to the `tests` directory inside the `ocslogger` package directory.

3. Use Python's built-in `unittest` module to discover and run tests:
   ```bash
   python -m unittest discover
   ```

This command will discover all test files (i.e., files named `test_*.py`) in the current directory and run them. After running the tests, you should see an output indicating the number of tests run and if any failures or errors occurred.

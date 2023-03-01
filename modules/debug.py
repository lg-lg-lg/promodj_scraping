import logging
from dataclasses import dataclass
from functools import wraps
from time import gmtime, strftime
from typing import Any, Callable, Optional


@dataclass(slots=True)
class __Constants:
    GUI: bool = True       # need for some tests
    IS_DOWNLOAD = True     # download simulation (True = Real)
    PRINTING: bool = True  # console output
    LOGGING: bool = True
    LOG_FILE = "logging.log"

Constants = __Constants()


def log(message: str, error: Optional[Exception] = None, is_exit: bool = False) -> None:
    assert isinstance(message, str)
    assert isinstance(error, Exception | None)
    assert isinstance(is_exit, bool)
    message = message[:1000]
    if Constants.LOGGING:
        tm = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        logging.basicConfig(filename=Constants.LOG_FILE, encoding="utf-8", level=logging.ERROR)
        logging.exception(tm) if error else logging.error(tm + " - " + message)
    if is_exit: exit(message + (" - " + str(error) if error else ""))


def print_message(*args: Any, **kwargs: Any) -> None:
    if Constants.PRINTING: print(*args, **kwargs)


def is_download() -> Any:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
            return await func(*args, **kwargs) if Constants.IS_DOWNLOAD else False
        return wrapped
    return wrapper


def gui_disabler() -> Any:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        async def wrapped(*args: Any, **kwargs: Any) -> Any:
            return await func(*args, **kwargs) if Constants.GUI else False
        return wrapped
    return wrapper

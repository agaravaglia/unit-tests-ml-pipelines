from functools import wraps
from typing import Callable

from src.utilities.logging import Logger


logger = Logger(module="utilities.error")


def error_catch(
    func: Callable,
    **kwargs
) -> Callable:
    """
    Decorator that hanldes the execution of a function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(msg=f"{e}")
            logger.warning(msg=f"Failed during function {func.__name__}")
            return None
    return wrapper

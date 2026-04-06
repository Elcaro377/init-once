import sys
from functools import wraps
from typing import Callable, TypeVar

if sys.version_info >= (3, 10):
    from typing import ParamSpec

else:
    from typing_extensions import ParamSpec

InitParams = ParamSpec('InitParams')
InitRet = TypeVar('InitRet')

def init_once(
    initializer: Callable[InitParams, InitRet], 
    *init_args: InitParams.args, 
    **init_kwds: InitParams.kwargs
):
    """Runs `initializer` once before a function is called

    :param initializer: The initialization function that needs to be executed once
    :param init_args: Positional arguments to pass to `initializer`
    :param init_kwds: Keyword arguments to pass to `initializer`
    
    :return: Decorated function

    Examples
    --------
    >>> def init_func(msg: str):
    ...     print(f"Initializing msg: {msg}")
    ... 
    ... @init_once(init_func, "hello")
    ... def main_task(data: str):
    ...     print(f"Processing: {data}")
    ... 
    ... # First call: init_func executes first, then main_task
    ... main_task("first")
    ... # Output:
    ... # Initializing msg: hello
    ... # Processing: first
    ... 
    ... # Subsequent calls: only main_task executes
    ... main_task("second")
    ... # Output:
    ... # Processing: second

    .. note::
        This decorator is only for simple initialization (return ignored).

    .. warning::
        Async and thread-safe are not supported yet
        
    """
    P = ParamSpec('P')
    R = TypeVar('R')

    def decorator(func: Callable[P, R]):
        def first_call(*args: P.args, **kwds: P.kwargs):
            nonlocal curr_func
            initializer(*init_args, **init_kwds)
            curr_func = func
            return func(*args, **kwds)

        curr_func = first_call

        @wraps(func)
        def wrapper(*args: P.args, **kwds: P.kwargs):
            return curr_func(*args, **kwds)
        
        return wrapper
    return decorator

__all__ = ['init_once']
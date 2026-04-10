import threading
from collections.abc import Callable
from functools import wraps


def init_once[**InitParams, InitRet](
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
        Async is not supported yet
        
    """

    def decorator[**P, R](func: Callable[P, R]):
        lock = threading.Lock()

        def initialization():
            nonlocal curr_func
            if curr_func is func: return
            initializer(*init_args, **init_kwds)
            curr_func = func

        def first_call(*args: P.args, **kwds: P.kwargs):
            with lock: initialization()
            return func(*args, **kwds)

        curr_func = first_call

        @wraps(func)
        def wrapper(*args: P.args, **kwds: P.kwargs):
            return curr_func(*args, **kwds)
        
        return wrapper
    return decorator

__all__ = ['init_once']
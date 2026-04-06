from collections.abc import Callable
from functools import wraps


def init_once[**InitParams, InitRet](
    initializer: Callable[InitParams, InitRet], 
    *init_args: InitParams.args, 
    **init_kwds: InitParams.kwargs
):
    def decorator[**P, R](func: Callable[P, R]):
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
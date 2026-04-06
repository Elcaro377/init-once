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
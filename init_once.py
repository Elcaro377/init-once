def init_once(initializer, *init_args, **init_kwds):
    def decorator(func):
        def first_call(*args, **kwds):
            nonlocal curr_func
            initializer(*init_args, **init_kwds)
            curr_func = func
            return func(*args, **kwds)

        curr_func = first_call

        def wrapper(*args, **kwds):
            return curr_func(*args, **kwds)
        
        return wrapper
    return decorator
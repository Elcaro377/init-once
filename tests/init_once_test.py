from init_once import init_once

init_count = 0

def init_func(i: int):
    global init_count
    init_count += i

@init_once(init_func, 1)
def func(s: str):
    """func doc"""
    return s

def test_init_once():
    assert func.__doc__ == """func doc"""   # test functools.wraps
    assert func('x') == 'x'
    assert init_count == 1
    assert func('x') == 'x'
    assert init_count == 1
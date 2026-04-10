from unittest.mock import Mock

from init_once import init_once

init_count = 0
mock_init = Mock()

@init_once(mock_init)
def func(s: str):
    """func doc"""
    return s

def test_basic_function():
    assert func.__doc__ == """func doc"""   # test functools.wraps
    assert func('x') == 'x'
    assert func('x') == 'x'
    assert func('x') == 'x'
    assert mock_init.call_count == 1
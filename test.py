from init_once import init_once

def init_func(s: str):
    print(f'init: {s}')

@init_once(init_func, 'a')
def func(s: str):
    """func doc"""
    print(f'func: {s}')
    return 1, 2, 3

print(func.__doc__)
print(func('b')[0])
print(func('c')[1])
print(func('d')[2])
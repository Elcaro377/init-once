from init_once import init_once

def init_func(s: str):
    print(f'init: {s}')

@init_once(init_func, 'a')
def func(s: str):
    print(f'func: {s}')

func('b')
func('c')
func('d')
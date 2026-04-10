import threading
from time import sleep
from unittest.mock import Mock

from init_once import init_once

cnt = 0
mock_init = Mock()

def init_func():
    global cnt
    mock_init()
    for _ in range(100):
        sleep(0.01)
        cnt += 1

@init_once(init_func)
def func():
    ...

def test_thread_safe():
    threads = [threading.Thread(target=func) for _ in range(200)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    assert cnt == 100
    assert mock_init.call_count == 1

English | [简体中文](README.zh-CN.md)

# init_once

## Introduction

`init_once` is a thread-safe decorator that **runs an initialization function once right before the decorated function is called for the first time**. The initialization runs only once. **No outer flag needed**.

## Dependencies and Version Requirements

- Python 3.8 or higher

## Usage

### Basic Syntax

```python
@init_once(initializer, *init_args, **init_kwds)
def func(...):
    ...
```

- `initializer`: The initialization function that needs to be executed once.
- `*init_args`: Positional arguments to pass to `initializer`.
- `**init_kwds`: Keyword arguments to pass to `initializer`.

### Simple Example

```python
from init_once import init_once

# Initialization function: runs only once
def init_func(msg: str):
    print(f"Initializing msg: {msg}")

@init_once(init_func, "hello")
def main_task(data: str):
    print(f"Processing: {data}")

# First call: init_func executes first, then main_task
main_task("first")
# Output:
# Initializing msg: hello
# Processing: first

# Subsequent calls: only main_task executes
main_task("second")
# Output:
# Processing: second

# The above is equivalent to:
initialized = False

def init_func(msg: str):
    print(f"Initializing msg: {msg}")

def main_task(data: str):
    global initialized
    if not initialized:
        init_func("hello")
        initialized = True

    print(f"Processing: {data}")

main_task("first")
main_task("second")
```

## Notes
1. This decorator is only for simple initialization (return ignored). If you need the return value, you should handle the initialization explicitly instead of using this decorator.
2. Async version is to be implemented in the future.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

If you have any questions or suggestions for improvement, feel free to open an Issue or submit a Pull Request.

[English](README.md) | 简体中文

# init_once

## 简介

`init_once` 是一个装饰器，用于**在被装饰函数第一次被调用时运行前执行一次初始化函数**，初始化仅执行一次，**无需手动维护外层标志位**。


## 依赖与版本要求

- Python 3.8 或更高版本

## 使用方法

### 基本语法

```python
@init_once(initializer, *init_args, **init_kwds)
def func(...):
    ...
```

- `initializer`：需要执行一次的初始化函数。
- `*init_args`：传递给 `initializer` 的位置参数。
- `**init_kwds`：传递给 `initializer` 的关键字参数。

### 简单示例

```python
from init_once import init_once

# 初始化函数：只执行一次
def init_func(msg: str):
    print(f"Initializing msg: {msg}")

@init_once(init_func, "hello")
def main_task(data: str):
    print(f"Processing: {data}")

# 第一次调用：先执行 init_func，再执行 main_task
main_task("first")
# 输出：
# Initializing msg: hello
# Processing: first

# 第二次及后续调用：只执行 main_task
main_task("second")
# 输出：
# Processing: second

# 以上代码等效于：
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

## 注意事项
1. **适用建议**：此装饰器仅用于简单初始化（返回值被忽略）。若需获取返回值则应显式处理初始化逻辑而不是使用此装饰器。
2. **异步与线程**：异步与线程安全版本待后续实现。


## 许可

本项目采用 MIT 许可证。详情参见 [LICENSE](LICENSE) 文件。

---

如有问题或改进建议，欢迎提出 Issue 或 Pull Request。
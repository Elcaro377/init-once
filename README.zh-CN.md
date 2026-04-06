[English](README.md) | 简体中文

# init_once

## 简介

`init_once` 是一个装饰器，用于确保初始化函数**仅在被装饰函数第一次调用前执行一次**。后续调用被装饰函数时，初始化逻辑不会重复执行。


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
```

## 注意事项
1. **适用建议**：该装饰器仅适用于简单的初始化过程，其返回值将被忽略，若有获取的需求则说明此时不应使用此装饰器进行隐式初始化。
2. **异步与线程**：异步与线程安全版本待后续实现。


## 许可

本项目采用 MIT 许可证。详情参见 [LICENSE](LICENSE) 文件。

---

如有问题或改进建议，欢迎提出 Issue 或 Pull Request。
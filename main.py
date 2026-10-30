"""Python 项目入口文件（Visual Studio 启动项）。

在 Visual Studio 中按 F5 即可运行，断点可直接下在下面任意一行。
"""

import sys


def greet(name: str) -> str:
    """返回一句问候语，用于演示单步调试。"""
    message = f"你好，{name}！"
    return message


def main() -> int:
    print(greet("Python"))
    print(f"解释器版本: {sys.version.split()[0]}")
    print(f"解释器路径: {sys.executable}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

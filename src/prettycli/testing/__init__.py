"""
prettycli.testing - 交互式测试框架

用于测试交互式 CLI 应用程序。

Example:
    >>> from prettycli.testing import test, mock_prompt, TestRunner, ShellSession
    >>>
    >>> @test("should greet user")
    ... def test_greet():
    ...     with mock_prompt(["Alice"]):
    ...         result = greet_user()
    ...         assert "Alice" in result
    >>>
    >>> # 持久化 Shell 会话
    >>> with ShellSession() as sh:
    ...     sh.run("cd /tmp")
    ...     sh.run("pwd")  # 输出 /tmp
    >>>
    >>> runner = TestRunner()
    >>> runner.discover(Path("tests/"))
    >>> runner.run(interactive=True)
"""
from prettycli.testing.session import *
from prettycli.testing.assertions import *
from prettycli.testing.mock import *
from prettycli.testing.runner import *
from prettycli.testing.shell import *

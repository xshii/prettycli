"""底部固定工具栏：每日一句"""
from pathlib import Path

from prompt_toolkit.formatted_text import HTML

__all__ = ["BottomToolbar"]

# quotes.txt 在 prettycli 根目录
QUOTES_FILE = Path(__file__).parent.parent.parent / "quotes.txt"


class BottomToolbar:
    """底部固定工具栏

    用于在终端底部显示每日一句或提示信息。

    Example:
        >>> toolbar = BottomToolbar()
        >>> session = PromptSession(bottom_toolbar=toolbar)
    """

    def __init__(self, quotes_file: Path = None):
        self._quotes_file = quotes_file or QUOTES_FILE
        self._index = 0
        self._quotes = self._load_quotes()

    def _load_quotes(self) -> list:
        """加载 quotes 文件"""
        if self._quotes_file.exists():
            return [
                line.strip()
                for line in self._quotes_file.read_text().splitlines()
                if line.strip()
            ]
        return ["Keep coding!"]

    def next_quote(self) -> str:
        """获取下一条 quote"""
        quote = self._quotes[self._index % len(self._quotes)]
        self._index += 1
        return quote

    def current_quote(self) -> str:
        """获取当前 quote（不切换）"""
        return self._quotes[self._index % len(self._quotes)]

    def render(self) -> HTML:
        """渲染工具栏内容"""
        quote = self.current_quote()
        return HTML(f"<i>{quote}</i>")

    def __call__(self):
        """prompt_toolkit toolbar 回调"""
        return self.render()

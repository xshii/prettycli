# PrettyCLI

A beautiful CLI framework for Python with VS Code integration.

## Quick Start

### 1. Setup Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate
```

### 2. Install Package

```bash
# Basic installation
pip install -e .

# With VS Code support
pip install -e ".[vscode]"

# With development tools
pip install -e ".[dev]"
```

### 3. Create Your First CLI

```python
# app.py
from prettycli import App, BaseCommand, Context

class HelloCommand(BaseCommand):
    name = "hello"
    description = "Say hello"

    def execute(self, ctx: Context, name: str = "World"):
        ctx.print(f"Hello, {name}!")

app = App("myapp")
app.register(HelloCommand())

if __name__ == "__main__":
    app.run()
```

Run it:
```bash
python app.py hello
python app.py hello --name Alice
```

### 4. Interactive Mode

```python
from prettycli import CLI

cli = CLI("myapp")
cli.register(HelloCommand())
cli.run()  # Starts interactive shell
```

## VS Code Extension

### Install Extension

```bash
cd vscode-extension
npm install
npm run compile
```

Then press `F5` in VS Code to launch the extension in debug mode.

### Use with Python

```python
from prettycli import vscode

# Connect to VS Code
client = vscode.get_client()

# Show a chart
vscode.show_chart(
    chart_type="bar",
    labels=["A", "B", "C"],
    datasets=[{"label": "Sales", "data": [10, 20, 30]}],
    title="Sales Report"
)

# Show a table
vscode.show_table(
    columns=["Name", "Age"],
    rows=[["Alice", 30], ["Bob", 25]],
    title="Users"
)

# Show JSON
vscode.show_json({"key": "value", "nested": {"a": 1}})

# Show diff
vscode.show_diff(
    original="line1\nline2",
    modified="line1\nline2\nline3",
    original_path="old.txt",
    modified_path="new.txt"
)

# Show markdown
vscode.show_markdown("# Hello\n**Bold** and *italic*")

# Show image
vscode.show_image("/path/to/image.png", title="Screenshot")
```

### Status Bar Integration

```python
from prettycli import vscode

# Check connection status
status = vscode.get_status()
# Returns: ("VSCode", "已连接") or ("VSCode", "未连接")
```

### Artifact Variable

Configure in your CLI config (YAML):
```yaml
artifact_var: "@@$"  # Default
```

Use in commands:
```bash
> mycommand @@$
# @@$ expands to current artifact file path
```

## Project Structure

```
prettycli/
├── src/prettycli/       # Python package
│   ├── __init__.py
│   ├── app.py           # Application class
│   ├── cli.py           # Interactive CLI
│   ├── command.py       # Base command class
│   ├── context.py       # Execution context
│   ├── ui.py            # UI components
│   ├── subui/           # Status bar, etc.
│   └── vscode.py        # VS Code client API
├── vscode-extension/    # VS Code extension
│   ├── src/
│   │   ├── extension.ts
│   │   ├── apiServer.ts      # WebSocket server
│   │   ├── panelManager.ts   # Webview panels
│   │   ├── pluginManager.ts  # Renderer plugins
│   │   ├── sessionManager.ts # Artifact storage
│   │   └── renderers/        # Built-in renderers
│   └── package.json
└── tests/               # Test suite
```

## Interactive Testing Framework

PrettyCLI includes a testing framework for interactive CLI applications.

### ShellSession - Persistent Shell

```python
from prettycli.testing import ShellSession

with ShellSession() as sh:
    sh.run("cd /tmp")
    result = sh.run("pwd")  # /tmp - state persists!

    sh.export("MY_VAR", "hello")
    print(sh.env("MY_VAR"))  # hello

    # Check exit codes
    result = sh.run("ls /nonexistent")
    print(result.exit_code)  # non-zero
```

### Mock Prompts

```python
from prettycli.testing import mock_prompt, test, TestRunner

@test("should greet user")
def test_greet():
    with mock_prompt(["Alice"]):  # Simulate user input
        result = my_prompt_function()
        assert "Alice" in result

# Run tests
runner = TestRunner()
runner.discover(Path("tests/"))
runner.run()  # Returns 0 if all pass
```

### Assertions

```python
from prettycli.testing import assert_contains, assert_matches, assert_equals

assert_contains(output, "success")
assert_matches(output, r"ID: \d+")
assert_equals(result.exit_code, 0)
```

### Interactive Mode

```bash
# Run with interactive debugging (pause on failure)
python tests/test_shell_session.py -i
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev,vscode]"

# Run pytest tests
pytest

# Run interactive tests
python tests/test_shell_session.py

# Run TypeScript tests
cd vscode-extension && npm test

# Run with coverage
pytest --cov=prettycli --cov-report=term
```

## License

MIT

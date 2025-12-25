"""
Entry point for running prettycli as a module.

Usage:
    python -m prettycli
"""
from prettycli.cli import CLI

if __name__ == "__main__":
    cli = CLI("prettycli")
    cli.run()

"""Тесты парсера."""

import os
import sys

sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "src")
)
from emulator import expand_vars, parse_line


def test_parse():
    """Проверяет разбор обычной команды с аргументом."""
    cmd, args = parse_line("ls /tmp")
    assert cmd == "ls"
    assert args == ["/tmp"]


def test_empty():
    """Проверяет разбор пустой строки."""
    cmd, args = parse_line("")
    assert cmd is None


def test_comment():
    """Проверяет отсечение комментария после #."""
    cmd, args = parse_line("ls # comment")
    assert cmd == "ls"
    assert args == []


if __name__ == "__main__":
    test_parse()
    test_empty()
    test_comment()
    print("OK parser")

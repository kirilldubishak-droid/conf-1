"""Тесты VFS."""

import os
import sys

sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "src")
)
from vfs import VFS

MIN_COUNT = 1


ROOT = os.path.join(
    os.path.dirname(__file__), "..", "vfs_data"
)


def test_minimal():
    """Проверяет загрузку minimal.csv и список корня."""
    v = VFS()
    v.load_from_csv(os.path.join(ROOT, "minimal.csv"))
    assert "readme.txt" in v.list_dir("/")


def test_cd():
    """Проверяет смену каталога и список файлов."""
    v = VFS()
    v.load_from_csv(os.path.join(ROOT, "medium.csv"))
    v.change_dir("/home/user")
    assert v.current_path == "/home/user"
    assert "hello.txt" in v.list_dir(".")


def test_wc():
    """Проверяет подсчёт строк и слов в файле."""
    v = VFS()
    v.load_from_csv(os.path.join(ROOT, "medium.csv"))
    lines, words, _ = v.wc("/home/user/hello.txt")
    assert lines >= MIN_COUNT
    assert words >= MIN_COUNT


def test_find():
    """Проверяет поиск файла по имени."""
    v = VFS()
    v.load_from_csv(os.path.join(ROOT, "deep.csv"))
    r = v.find("/", "main.py")
    assert any("main.py" in x for x in r)


if __name__ == "__main__":
    test_minimal()
    test_cd()
    test_wc()
    test_find()
    print("OK vfs")

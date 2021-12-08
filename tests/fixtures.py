from pytest import fixture

from src.directories import Directory


@fixture
def directory_empty() -> Directory:
    return Directory()


@fixture
def directory_full() -> Directory:
    directory: Directory = Directory()
    directory.root = {'fruits': {'apples': {'fuji': {}}}}
    return directory

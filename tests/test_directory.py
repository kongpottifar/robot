from directory import directory
from os import path, mkdir, rmdir
from pytest import raises


def test_single_directory():
    test_dir = "test_dir"
    if path.isdir(test_dir):
        rmdir(test_dir)
    dir = directory(directory_name=test_dir)
    _ = dir.run()
    try:
        assert path.isdir(test_dir)
    finally:
        if path.isdir(test_dir):
            rmdir(test_dir)


def test_multiple_directory():
    parent_dir = "parent_dir"
    test_dir = f"{parent_dir}/test_dir"
    if path.isdir(test_dir):
        rmdir(test_dir)
    if path.isdir(parent_dir):
        rmdir(parent_dir)
    dir = directory(directory_name=test_dir)
    _ = dir.run()
    try:
        assert path.isdir(test_dir)
    finally:
        if path.isdir(test_dir):
            rmdir(test_dir)
        if path.isdir(parent_dir):
            rmdir(parent_dir)


def test_directory_error():
    test_dir = "test_dir"
    if path.isdir(test_dir):
        rmdir(test_dir)
    mkdir("test_dir")
    dir = directory(directory_name=test_dir)
    with raises(FileExistsError):
        _ = dir.run()


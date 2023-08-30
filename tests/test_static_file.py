from robot import static_file, BuildError
from pytest import raises
from os import path, remove


def test_static_file():
    test_file = "a_test_file.txt" 
    with open(test_file, "w") as f:
        f.write("This is a test file")

    ft = static_file(test_file)
    try:
        assert not ft.needs_build()
        assert ft.run()
    finally:
        if path.isfile(test_file):
            remove(test_file)
    assert ft.needs_build()


def test_static_file_error():
    test_file = "a_test_file.txt" 
    ft = static_file(test_file)
    with raises(BuildError):
        _ = ft.run()

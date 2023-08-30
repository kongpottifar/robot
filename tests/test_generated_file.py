from robot import generated_file
from pytest import raises
from os import path, remove
from robot import BuildError


def test_generate_file():
    test_file = "a_test_file.txt"
    gf = generated_file(file_name=test_file,
                        cmd = f"touch {test_file}",
                        dependencies = [])
    if path.isfile(test_file):
        remove(test_file)
    try:
        assert gf.needs_build()
        _ = gf.run()
        assert path.isfile(test_file)
    finally:
        if path.isfile(test_file):
            remove(test_file)

    
def test_generate_file_error():
    test_file = "a_test_file.txt"
    gf = generated_file(file_name=test_file,
                        cmd = f"cat {test_file}",
                        dependencies = [])
    if path.isfile(test_file):
        remove(test_file)
    with raises(BuildError):
        _ = gf.run()

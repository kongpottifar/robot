from robot import command
from pytest import raises
from robot import BuildError


def test_command():
    cmd = command(cmd_name="test_cmd", cmd="echo 'yay'", dependencies=[])
    assert cmd.run()


def test_command_error():
    cmd = command(cmd_name="test_cmd", cmd="cat 1234bobo.txt", dependencies=[])
    with raises(BuildError):
        _ = cmd.run()


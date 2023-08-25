from pytest import raises
from errors import BuildError
from robot import Robot
from toposort import CircularDependencyError


class mock_target:
    def __init__(self, dependencies: list[str], ok: bool = True):
        self.dependencies = dependencies
        self.ok = ok

    def run(self) -> bool:
        if self.ok:
            return True
        else:
            raise BuildError("Some error building")

    def needs_build(self) -> bool:
        return True


def test_robot_add():
    A = mock_target(dependencies=[])
    B = mock_target(dependencies=["A"])
    C = mock_target(dependencies=["A", "B"])

    robot = Robot()
    robot.add_target("A", A)
    robot.add_target("B", B)
    robot.add_target("C", C)

    with raises(ValueError):
        robot.add_target("C", C)


def test_dependency_check():
    A = mock_target(dependencies=[])
    B = mock_target(dependencies=["A"])
    C = mock_target(dependencies=["A", "B", "D"])

    robot = Robot()
    robot.add_target("A", A)
    robot.add_target("B", B)
    robot.add_target("C", C)

    with raises(ValueError):
        robot.check_dependencies()


def test_toposort():
    A = mock_target(dependencies=[])
    B = mock_target(dependencies=["A"])
    C = mock_target(dependencies=["A", "B"])
    D = mock_target(dependencies=["B", "C"])

    robot = Robot()
    robot.add_target("A", A)
    robot.add_target("B", B)
    robot.add_target("C", C)
    robot.add_target("D", D)

    target_list = robot.sort_targets()
    assert target_list[0] == "A"
    assert target_list[1] == "B"
    assert target_list[2] == "C"
    assert target_list[3] == "D"


def test_toposort_error():
    A = mock_target(dependencies=["D"])
    B = mock_target(dependencies=["A"])
    C = mock_target(dependencies=["A", "B"])
    D = mock_target(dependencies=["B", "C"])

    robot = Robot()
    robot.add_target("A", A)
    robot.add_target("B", B)
    robot.add_target("C", C)
    robot.add_target("D", D)

    with raises(CircularDependencyError):
        robot.sort_targets()
    

def test_build():
    A = mock_target(dependencies=[])
    B = mock_target(dependencies=["A"])
    C = mock_target(dependencies=["A", "B"])
    D = mock_target(dependencies=["B", "C"])

    robot = Robot()
    robot.add_target("A", A)
    robot.add_target("B", B)
    robot.add_target("C", C)
    robot.add_target("D", D)

    robot.build()


def test_build_error():
    A = mock_target(dependencies=[])
    B = mock_target(dependencies=["A"], ok=False)
    C = mock_target(dependencies=["A", "B"])
    D = mock_target(dependencies=["B", "C"])

    robot = Robot()
    robot.add_target("A", A)
    robot.add_target("B", B)
    robot.add_target("C", C)
    robot.add_target("D", D)
    
    with raises(BuildError):
        robot.build()




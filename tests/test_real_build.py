from robot import Robot
from robot import directory
from robot import static_file
from robot import web_file
from robot import generated_file
from robot import command
from os import path, remove, mkdir, rmdir


def test_full_build():
    sf = "a_static_file.txt"
    td = "test_dir"
    wf = "test_dir/a_web_file.txt"
    test_url = "https://gist.githubusercontent.com/kongpottifar/4145ce86303d82916997b2ad3ea54320/raw/499df95ca8515780dfbc1f609e9d8b7edb97c73e/B.txt" 
    gf = "a_generated_file.txt"
    with open(sf, "w") as f:
        f.write("Static file")

    if path.isfile(wf):
        remove(wf)

    if path.isdir(td):
        rmdir(td)

    if path.isfile(gf):
        remove(gf)

    robot = Robot()
    robot.add_target(static_file(sf))
    robot.add_target(directory(td))
    robot.add_target(web_file(file_name = wf,
                              url = test_url,
                              dependencies = [td]))
    robot.add_target(generated_file(file_name=gf,
                                    cmd = f"touch {gf}"))
    robot.add_target(command(
        cmd_name = "cat_all",
        cmd = f"cat {sf} {wf} {gf}",
        dependencies=[sf, wf, gf]))

    try:
        robot.build()
        assert path.isfile(sf)
        assert path.isdir(td)
        assert path.isfile(wf)
        assert path.isfile(gf)
    finally:
        if path.isfile(wf):
            remove(wf)

        if path.isdir(td):
            rmdir(td)

        if path.isfile(gf):
            remove(gf)

        if path.isfile(sf):
            remove(sf)






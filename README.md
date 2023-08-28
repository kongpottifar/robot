```
           _           _                 
          | |         | |                
 _ __ ___ | |__   ___ | |_   _ __  _   _ 
| '__/ _ \| '_ \ / _ \| __| | '_ \| | | |
| | | (_) | |_) | (_) | |_ _| |_) | |_| |
|_|  \___/|_.__/ \___/ \__(_) .__/ \__, |
                            | |     __/ |
                            |_|    |___/ 
```

A dirt simple python library for running functions that depends on other functions
in a topological order. It implements some convenience classes for creating or
downloading files or running commands.

## Usage

```python
from robot import Robot
from static_file import static_file
from web_file import web_file
from command import command

robot = Robot()

robot.add(static_file(file_name = "a_file.txt"))
robot.add(web_file(file_name="a_dowloaded_file.txt", url = "some_url"), dependencies=[])
robot.add(command(
                    cmd_name="concatenate_files",
                    cmd="cat a_file.txt a_dowloaded_file.txt"),
                    dependencies=["a_file.txt","a_downloaded_file.text"])

robot.build()
```

## Extending

The robot can take any instance of  a class that implements:

```python

class my_target:
    dependencies: list[str]

    def run(self) -> bool:
        ...

    def needs_build(self) -> bool:
        ...
```





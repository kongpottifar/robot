from errors import BuildError
import subprocess
import shlex
from os import path


class generated_file:
    def __init__(self, file_name: str, cmd: str, dependencies: list[str]|None = None) -> None:
        self.dependencies: list[str] = [] if dependencies is None else dependencies
        self.file_name: str = file_name
        self.cmd: list[str] = shlex.split(cmd) 

   def run(self) -> bool:
        process = subprocess.run(self.cmd, capture_output=True)
        if process.returncode != 0:
            raise BuildError(
                f"""
                Command for building {self.file_name} exited with returncode {process.returncode}
                Stderr output:
                {process.stderr}
                """)
        return True

    def needs_build(self) -> bool:
        if not path.isfile(self.file_name):
            return True
        return False
        





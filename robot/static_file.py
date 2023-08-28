from os import path
from errors import BuildError

class static_file:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.dependencies: list[str] = []

    def run(self):
        if not path.isfile(self.file_name):
            raise BuildError(f"Could not complete build. File {self.file_name} was not found.")
        return True

    def needs_build(self):
        if not path.isfile(self.file_name):
            return True
        else:
            return False

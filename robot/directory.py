from os import makedirs, path


class directory:
    def __init__(self, directory_name: str, dependencies: list[str]|None = None) -> None:
        self.directory_name: str = directory_name
        self.dependencies: list[str] = [] if dependencies is None else dependencies 

    def run(self) -> bool:
        makedirs(self.directory_name)
        return True

    def needs_build(self) -> bool:
        if not path.isdir(self.directory_name):
            return True
        return False


        


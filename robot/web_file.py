import requests
from errors import BuildError
from os import path


class web_file:
    def __init__(self, file_name: str, url: str, dependencies: list[str]):
        self.dependencies = dependencies
        self.file_name = file_name
        self.url = url

    def run(self):
        response = requests.get(self.url)
        response.raise_for_status()
        with open(self.file_name, "wb") as f:
            f.write(response.content)

        return True

    def needs_build(self):
        if not path.isfile(self.file_name):
            return True
        return False

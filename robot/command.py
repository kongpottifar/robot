import shlex
import subprocess
from robot.errors import BuildError

class command:
    def __init__(self, cmd_name: str, cmd: str, dependencies: list[str], run_when: str = "always") -> None:
        self.target_name: str = cmd_name
        self.dependencies = dependencies
        self.cmd: list[str] = shlex.split(cmd)
        self.cmd_name: str = cmd_name
        valid_values_for_run_when = ["always", "depends"]
        if run_when in valid_values_for_run_when:
            self.run_when: str = run_when
        else:
           raise ValueError(f"Parameter run_when for command {cmd_name} must"
                       f"be one of {valid_values_for_run_when}")

    def run(self) -> bool:
        process = subprocess.run(self.cmd, capture_output=True)
        if process.returncode != 0:
            raise BuildError(
                f"""
                Command {self.cmd_name} exited with returncode {process.returncode}
                Stderr output:
                {process.stderr}
                """)
        return True

    def needs_build(self):
        return self.run_when == "always"

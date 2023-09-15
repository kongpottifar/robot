from typing import Protocol
from toposort import toposort_flatten


class Target(Protocol):
    target_name: str
    dependencies: list[str]
    
    def run(self) -> bool:
        ...

    def needs_build(self) -> bool:
        ...


class Robot:
    def __init__(self) -> None:
        self.targets: dict[str, Target] = dict()
        self.check_tree = False

    def add_target(self, target: Target) -> None:
        if target.target_name in self.targets:
            raise ValueError(f"Can not add target. Target {target.target_name} already exists")
        self.targets[target.target_name] = target
        
    def check_dependencies(self) -> None:
        for target in self.targets.values():
            for dependency in target.dependencies:
                if not dependency in self.targets:
                    raise ValueError(f"Dependency {dependency} has not been defined as a target")
        self.check_tree = True

    def sort_targets(self) -> list[str]:
        tree = {t: set(d.dependencies) for t, d in self.targets.items()}
        return toposort_flatten(tree)

    def build(self) -> None:
        print("Starting build...")
        if not self.check_tree:
            print("Checking dependencies...")
            self.check_dependencies()
            self.check_tree = True

        print("Generating build sequence...")
        sorted_targets = self.sort_targets()
        build_sequence = []
        for target_name in sorted_targets:
            target = self.targets[target_name]
            if target.needs_build():
                build_sequence.append(target_name)
            elif any([dependency in build_sequence for dependency in target.dependencies]):
                build_sequence.append(target_name)

        if not build_sequence:
            print("Nothing to build. Build complete!")
            return
        n_builds = len(build_sequence)
        for i, target_name in enumerate(build_sequence):
            print(f"{i+1}/{n_builds}: Building target {target_name}...", end="")
            _ = self.targets[target_name].run()
            print(" Completed!")
        
        print("Build complete!")




        



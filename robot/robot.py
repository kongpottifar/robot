from typing import Protocol
from toposort import toposort_flatten


class Target(Protocol):
    dependencies: list[str]
    
    def run(self) -> bool:
        ...

    def needs_build(self) -> bool:
        ...


class Robot:
    def __init__(self) -> None:
        self.targets: dict[str, Target] = dict()
        self.check_tree = False

    def add_target(self, target_name: str, target: Target) -> None:
        if target_name in self.targets:
            raise ValueError(f"Can not add target. Target {target_name} is already exists")
        self.targets[target_name] = target
        
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
        if not self.check_tree:
            self.check_dependencies()
            self.check_tree = True

        sorted_targets = self.sort_targets()
        build_sequence = []
        for target_name in sorted_targets:
            target = self.targets[target_name]
            if target.needs_build():
                build_sequence.append(target_name)
            elif any([dependency in build_sequence for dependency in target.dependencies]):
                build_sequence.append(target_name)
        for target_name in build_sequence:
            _ = self.targets[target_name].run()
            print(f"Building target {target_name}")





        



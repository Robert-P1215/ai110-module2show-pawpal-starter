from dataclasses import dataclass, field
from datetime import time
from typing import List

PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


@dataclass
class Task:
    name: str
    description: str
    time: time
    priority: str
    completion_status: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completion_status = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Append a task to this pet's task list."""
        self.tasks.append(task)

    def remove_task(self, task_name: str) -> None:
        """Remove a task by name from this pet's task list."""
        self.tasks = [t for t in self.tasks if t.name != task_name]

    def get_tasks(self) -> List[Task]:
        """Return all tasks assigned to this pet."""
        return self.tasks


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet by name from this owner's pet list."""
        self.pets = [p for p in self.pets if p.name != pet_name]

    def get_pets(self) -> List[Pet]:
        """Return all pets belonging to this owner."""
        return self.pets


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner

    def build_schedule(self) -> List[Task]:
        """Collect all incomplete tasks across the owner's pets and return them sorted."""
        all_tasks = []
        for pet in self.owner.get_pets():
            for task in pet.get_tasks():
                if not task.completion_status:
                    all_tasks.append(task)
        return self.sort_tasks(all_tasks)

    def sort_tasks(self, tasks: List[Task], key: str = "priority") -> List[Task]:
        """Sort tasks by priority (high→low) then time, or by time alone if key='time'."""
        if key == "time":
            return sorted(tasks, key=lambda t: t.time)
        return sorted(tasks, key=lambda t: (PRIORITY_ORDER.get(t.priority, 99), t.time))

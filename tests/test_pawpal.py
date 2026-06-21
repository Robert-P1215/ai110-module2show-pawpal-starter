from datetime import time
from pawpal_system import Task, Pet


def test_mark_complete_changes_status():
    task = Task(name="Morning Walk", description="Walk the dog", time=time(7, 0), priority="high")
    assert task.completion_status is False
    task.mark_complete()
    assert task.completion_status is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task(name="Evening Feed", description="One cup of dry food", time=time(18, 0), priority="medium"))
    assert len(pet.get_tasks()) == 1
